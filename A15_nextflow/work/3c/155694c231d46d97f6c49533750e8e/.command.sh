#!/bin/bash -ue
echo 'Hello World' | awk '{ print toupper($0) }'
