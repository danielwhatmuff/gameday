#!/bin/bash

ENV=$1

if [ "$ENV" = "" ]; then
   ENV="dev"
fi

echo "SETTING collector/settings/${ENV}_settings.py to settings"
cp collector/settings/${ENV}_settings.py collector/settings/__init__.py

echo "DEPLOYING to $ENV"
zappa deploy $ENV

