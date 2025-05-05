from setuptools import setup
import py2exe

setup(
    name="Git Helper",
    version="1.0",
    description="Simple Git helper to add, commit and push",
    author="User",
    console=[{"script": "git_helper.py"}],
    options={"py2exe": {"bundle_files": 1, "compressed": True}},
    zipfile=None,
) 