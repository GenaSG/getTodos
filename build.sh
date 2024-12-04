#!/bin/bash
pip3 install --upgrade --target ./lib/ todoist_api_python
zip -x ./env/**\* -x ./**/__pycache__/**\* -x build.sh -r ../getTodos.zip *
echo '#!/usr/bin/env python3' | cat - ../getTodos.zip > ../getTodos.pyz
chmod +x ../getTodos.pyz 
