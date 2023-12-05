"""Post-generate hook to be run after project generation."""

print(
    """
Congratulations!

You have now taken the first step in creating your new AiiDAlab App:

    {{cookiecutter.app_title}}

### NEXT STEPS ###

1. Open your new AiiDAlab App folder:

    cd {{cookiecutter.repo_name}}

2. Enable version control:

    git init

3. Enable code sanity checks on every commit (recommended):

    pip install -U pre-commit
    pre-commit install

4. Upload your app repository online, e.g., to GitHub (https://docs.github.com/en/get-started/quickstart/create-a-repo):

    git remote add origin https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}
    git push -u origin main

5. Register your app NOW by following the instructions here:

   https://aiidalab.readthedocs.io/en/latest/app_development/publish.html

6. Import your repository to readthedocs.org to automatically build and publish your documentation, with the following instructions:

    https://readthedocs.org/dashboard/import/ for the import of your repository.
    https://docs.readthedocs.io/en/stable/pull-requests.html for the configuration of pull request previews.

"""
)
