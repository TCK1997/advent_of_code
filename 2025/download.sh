#!/bin/bash

day=$1
session=$2
curl "https://adventofcode.com/2025/day/${day}/input" \
  -H "authority: adventofcode.com" \
  -H "cookie: session=${session}" \
  --compressed \
  -o "day_${day}.input"
