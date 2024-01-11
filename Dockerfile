FROM python:3.11-alpine

RUN apk add --no-cache alpine-sdk bash py3-virtualenv valgrind

ARG SOURCE_PATH="/source"

RUN mkdir -p ${SOURCE_PATH}
WORKDIR ${SOURCE_PATH}

COPY requirements.txt ${SOURCE_PATH}
COPY Makefile ${SOURCE_PATH}
RUN make virtualenv
COPY . /source

VOLUME [ "/source/src" ]
VOLUME [ "/source/report" ]
CMD make
