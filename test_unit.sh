#!/bin/bash

# Copyright (c) Huawei Technologies Co., Ltd. 2021. All rights reserved.
# Description: This shell script is used to do unit test.
# Author: xiadanni1@huawei.com
# Create: 2021-12-20                                                     

test_log=${PWD}/unit_test_log
rm -rf "${test_log}"
touch "${test_log}"
while IPF= read -r line
do
    echo "Start to test: ${line}"
    go test -timeout 300s -v "${line}" >> "${test_log}"
    cat "${test_log}" | grep -E -- "--- FAIL:|^FAIL"
    if [ $? -eq 0 ]; then
        echo "Testing failed... Please check ${test_log}"
        exit 1
    fi
    tail -n 1 "${test_log}"
done < "unit_test_list"
