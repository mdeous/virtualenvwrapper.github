# -*- coding: utf-8 -*-
#
# Copyright (c) 2010 MatToufoutu
#
"""
virtualenvwrapper.project plugin for github repositories
"""

import os

from git import *
from github2.client import Github

def get_environment():
    """
    Get required environment variables.
    """
    env_is_ok = True
    github_user = os.environ.get('GITHUB_USER')
    if github_user is None:
        print 'GITHUB_USER not found'
        print 'Add \'export GITHUB_USER="username"\' to your .bashrc'
        env_is_ok = False
    api_token = os.environ.get('GITHUB_API_TOKEN')
    if api_token is None:
        print 'GITHUB_API_TOKEN not found'
        print 'Add \'export GITHUB_API_TOKEN"=api_token"\' to your .bashrc'
        env_is_ok = False
    if not env_is_ok:
        return None
    return (github_user, api_token)

def template(args):
    """
    Creates a GitHub repository into the project directory,
    if the GitHub project still exists, clone the repository
    """
    prj_name = args[0]
    print 'Initializing git repository and creating GitHub project for %s' % prj_name
    src_dir = os.path.join(os.getcwd(), 'src')
    env_vars = get_environment()
    if env_vars is None:
        print 'Repository was not created'
        return
    username, api_token = env_vars
    git_url = 'git@github.com:%s/%s.git' % (username, prj_name)
    github = Github(username, api_token)
    try:
        github.repos.show("%s/%s" % (username, prj_name))
        repo_exists = True
    except RuntimeError:
        repo_exists = False
    if repo_exists:
        print 'Repository already exists on GitHub'
        print '[C]lone or [A]bort? ',
        choice = raw_input().lower()
        if choice == 'c':
            print 'Cloning repository from %s' % git_url
            try:
                # delete src folder to prevent error when cloning (will be created by the clone command)
                if os.path.exists(src_dir):
                    os.rmdir(src_dir)
                Repo.clone_from(git_url, src_dir)
                repo_created = True
            except GitCommandError:
                print 'An error occured while cloning the repository'
                if os.path.exists(os.path.join(src_dir, '.git')):
                    os.rmdir(os.path.join(src_dir, '.git'))
                repo_created = False
        else:
            repo_created = False
    else:
        prj_desc = raw_input('Project description (default=None): ')
        prj_url = raw_input('Project homepage (default=None): ')
        github.repos.create(
                name = prj_name,
                description = prj_desc if (prj_desc != '') else None,
                homepage = prj_url if (prj_url != '') else None,
        )
        repo = Repo.init(src_dir)
        repo.create_remote('origin', git_url)
        repo_created = True
    if repo_created:
        print 'Repository was successfuly created'
    else:
        print 'Repository was not created'
    return
