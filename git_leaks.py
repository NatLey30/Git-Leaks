import pandas as pd
from git import Repo
import re, signal, sys, time, pwn, pdb, os

def handler_signal(signal, frame):
    print('\n\n Out ..........\n')
    sys.exit(1)
signal.signal(signal.SIGINT, handler_signal)

def extract(url):
    repo = Repo(url)
    commits = list(repo.iter_commits())
    return commits

def transform(commits):
    coincidencias = []
    pattern = re.compile(r".{10}private[-.\s]keys.{10}", re.IGNORECASE)
    for commit in commits:
        coincide = pattern.finditer(commit.message)
        if coincide:
            coincidencias.append(coincide)
    return coincidencias

def load(coincidencias):
    for i in coincidencias:
        for j in i:
            print(j)

if __name__ == '__main__':
    DIR_REPO = "./skale/skale-manager"
    commits  = extract(DIR_REPO)
    coincidencias = transform(commits)
    load(coincidencias)