#!/usr/bin/env python3
import os
import pygit2 as git2

def main():
    cwd = os.getcwd()
    repo = git2.init_repository(cwd)


def find_file_creation(repo, path):
    result = repo.ahead_behind()


if __name__ == '__main__':
    main()
