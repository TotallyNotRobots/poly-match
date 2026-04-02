FROM mcr.microsoft.com/devcontainers/python:3.14@sha256:1af48f9bd555f7972b14424def113c166dab9c5027bd9d9f5cc57704a42974f2

RUN \
    pipx uninstall mypy \
    && pipx uninstall pylint \
    && pipx uninstall pytest \
    && pipx uninstall flake8 \
    && pipx uninstall black

RUN pipx install commitizen \
    && pipx install hatch

RUN umask 0002 \
    && mkdir -p ${PIPX_BIN_DIR} \
    && chown -R "vscode:pipx" ${PIPX_HOME} \
    && chmod -R g+r+w "${PIPX_HOME}"

RUN su vscode -c "hatch config set dirs.env.virtual /home/vscode/.virtualenvs"

ENV SHELL /bin/bash
