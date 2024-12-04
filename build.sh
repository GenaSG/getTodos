#!/bin/bash
pip3 install --upgrade --target ./lib/ todoist_api_python
zip -x ./env/**\* -x ./**/__pycache__/**\* -x build.sh -r ../getTasks.zip *
echo '#!/usr/bin/env python3' | cat - ../getTasks.zip > ../getTasks.pyz
chmod +x ../getTasks.pyz 
