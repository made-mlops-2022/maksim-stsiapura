from setuptools import find_packages, setup


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(name="src",
      packages=find_packages(),
      version="1.0.0",
      description="Production ready project",
      author="maxima1ist",
      install_requires=required)
