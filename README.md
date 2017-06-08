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
