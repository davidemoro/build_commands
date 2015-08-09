import os
from distutils.errors import DistutilsArgError
from distutils.spawn import find_executable
from distutils.log import INFO
from setuptools import Command


class BowerCommand(Command):
    """ Run bower install command """

    description = 'run bower install command'
    user_options = [
        ('executable=', 'e', 'executable path'),
        ('instance-dir=', 'i', 'instance dir of the project'),
        ('production=', 'p', 'production mode'),
    ]

    def initialize_options(self):
        self.executable = 'bower'
        self.production = False
        self.instance_dir = None
  
    def finalize_options(self):
        executable = find_executable(self.executable)
        if not executable:
            raise DistutilsArgError(
                "{0} not found. You must specify --executable or -e"
                " with the bower path".format(self.executable)
                )
        if self.instance_dir and not os.path.isdir(self.instance_dir):
            raise DistutilsArgError(
                "project dir {0} not found."
                " You must specify --instance_dir or -p"
                " with the project instance_dir".format(self.instance_dir)
                )
  
    def run(self):
        command = '{0} install'.format(self.executable)
        if self.instance_dir:
            command = '{0} {1}'.format(command, self.instance_dir)
        if self.production:
            command = '{0} -p'.format(command)
        self.announce(
            'Running command: {0}'.format(command),
            level=INFO)
        self.spawn(command.split(' '))
