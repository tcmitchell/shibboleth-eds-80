.PHONY: image clean

IMAGE_NAME = eds:centos7

image:
	docker build -t $(IMAGE_NAME) .

clean:
	docker rmi $(IMAGE_NAME)
