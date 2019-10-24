#!/bin/bash

# this script is meant to be used with 'datalad run'

pip install -r scripts/requirements_preprocess_parlai.txt --upgrade
if [ $? -ne 0 ]; then
   echo "Failed to install requirements: pip install: $?"
   return $?
fi

git-annex direct --fast
python scripts/preprocess_parlai.py
git-annex indirect --fast

# Delete raw files
git rm personachat.tgz

