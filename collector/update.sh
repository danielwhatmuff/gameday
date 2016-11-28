#!/bin/bash

ENV=$1

if [ "$ENV" = "" ]; then
   ENV="dev"
fi

echo "SETTING collector/settings/$ENV_settings.py to settings"
cp collector/settings/$ENV_settings.py collector/settings/__init__.py

echo "UPDATING to $ENV"
zappa update $ENV

