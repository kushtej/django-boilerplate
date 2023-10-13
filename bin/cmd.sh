#!/bin/sh

THISDIR=$(cd "$(dirname "$0")"; pwd)
cd $THISDIR/..

initialse() {
    source venv/bin/activate
}

help() {
    sed -n '/^###/p' "$0"
}

### --install : install requirements in venv
install() {
    virtualenv venv --python=python3.8
    initialse
    pip install -r requirements.txt
}

### --start-dev : start dev server
start() {
    initialse
    python src/manage.py runserver
}

### --test <APPNAME> : Run unit test cases for respective app
test() {
    initialse
    python src/manage.py test $1
}

### --lint - lint code
lint() {
    isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=100 src/ app.py config.py -y
    black --line-length=100 src/ config.py
}

### --migrate : migrate db changes
migrate() {
    initialse
    python src/manage.py migrate $1
    python src/manage.py makemigrations $1
    python src/manage.py migrate $1
}


case $1 in
    --start-dev)
        start
    ;;
    --install)
        install
    ;;

    --test)
        test "$2"
    ;;

    --migrate)
        migrate
    ;;


    --lint)
        lint
    ;;

  *)
    printf "\nAvailable Commands :\n\n"
    help
    exit 0
    ;;
esac