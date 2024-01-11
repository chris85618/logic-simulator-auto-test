FROM python:3.11-alpine

RUN apk add --no-cache alpine-sdk bash py3-virtualenv valgrind

ARG SOURCE_PATH="/source"

# Setup a normal user
ARG USERNAME="tester"
RUN adduser -D ${USERNAME}

RUN mkdir -p ${SOURCE_PATH} && chown ${USERNAME} ${SOURCE_PATH}
USER ${USERNAME}
WORKDIR ${SOURCE_PATH}

COPY requirements.txt ${SOURCE_PATH}
COPY Makefile ${SOURCE_PATH}
RUN make virtualenv
COPY . ${SOURCE_PATH}

VOLUME [ "${SOURCE_PATH}/src" ]
VOLUME [ "${SOURCE_PATH}/report" ]

ENTRYPOINT ["/source/docker-entrypoint.sh"]
CMD ["make"]
