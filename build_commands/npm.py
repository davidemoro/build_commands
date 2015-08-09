import os
from distutils.errors import DistutilsArgError
from distutils.spawn import find_executable
from distutils.log import INFO
from setuptools import Command


class NpmCommand(Command):
    """ Run npm install command """

    description = 'run npm install command'
    user_options = [
        ('executable=', 'e', 'executable path'),
        ('instance-dir=', 'i', 'instance dir of the project'),
    ]

    def initialize_options(self):
        self.executable = 'npm'
        self.instance_dir = None
  
    def finalize_options(self):
        command = find_executable(self.executable)
        if not command:
            raise DistutilsArgError(
                "{0} not found. You must specify --executable or -e"
                " with the npm instance_dir".format(self.executable)
                )
        if self.instance_dir is None or not os.path.isdir(self.instance_dir):
            raise DistutilsArgError(
                "project dir {0} not found."
                " You must specify --instance_dir or -p"
                " with the project instance_dir".format(self.instance_dir)
                )
  
    def run(self):
        command = '{0} install --prefix {1} {1}'.format(
            self.executable,
            self.instance_dir,
            )
        self.announce(
            'Running command: {0}'.format(command),
            level=INFO)
        self.spawn(command.split(' '))
