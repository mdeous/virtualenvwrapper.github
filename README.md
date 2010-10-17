virtualenvwrapper.github
========================

virtualenvwrapper.github is a template for virtualenvwrapper.project (by Doug Hellmann).
It automaticaly creates a GitHub repository for the new project, initializes the local
repository and configures the remote origin.

Dependencies
------------

The following python packages need to be installed and can be downloaded from pypi:

* virtualenv
* virtualenvwrapper (>=2.0)
* virtualenvwrapper.project (>=1.0)
* github2
* gitpython

The following softwares need to be installed:

* git

Installation
------------

Download the latest project version, put yourself in the source directory, and as root, type:

    python setup.py install

Then, you need to set your GitHub username and api key, you can find your api key in your account
settings, under the administration tab.
Add these two lines to your .bashrc (or .zshrc or whatever your shell is)

    export GITHUB_USERNAME="username"
    export GITHUB_API_TOKEN="api_token"

Usage
-----

Just specify 'github' as a template to use when launching the mkproject command:

    mkproject -t github my_project_name

Enter your project description and homepage if needed, and you're good to go.
