#!/bin/bash
# Gets the size of the body of a response from a URL
curl -sI $1 | grep -i content-length | awk '{print $2}'
