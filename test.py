import docker
c = docker.from_env()
c.build('.', testimage)


