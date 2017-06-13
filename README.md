This repository serves as a test platform for a fix to a Shibboleth
Embedded Discover Service configuration issue with Apache 2.4 on Centos 7.

See https://issues.shibboleth.net/jira/projects/EDS/issues/EDS-80

# 1. Install docker

Follow the
[docker installation instructions](https://docs.docker.com/engine/installation/)
for your platform.

# Build EDS images

Four images are built by the `buildimages` script. These images are a
vanilla EDS installation and EDS with the
[EDS-80 fix](https://issues.shibboleth.net/jira/secure/attachment/13631/shibboleth-ds.conf)
applied on both CentOS 6 (Apache 2.2) and CentOS 7 (Apache 2.4).

```
./buildimages
```

You can see the commands used to configure these images in their
respective Dockerfiles:

* centos6/eds/Dockerfile
* centos6/eds80/Dockerfile
* centos7/eds/Dockerfile
* centos7/eds80/Dockerfile


# Run tests

Use the `test-eds` script to test each image. You'll see a printout in
green that shows success for three of the images, and a printout in red
for CentOS 7 with vanilla EDS installed. This script demonstrates that
the EDS-80 fix works on both CentOS 6 (Apache 2.2) and CentOS 7 (Apache 2.4).

```
./test-eds
```

# Clean up

The constructed EDS images can be deleted using the `delimages` script.
After this script is run there will still be the two base CentOS images:
centos:centos6 and centos:centos7.
