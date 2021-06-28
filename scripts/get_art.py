#!/usr/bin/env python3

import requests, json, argparse, re, io, os
import google.auth
import google.auth.transport.requests
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

scopes = "https://www.googleapis.com/auth/drive.readonly"

def get_creds(credentials_file):
	creds, project = google.auth.load_credentials_from_file(credentials_file, scopes = [scopes])
	auth_req = google.auth.transport.requests.Request()
	creds.refresh(auth_req)
	return creds


def list_files(service):
	results = service.files().list(pageSize=250, fields="nextPageToken, files(id, name, mimeType, createdTime, modifiedTime, parents, description, md5Checksum)").execute()
	items = results.get("files", [])
	return items


def sort_files(files):
	punctuation = "!#$%&\"'()*+,./:;<=>?@[\\]^_`{|}~"

	folder_id_to_name = {}
	for file in files:
		if file["mimeType"] == "application/vnd.google-apps.folder":
			name = file["name"].lower().replace(" ", "-")
			folder_id_to_name[file["id"]] = name

	sorted_files = {category: list() for category in folder_id_to_name.values()}
	for file in files:
		if not file["mimeType"] == "application/vnd.google-apps.folder":
			parent = file["parents"][0]
			description = file.get("description", None)
			if description:
				description_split = description.split("\n")
				name = description_split[0]
				try:
					medium = description_split[1]
				except IndexError:
					medium = ""
			else:
				name = re.sub("\.[^.]*$", "", file["name"])
				medium = ""

			id = name.lower().replace(" ", "-")
			for char in punctuation:
				id = id.replace(char, "")

			file_obj = {
				"id": id,
				"file": file["name"].replace("?", "").replace("#", ""),
				"name": name,
				"drive_id": file["id"],
				"medium": medium,
				"md5Checksum": file.get("md5Checksum", None),
			}

			sorted_files[folder_id_to_name[parent]].append(file_obj)

	# Set the first item in the Digital array to the file with ID breakfast-c2020
	first_image_index = [item for item in sorted_files["digital"] if item["id"] == "breakfast-c2020"][0]
	sorted_files["digital"].insert(0, sorted_files["digital"].pop(sorted_files["digital"].index(first_image_index)))
	sorted_files.pop("jessi-art", None)
	return sorted_files


def load_previous_metadata(metadata_file):
	downloaded_checksums = []
	try:
		with open(metadata_file, "r") as f:
			previous_metadata = json.load(f)
		for category, items in previous_metadata.items():
			for item in items:
				downloaded_checksums.append(item["md5Checksum"])
		return downloaded_checksums
	except FileNotFoundError:
		return downloaded_checksums


def check_file_exists(file_obj, downloaded_checksums, asset_dir):
	if file_obj["md5Checksum"] in downloaded_checksums and os.path.isfile(asset_dir + "/" + file_obj["file"]):
		return True
	else:
		return False


def get_files(files, asset_dir, service, downloaded_checksums):
	def _download_file(file_obj):
		file_exists = check_file_exists(file_obj, downloaded_checksums, asset_dir)
		if not file_exists:
			print("Downloading file {}".format(file_obj["file"]))
			request = service.files().get_media(fileId = file_obj["drive_id"])
			fh = io.FileIO(asset_dir + "/" + file_obj["file"], "w+")
			downloader = MediaIoBaseDownload(fh, request)
			done = False
			while done is False:
				status, done = downloader.next_chunk()

	for category, files in files.items():
		for file_obj in files:
			_download_file(file_obj)


def write_metadata(files, metadata_file):
	with open(metadata_file, "w+") as f:
		json.dump(files, f)


def main(args):
	asset_directory = args.asset_directory
	metadata_file = asset_directory + "/metadata.json"

	if not os.path.isdir(asset_directory):
		os.mkdir(asset_directory)

	creds = get_creds(args.credentials)
	drive_service = build('drive', 'v3', credentials = creds)
	files = list_files(drive_service)
	sorted_files = sort_files(files)

	downloaded_checksums = load_previous_metadata(metadata_file)
	get_files(sorted_files, asset_directory, drive_service, downloaded_checksums)
	write_metadata(sorted_files, metadata_file)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = "Scrape the drive folder where Jessi uploads her art for new entries")
	parser.add_argument("-c", "--credentials", type=str, help="Credentials JSON file for the app accessing the drive folder", required=True)
	parser.add_argument("-a", "--asset_directory", type=str, help="Directory to save image files and metadata to", required=True)

	args = parser.parse_args()
	main(args)
