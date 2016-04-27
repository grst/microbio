from distutils.core import setup
from setuptools import find_packages
setup(
  name = 'microbio',
  packages = find_packages(exclude=['docs','tests*','dist']), # this must be the same as the name above
  version = '0.1',
  description = 'A minimalist Bioinformatics framework',
  author = 'Gregor Sturm',
  author_email = 'gregor.sturm@cs.tum.edu',
  url = 'https://github.com/grst/microbio', # use the URL to the github repo
  keywords = ['bioinformatics', 'framework'], # arbitrary keywords
  license = 'MIT',
  classifiers = [],
)

