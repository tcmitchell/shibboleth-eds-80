FROM eds:centos7

# Install the EDS-80 patched httpd conf file
ADD https://issues.shibboleth.net/jira/secure/attachment/13631/shibboleth-ds.conf /etc/httpd/conf.d

# Run Apache in the foreground when running this container
ENTRYPOINT [ "/usr/sbin/httpd", "-D", "FOREGROUND" ]
