# -*- coding: utf-8 -*-

from __future__ import print_function

print("""
Congratulations!
You have now taken the first step in creating your new AiiDAlab App:

    {{cookiecutter.app_title}}

### NEXT STEPS ###

1. Open your new AiiDAlab App folder

    cd {{cookiecutter.repo_name}}

2. Enable version control

    git init

3. Enable code sanity checks on every commit (recommended)

    pip install -U pre-commit
    pre-commit install

4. Register your app NOW by making a pull request to the AiiDAlab App Registry
on https://github.com/aiidalab/aiidalab-registry

See this link also for a full list of recognized metadata keys for the setup.cfg file.
""")
