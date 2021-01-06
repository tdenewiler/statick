#!/usr/bin/env bash

EXIT_CODE=0

mkdir -p /tmp/statick_output

if [ -f /tmp/statick_package/requirements.txt ]
then
    python3 -m pip install -r /tmp/statick_package/requirements.txt
fi

statick /tmp/statick_package \
        --output-directory /tmp/statick_output \
        --user-paths /tmp/statick_config \
        --profile "${STATICK_PROFILE}"

exit "$EXIT_CODE"
