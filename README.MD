### Django-19 and python3.x starter project



#### Kurulum

    sudo apt-get install python-pip
    sudo pip install virtualenvwrapper

    add to ~/.bash_profile;
        export WORKON_HOME=~/Envs
        source /usr/local/bin/virtualenvwrapper.sh

    add to ~/.bashrc;
        export WORKON_HOME=$HOME/Envs
        export PROJECT_HOME=$HOME/Project
        source /usr/local/bin/virtualenvwrapper.sh

    source ~/.bash_profile
    mkdir -p $WORKON_HOME
    mkvirtualenv --python=python3 starter

    go to project folder
        setvirtualenvproject starter(for after; workon starter)

        sudo apt-get install -f $(grep -vE "^\s*#" requirements.apt  | tr "\n" " ")

        pip install -r requirements.txt

#### Install Postgresql

    sudo apt-get install postgresql
    (Optional) sudo apt-get install pgadmin3

    change default password;

        $ sudo -u postgres psql
        postgres=> alter user postgres password 'root';
        postgres=> create user yerusername createdb createuser password
        'somepass';
        postgres=> create database starter owner yerusername;
        postgres=> \q

#### Start

    go to project folder

    python manage.py migrate

    python manage.py runserver

