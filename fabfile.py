from fabric.api import local, prefix, cd, run, env, get
import config

env.hosts = ["production"]


def deploy():
    local("git push")
    with prefix("source ~/.virtualenvs/temphumi/bin/activate"):
        with cd("~/temphumi"):
            run("git pull")
            run("pip install -r requirements.txt")


def get_data():
    get(f"~/temphumi/{config.CSV_FILE}", config.CSV_FILE)
