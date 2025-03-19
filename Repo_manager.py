import os, time; from pathlib import Path; from git import Repo
PROJECT_DIR = Path(__file__).parent


def main(*args):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Running git pull...')

    deployment_repo = Repo(PROJECT_DIR)
    deployment_repo.git.pull()

    print('Git pull complete.')
    time.sleep(5)
    exit("Finished")
