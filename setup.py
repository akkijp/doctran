from setuptools import setup, find_packages

def requirements_from_file(file_name):
    return open(file_name).read().splitlines()

setup(
  name="doctran",
  version="1.0.0",  # Set the version appropriately
  description="doctran",
  long_description="doctran",
  packages=find_packages(),
  install_requires=requirements_from_file('requirements.txt'),
)
