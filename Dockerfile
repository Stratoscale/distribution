FROM golang:1.6-alpine

ENV DISTRIBUTION_DIR /go/src/github.com/docker/distribution
ENV DOCKER_BUILDTAGS include_oss include_gcs

WORKDIR $DISTRIBUTION_DIR
COPY . $DISTRIBUTION_DIR
COPY cmd/registry/config-dev.yml /etc/docker/registry/config.yml
COPY cmd/registry/config-read-only.yml /etc/docker/registry/config-read-only.yml

RUN set -ex \
    && apk add --no-cache make git

RUN make PREFIX=/go clean binaries

VOLUME ["/var/lib/registry"]
EXPOSE 1818
ENTRYPOINT ["registry"]
CMD ["serve", "/etc/docker/registry/config.yml"]
