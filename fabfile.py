from fabric.api import local, cd, run, env, get
import config

env.hosts = ["production"]


def deploy():
    local("git push")
    with cd("~/temphumi"):
        run("git pull")
        run("pipenv install")


def get_data():
    get(f"~/temphumi/{config.CSV_FILE}", config.CSV_FILE)
