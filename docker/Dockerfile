FROM ubuntu:20.04

LABEL "com.github.actions.name"="Statick"
LABEL "com.github.actions.description"="Making code quality easier."
LABEL "com.github.actions.icon"="check-circle"
LABEL "com.github.actions.color"="blue"

LABEL "repository"="https://github.com/sscpac/statick.git"
LABEL "homepage"="https://github.com/sscpac/statick"
LABEL "maintainer"="Thomas Denewiler <tdenewiler@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive

USER root

RUN apt update && apt install -y --no-install-recommends \
    bandit \
    build-essential \
    cccc \
    chktex \
    clang \
    clang-6.0 \
    clang-10 \
    clang-format \
    clang-format-6.0 \
    clang-format-10 \
    clang-tidy \
    clang-tidy-6.0 \
    clang-tidy-10 \
    cmake \
    cppcheck \
    curl \
    file \
    findbugs \
    flawfinder \
    git \
    lacheck \
    libomp-dev \
    libperl-critic-perl \
    libxml2 \
    libxml2-utils \
    maven \
    pylint \
    python3-pip \
    python3-pylint-django \
    python3-yaml \
    python3-yapsy \
    shellcheck \
    uncrustify \
    wget
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install \
    black \
    cmakelint \
    cpplint \
    docformatter \
    flake8 \
    flake8-blind-except \
    flake8-builtins \
    flake8-class-newline \
    flake8-comprehensions \
    flake8-docstrings \
    flake8-import-order \
    flake8-quotes \
    mypy \
    lizard \
    statick \
    statick-md \
    statick-tex \
    statick-web \
    yamllint

# Statick npm tools.
# Have to install newer version from non-apt source due to SSL library compatibility issues.
RUN curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt update && apt install -y nodejs
RUN npm config set prefix -g /usr
RUN npm install -g \
    prettier \
    eslint@5.16.0 \
    eslint-plugin-html \
    eslint-plugin-prettier \
    eslint-config-prettier \
    htmllint-cli \
    markdownlint-cli@0.21.0 \
    stylelint \
    stylelint-config-standard

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["package"]
