def test_import():
    import {{cookiecutter.repo_name | slugify(separator='_') }}  # noqa: F401
