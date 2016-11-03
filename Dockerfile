# Set the base image to use to Ubuntu
FROM ubuntu:14.04

MAINTAINER Prasanna Rishiraj

ENV DOCKYARD_SRC=cvsms_django

ENV DOCKYARD_PROJDIR=/projdir

ENV DOCKYARD_CVSMSPROJ=/projdir/cvsms_django

# Update the default application repository sources list
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python python-pip

# Create application subdirectories
WORKDIR $DOCKYARD_PROJDIR

COPY $DOCKYARD_SRC $DOCKYARD_CVSMSPROJ

RUN pip install -r $DOCKYARD_CVSMSPROJ/requirements.txt


EXPOSE 8000

WORKDIR $DOCKYARD_CVSMSPROJ
COPY ./entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
