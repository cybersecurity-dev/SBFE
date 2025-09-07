FROM ubuntu:latest

LABEL org.label-schema.name='SFET - Ubuntu' \
    org.label-schema.usage='https://github.com/cybersecurity-dev' \
    org.label-schema.url='https://github.com/cybersecurity-dev' \
    org.label-schema.vendor='https://cyberthreatdefence.com/' \
    MAINTAINER="Cyber Threat Defence Center"

# Set environment variables
ENV DEBCONF_NOWARNINGS=yes \
    DEBIAN_FRONTEND=noninteractive \
    TERM=xterm-256color \
    PIP_ROOT_USER_ACTION=ignore

ENV OPT=/opt
ENV TMP=/tmp
ENV SRC=/src

SHELL ["/bin/bash", "-c"]

# Install base utilities
RUN apt-get -y update && apt-get -y upgrade \
    && apt-get install -y build-essential \
    && apt-get install -y wget \
    && apt-get install -y git-all \
    && apt-get install -y linux-headers-generic \
    && apt-get install -y python3-dev python3-venv \
    && apt-get -y autoremove \
    && apt-get -y autoclean \ 
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/cybersecurity-dev/SFET.git $SRC/SFET \
    && ls -al $SRC

# Install
RUN cd $SRC/SFET && python3 -m venv workspace_sbfe \
    && source workspace_sbfe/bin/activate \
    && pip install --upgrade pip \
    && pip install -r $SRC/SFET/requirements.txt

CMD ["python3", "/src/SFET/src/sfet.py"]