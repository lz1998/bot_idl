#!/usr/bin/env bash

protoc -I . --proto_path=${dir} --java_out . *.proto
protoc -I . --proto_path=${dir} --python_out . *.proto

