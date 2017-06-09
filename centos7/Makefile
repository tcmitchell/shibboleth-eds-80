SUBDIRS := eds eds80

image: $(SUBDIRS)

clean: $(SUBDIRS)
	docker rmi centos:centos7

$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: image clean $(SUBDIRS)
