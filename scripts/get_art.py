#!/usr/bin/env python3

import requests, json, argparse, re, io, os
import google.auth
import google.auth.transport.requests
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

scopes = "https://www.googleapis.com/auth/drive.readonly"


def get_creds(credentials_file):
    creds, project = google.auth.load_credentials_from_file(
        credentials_file, scopes=[scopes]
    )
    auth_req = google.auth.transport.requests.Request()
    creds.refresh(auth_req)
    return creds


def list_files(service):
    results = (
        service.files()
        .list(
            pageSize=250,
            fields="nextPageToken, files(id, name, mimeType, createdTime, modifiedTime, parents, description, md5Checksum)",
        )
        .execute()
    )
    items = results.get("files", [])
    return items


def sort_files(files):
    def _get_path(file, path=None):
        parent_id = file.get("parents")
        if parent_id is None:
            # Remove the top-level folder
            del path[-1]
            path.reverse()
            return "-".join(path)
        else:
            parent_id = parent_id[0]
            parent_file = id_to_file[parent_id]
            parent_name_formatted = parent_file["name"].lower().replace(" ", "-")
            if path is None:
                path = [parent_name_formatted]
            else:
                path.append(parent_name_formatted)
            return _get_path(parent_file, path)

    id_to_file = {file["id"]: file for file in files}
    punctuation = "!#$%&\"'()*+,./:;<=>?@[\\]^_`{|}~"

    files_formatted = dict()
    for file in files:
        if file["mimeType"].split("/")[0] == "image":
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

            file_id = name.lower().replace(" ", "-")
            for char in punctuation:
                file_id = file_id.replace(char, "")

            file_obj = {
                "id": file_id,
                "file": file["name"].replace("?", "").replace("#", ""),
                "name": name,
                "drive_id": file["id"],
                "medium": medium,
                "md5Checksum": file.get("md5Checksum", None),
            }

            path = _get_path(file)
            if path in files_formatted:
                files_formatted[path].append(file_obj)
            else:
                files_formatted[path] = [file_obj]

    # Set the first item in the Digital array to the file with ID breakfast-c2020
    first_image_index = [
        item
        for item in files_formatted["illustrations-digital"]
        if item["id"] == "breakfast-c2020"
    ][0]
    files_formatted["illustrations-digital"].insert(
        0,
        files_formatted["illustrations-digital"].pop(
            files_formatted["illustrations-digital"].index(first_image_index)
        ),
    )
    return files_formatted


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
    if file_obj["md5Checksum"] in downloaded_checksums and os.path.isfile(
        asset_dir + "/" + file_obj["file"]
    ):
        return True
    else:
        return False


def get_files(files, asset_dir, service, downloaded_checksums):
    def _download_file(file_obj):
        file_exists = check_file_exists(file_obj, downloaded_checksums, asset_dir)
        if not file_exists:
            print("Downloading file {}".format(file_obj["file"]))
            request = service.files().get_media(fileId=file_obj["drive_id"])
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
    drive_service = build("drive", "v3", credentials=creds)
    files = list_files(drive_service)
    sorted_files = sort_files(files)

    downloaded_checksums = load_previous_metadata(metadata_file)
    get_files(sorted_files, asset_directory, drive_service, downloaded_checksums)
    write_metadata(sorted_files, metadata_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scrape the drive folder where Jessi uploads her art for new entries"
    )
    parser.add_argument(
        "-c",
        "--credentials",
        type=str,
        help="Credentials JSON file for the app accessing the drive folder",
        required=True,
    )
    parser.add_argument(
        "-a",
        "--asset_directory",
        type=str,
        help="Directory to save image files and metadata to",
        required=True,
    )

    args = parser.parse_args()
    main(args)
