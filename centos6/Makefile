SUBDIRS := eds eds80

image: $(SUBDIRS)

clean: $(SUBDIRS)
	docker rmi centos:centos6

$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: image clean $(SUBDIRS)
