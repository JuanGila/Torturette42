#!/bin/bash
docker exec -it --workdir $PWD run-hades python3 /torturette/main.py "$@"
