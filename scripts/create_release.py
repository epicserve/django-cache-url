#!/usr/bin/env python

import argparse
import os
import re
import time
from pathlib import Path

VERSION_PATTERN = r'[\d]+\.[\d]+\.[\d]+'


def get_args():
    parser = argparse.ArgumentParser(description='Create a new release.')
    parser.add_argument('version', nargs='?', help='The release version.')
    parser.add_argument('--push', action='store_true', help="Push changes to origin.")
    parser.add_argument('--publish', action='store_true', help="Publish changes to Pypi.")
    return parser.parse_args()


def update_version(version):
    with open('setup.py', 'r+') as f:
        out = f.read()
        out = re.sub(f"version='{VERSION_PATTERN}'", f"version='{version}'", out)
        f.seek(0)
        f.write(out)


def commit_and_tag(version):
    os.popen('git add setup.py')
    os.popen(f'git commit -m "Bump version to {version}"')
    # without sleep it tags the previous commit
    time.sleep(2)
    os.popen(f'git tag -a -m "" v{version}')


def push():
    print(os.popen('git push --tags origin master').read())


def build():
    print(os.popen('rm -rf build dist').read())
    print(os.popen('python setup.py sdist bdist_wheel').read())


def publish():
    print(os.popen('twine upload dist/*').read())


if __name__ == "__main__":
    """
    TODO: This script needs fixed. You can run it, but you'll have to commit manually
    and push the tag and commit.
    
    Then you can run the following:
    
    # Install requirements
    python -m pip install build twine
    
    # Build
    python -m build
    
    # Check build
    twine check dist/*
    
    # Test upload
    twine upload -r testpypi dist/*
    
    # Upload
    twine upload dist/*
    """

    # change working directory so you can run this script from the project root or in the same directory as the file.
    parent_dir = Path(os.path.realpath(os.path.dirname(__file__))).parent
    os.chdir(parent_dir)
    args = get_args()
    new_version = args.version
    current_version = os.popen('git tag | tail -1').read()[1:].strip()
    while new_version is None or re.match(VERSION_PATTERN, new_version) is None:
        new_version = input(f'What version would you like for this release (current version: {current_version})? ')

    update_version(new_version)

    commit_and_tag(new_version)

    if args.push is True:
        push()

    build()

    if args.publish is True:
        publish()
