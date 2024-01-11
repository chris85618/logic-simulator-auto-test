#!/bin/bash
ulimit -n 1024
# Execute the input arguments
${@:1}
