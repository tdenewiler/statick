FROM python:3.7-slim-buster

LABEL Name = "Statick"
LABEL Maintainer = "NIWC"
LABEL Version = "0.4.4"

USER root

RUN mkdir -p /usr/share/man/man1

RUN apt update && apt install -y \
    bandit \
    build-essential \
    chktex \
    clang \
    clang-6.0 \
    clang-format \
    clang-format-6.0 \
    clang-tidy \
    clang-tidy-6.0 \
    cmake \
    cppcheck \
    flawfinder \
    git \
    lacheck \
    libomp-dev \
    libperl-critic-perl \
    libxml2 \
    maven \
    pylint \
    python3-pylint-django \
    python3-yaml \
    python3-yapsy \
    wget
RUN pip install --upgrade pip
RUN pip install \
    cmakelint \
    cpplint \
    flake8 \
    flake8-blind-except \
    flake8-builtins \
    flake8-class-newline \
    flake8-comprehensions \
    flake8-docstrings \
    flake8-import-order \
    flake8-quotes \
    lizard \
    statick \
    statick-md \
    statick-tex \
    statick-web \
    yamllint

RUN useradd -ms /bin/bash statick
USER statick
WORKDIR /home/statick
