#! /bin/bash

#
cd $(dirname $0)

#
docker run \
    --rm \
    -v $(pwd):/work \
    -it leapsolutionsasia/python-bss-client $*
