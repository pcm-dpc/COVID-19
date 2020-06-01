#!/bin/bash
# execute with sudo

# pull data from repository
sudo runuser -l covid -c 'git -C absolute_path_to_COVID-19_repository pull'

# push data in database
sudo su postgres -c 'sh absolute_path_to_scripts/auto_update.sh'
