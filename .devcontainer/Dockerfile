FROM mcr.microsoft.com/devcontainers/python:0-3.11-bullseye

ENV PYTHONUNBUFFERED 1

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

## Installing Requirements for mariadb connector
## https://mariadb.com/docs/skysql-previous-release/connect/programming-languages/c/install/#Installation_via_Package_Repository_(Linux)

RUN cd
RUN sudo apt install wget
RUN wget https://r.mariadb.com/downloads/mariadb_repo_setup
RUN chmod +x mariadb_repo_setup
RUN sudo ./mariadb_repo_setup --mariadb-server-version="mariadb-10.11"
RUN sudo apt install -y libmariadb3 libmariadb-dev
