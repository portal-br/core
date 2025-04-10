# syntax=docker/dockerfile:1.9
FROM ubuntu:noble

ARG PYTHON_VERSION=3.12
ARG PB_VERSION

SHELL ["sh", "-exc"]
ENV DEBIAN_FRONTEND=noninteractive
RUN <<EOT
    buildDeps="build-essential busybox ca-certificates curl git gosu libbz2-dev libffi-dev libjpeg-turbo8-dev libmagic1 libsasl2-dev libldap2-dev libopenjp2-7-dev libpcre3-dev libpq-dev libssl-dev libtiff6 libtiff5-dev libxml2-dev libxslt1-dev python3-setuptools python$PYTHON_VERSION-dev wget zlib1g-dev"
    apt-get update -qy
    apt-get install -qyy \
        -o APT::Install-Recommends=false \
        -o APT::Install-Suggests=false \
        $buildDeps
    busybox --install -s
EOT

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python$PYTHON_VERSION \
    UV_PROJECT_ENVIRONMENT=/app

# Script used for pre-compilation of po files
COPY /container/compile_mo.py /compile_mo.py

# Copy default structure for a Plone Project
COPY /container/skeleton /app

LABEL maintainer="PloneGov-BR <gov@plone.org.br>" \
      org.label-schema.name="ghcr.io/portal-br/core-builder" \
      org.label-schema.description="PortalBrasil $PB_VERSION builder image with Python $PYTHON_VERSION" \
      org.label-schema.vendor="PloneGov-BR"
