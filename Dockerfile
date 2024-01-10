FROM python:3.11-alpine

RUN apk add --no-cache alpine-sdk bash

ARG SOURCE_PATH="/source"
ARG REQUIREMENTS_PATH="${SOURCE_PATH}/requirements.txt"

RUN mkdir -p ${SOURCE_PATH}
WORKDIR ${SOURCE_PATH}

COPY requirements.txt ${REQUIREMENTS_PATH}
RUN pip3 install --upgrade pip && pip3 install -r ${REQUIREMENTS_PATH}
COPY . /source

VOLUME [ "/source/src" ]
VOLUME [ "/source/report" ]
CMD make
