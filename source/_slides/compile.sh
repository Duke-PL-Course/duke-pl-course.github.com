#!/bin/sh

DIR=$(pwd)

for f in *.md; do
  BASE=${f%.md}
  python render.py -i $f -o $DIR/../slides/$BASE.html
done
