export WEIRDFOODSTUDIO_FRONTEND_VERSION=$$(git rev-parse --short HEAD)
export WEIRDFOODSTUDIO_FRONTEND_IMAGE="weirdfoodstudio-front:${WEIRDFOODSTUDIO_FRONTEND_VERSION}"

build:
	rm -rf docker/target
	mkdir -p docker/target
	cp -r package.json src tests docker/target
	cd docker && docker build --rm -t ${WEIRDFOODSTUDIO_FRONTEND_IMAGE} .
	docker tag  ${WEIRDFOODSTUDIO_FRONTEND_IMAGE} weirdfoodstudio-front:latest
