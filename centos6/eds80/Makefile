.PHONY: image clean

IMAGE_NAME = eds80:centos6

image:
	docker build -t $(IMAGE_NAME) .

clean:
	docker rmi $(IMAGE_NAME)
