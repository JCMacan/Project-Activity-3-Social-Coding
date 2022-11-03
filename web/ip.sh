#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp ip.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

cd tempdir
docker build -t ip .
docker rm -f iprunning
docker run -t -d -p 5000:5000 --name iprunning ip
docker ps -a
