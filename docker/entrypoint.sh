#!/usr/bin/env bash

if [ ! -d /tmp/statick_output ]
then
    mkdir /tmp/statick_output
fi

if [ -f /tmp/statick_package/requirements.txt ]
then
    python3 -m pip install -r /tmp/statick_package/requirements.txt
fi

statick /tmp/statick_package --output-directory /tmp/statick_output --user-paths /tmp/statick_config --profile "${STATICK_PROFILE}"
