#!/bin/bash


tar --exclude ".*" \
    --exclude "*.properties" \
    -czvf cumulus-geoproc-test-data.tar.gz ./fixtures
