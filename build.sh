#!/usr/bin/env bash

protoc -I . --proto_path=${dir} --java_out . *.proto

