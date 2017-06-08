FROM centos:centos7

# Add the shibboleth repository
ADD http://download.opensuse.org/repositories/security://shibboleth/CentOS_7/security:shibboleth.repo /etc/yum.repos.d

RUN yum update
RUN yum -y install httpd shibboleth-embedded-ds
RUN yum clean all

# Run Apache in the foreground when running this container
ENTRYPOINT [ "/usr/sbin/httpd", "-D", "FOREGROUND" ]
