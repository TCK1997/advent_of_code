#!/bin/bash

year=$1
day=$2
session=$3
curl "https://adventofcode.com/${year}/day/${day}/input" \
  -H "cookie: session=${session}" \
  --compressed \
  -o "$(pwd)/day_${day}.input"
