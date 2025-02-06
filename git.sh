#!/bin/sh
ts=$(date "+%Y-%m-%d|%H:%M")
#echo $ts
git add .
git commit -m $ts
git push origin main
