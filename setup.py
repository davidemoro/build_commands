import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()

requires = [
    ]

test_requires = [
    'pytest>=2.4.2',
    'pytest-cov',
    'pytest-pep8!=1.0.3',
    'mock',
    ]

setup(name='build_commands',
      version='0.0.1',
      description='build_commands',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        ],
      author='Davide Moro',
      author_email='davide.moro@gmail.com',
      url='https://github.com/davidemoro/build_commands',
      keywords='web python gulp npm bower yeoman',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="build_commands",
      entry_points="""\
      [distutils.commands]
      npm = build_commands.setuptools_commands:NpmCommand
      bower = build_commands.setuptools_commands:BowerCommand
      gulp = build_commands.setuptools_commands:GulpCommand
      """,
      extras_require={
          'test': test_requires,
          },
      )
