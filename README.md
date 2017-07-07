BeeKeeper
=========

Look after all the little worker bees.

Getting started
---------------

To deploy a new BeeKeeper instance, clone this repo, and then run::

    $ heroku create
    $ git push heroku master
    $ heroku addons:create heroku-postgresql:hobby-dev
    $ heroku addons:create heroku-redis:hobby-dev
    $ heroku scale worker=1
    $ heroku run ./manage.py migrate
    $ heroku run ./manage.py createsuperuser

Django
~~~~~~

Configure a `SECRET_KEY` for the Django instance

    >>> from django.core.management.utils import get_random_secret_key
    >>> get_random_secret_key()
    'qn219x$#ox1$+(m4hdzi-q+5g&o9^7)(x5l8^y51+rrcvs*o3-'

Then set a `SECRET_KEY` configuration variable in your Heroku instance, and
put::

    SECRET_KEY=<your key here>

in the .env file inthe project home directory.

Github
~~~~~~

Next, go to the repository you want to manage, go to Settings, then Webhooks,
and add a new webhook for
`https:<your app name>.herokuapp.com/github/notify>`. When prompted for a secret,
generate one::

    >>> from django.utils.crypto import get_random_string
    >>> get_random_string(50)
    'nuiVypAArY7lFDgMdyC5kwutDGQdDc6rXljuIcI5iBttpPebui'

Once the webhook has been created, create a `GITHUB_WEBHOOK_KEY` Heroku
configuration variable to this string, and put::

    GITHUB_WEBHOOK_KEY=<your key here>

in the .env file in the project home directory.

Then, generate a `personal access token
<https://help.github.com/articles/creating-a-personal-access-token-for-the-
command-line/>`__, create `GITHUB_USERNAME` and `GITHUB_ACCESS_TOKEN` Heroku
configuration variables with that value, and put::

    GITHUB_USERNAME=<your github username>
    GITHUB_ACCESS_TOKEN=<your token here>

in the .env file in the project home directory.

Sendgrid
~~~~~~~~

Sign up for a Sendgrid account, then get an API key. Create a
`SENDGRID_API_KEY` configuration value on Heroku, and put::

    SENDGRID_API_KEY=<your key here>

In the .env file in the project home directory.

Amazon AWS
~~~~~~~~~~

Log into (or sign up for) your Amazon AWS account, and obtain an access key
and secret access key. Create the `AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY` Heroku configuration variables, and put::

    AWS_ACCESS_KEY_ID=<your key here>
    AWS_SECRET_ACCESS_KEY=<your secret key here>

In the .env file in the project home directory.

Go to the ECS panel and create a EC2 cluster in an AWS region of your choice.
Create the `AWS_ECS_REGION_NAME` and `AWS_ECS_CLUSTER_NAME` Heroku
configuration variables, and put::

    AWS_ECS_REGION_NAME=<your region ID (e.g., us-west-2) here>
    AWS_ECS_CLUSTER_NAME=<your cluster name here>

In the .env file in the project home directory.


Docker
~~~~~~


pip install awscli
aws configure
aws ecr get-login --no-include-email --region us-west-2
    (run the resutl of this command)




