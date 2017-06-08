# Build

```
docker build . -t testing:centos6
```

## Build from GitHub

See
https://docs.docker.com/engine/reference/commandline/build/#parent-command

# Run

This maps local port 8080 to container port 80

```shell
docker run -p8080:80 -d testing:centos6
```

# Test

```shell
curl http://localhost:8080/
```

# Halt

```shell
docker ps
```

```shell
docker stop <container ID>
```

```shell
wget http://localhost:8080/shibboleth-ds/idpselect_config.js
```

Run with patch on CentOS 6:

```shell
docker run -d -p 8080:80 --rm --name eds6-80 eds80:centos6
```

Verify idpselect_config.js:

```shell
$ sha1sum idpselect_config.js
24d749f9993ec58e6e170b482030145cbf0d0923  idpselect_config.js
```

Alternately:

```shell
wget -O - http://localhost:8080/shibboleth-ds/idpselect_config.js | sha1sum -
```

```
docker build -t eds80:centos6 .
```
