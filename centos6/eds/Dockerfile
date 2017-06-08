FROM centos:centos6

# Add the shibboleth repository
ADD http://download.opensuse.org/repositories/security://shibboleth/CentOS_CentOS-6/security:shibboleth.repo /etc/yum.repos.d

RUN yum update
RUN yum -y install httpd shibboleth-embedded-ds

# Do we need sudo?
# RUN yum -y install sudo

RUN yum clean all

# Run Apache in the foreground when running this container
ENTRYPOINT [ "/usr/sbin/httpd", "-D", "FOREGROUND" ]
