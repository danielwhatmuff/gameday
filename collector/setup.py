# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
import sys


def read_from_req(extra=None):
    f_name = "requirements.txt"

    if extra is not None:
        f_name = "requirements-%s.txt" % extra

    with open(f_name) as f:
        requirements = [line.strip() for line in f if line.strip()]

    return requirements


requires = read_from_req()
if sys.argv[1] == 'develop':
    requires += read_from_req("test")

version = "0.0.1"


setup(name="collector",
      version=version,
      description="The gameday collector",
      packages=find_packages(),
      install_requires=requires,
      setup_requires='',
      entry_points={
          'console_scripts': [
              #e.g. b'run = merritt:run',
          ],
          'gui_scripts': [
              # e.g. 'baz = my_package_gui.start_func',
          ]
      },
      test_suite='nose.collector',
      # initially include everything in source control in created packages
      include_package_data=True,
      # and put this particular data, local to a developer only, in the pkg_resources namespace
      #package_data={'credentials': ['*.txt']}, ??
      # but never distribute that stuff in an sdist or an egg
      #exclude_package_data={'credentials': ['*.txt', '*.*', '*']}, ??
)
