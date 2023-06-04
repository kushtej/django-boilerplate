#!/bin/bash

# Give permission before run:
# chmod +x init.sh
# sudo ./init.sh

GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

present_working_directory=$(pwd)
venv_directory=$(pwd)
venv_directory+=/venv/bin/activate

if [ $# -eq 1 ]
  then
    if [[ $1 == --help ]]; then
        printf "\nThese are all available commands in Installation :\n"
        printf "${YELLOW}\t--help\t\t\t${NC}Check flags\n${NC}"
    fi
    exit 0
fi


printf "${YELLOW}\n\nChecking Essential packages...\n\n${NC}"
essential_packages=('python3.8' 'pip' 'virtualenv')
essential_packages_length=${#essential_packages[@]}

packages=0

for i in "${essential_packages[@]}"
do
    printf "${YELLOW}\n\nChecking for ${i}\n\n${NC}"
    files=$(which $i)
    if [[ $? != 0 ]]; then
        printf "\n${RED}$i does not exists!\t${YELLOW}Install $i\n${NC}"
        exit 0
    elif [[ $files ]]; then
        printf "${GREEN}$i exists!\n${NC}"
        packages=$[$packages +1]
    else
        printf "\n${RED}$i does not exists!\t${YELLOW}Install $i\n${NC}"
        exit 0
    fi
done

printf "${YELLOW}\nMigrating Database...${NC}\n\n"
python3 src/manage.py migrate
python3 src/manage.py makemigrations
python3 src/manage.py migrate
printf "\n\n${GREEN}Database migrations completed.${NC}\n\n"

printf "\n\n${GREEN}Installation Successfull!{NC}\n\n"