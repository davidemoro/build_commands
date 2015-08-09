import os
from distutils.errors import DistutilsArgError
from distutils.spawn import find_executable
from distutils.log import INFO
from setuptools import Command


class GulpCommand(Command):
    """ Run gulp build command """

    description = 'run gulp build command'
    user_options = [
        ('executable=', 'e', 'executable path'),
        ('instance-dir=', 'i', 'instance dir of the project'),
        ('gulpfile=', 'g', 'name of the gulpfile'),
    ]

    def initialize_options(self):
        self.executable = 'gulp'
        self.instance_dir = None
        self.gulpfile = None
        self.gulpfile_path = None
  
    def finalize_options(self):
        executable = find_executable(self.executable)
        if not executable:
            raise DistutilsArgError(
                "{0} not found. You must specify --executable or -e"
                " with the gulp path".format(self.executable)
                )
        if self.instance_dir is None or not os.path.isdir(self.instance_dir):
            raise DistutilsArgError(
                "project dir {0} not found."
                " You must specify --instance_dir or -p"
                " with the project instance_dir".format(self.instance_dir)
                )
        if self.gulpfile is None:
            raise DistutilsArgError(
                "gulpfile {0} not provided."
                " You must specify --gulpfile or -g"
                " with the gulpfile name".format(self.gulpfile_path)
                )
        else:
            self.gulpfile_path = os.path.join(self.instance_dir, self.gulpfile)
            if self.gulpfile_path is None or not os.path.isfile(self.gulpfile_path):
                raise DistutilsArgError(
                    "gulpfile {0} not found."
                    " You must specify --gulpfile or -g"
                    " with the gulpfile name".format(self.gulpfile_path)
                    )
  
    def run(self):
      command = '{0} build --base {1} --gulpfile {2}'.format(
          self.executable,
          self.instance_dir,
          self.gulpfile_path,
          )
      self.announce(
          'Running command: {0}'.format(command),
          level=INFO)
      self.spawn(command.split(' '))
