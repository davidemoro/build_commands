"""gulp tests
"""

import pytest


class TestGulpTest:

    def test_finalize_options_no_command(self):
        """ gulp command not found """
        from setuptools.dist import Distribution
        dist = Distribution(
            dict(name='foo',
                 packages=['foo'],
                 use_2to3=True,
                 version='0.0',
                 ))
        dist.script_name = 'setup.py'
        from build_commands import GulpCommand
        cmd = GulpCommand(dist)
        from distutils.errors import DistutilsArgError
        with pytest.raises(DistutilsArgError):
            cmd.finalize_options()

    def test_finalize_options_no_instance_dir(self):
        """ instance_dir not found """
        from setuptools.dist import Distribution
        dist = Distribution(
            dict(name='foo',
                 packages=['foo'],
                 use_2to3=True,
                 version='0.0',
                 ))
        dist.script_name = 'setup.py'
        from build_commands import GulpCommand
        cmd = GulpCommand(dist)
        from distutils.errors import DistutilsArgError
        import mock
        with mock.patch('build_commands.gulp.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/gulp'
            with pytest.raises(DistutilsArgError):
                cmd.finalize_options()

    def test_finalize_options_no_gulpfile(self):
        """ no gulpfile """
        from setuptools.dist import Distribution
        dist = Distribution(
            dict(name='foo',
                 packages=['foo'],
                 use_2to3=True,
                 version='0.0',
                 ))
        dist.script_name = 'setup.py'
        from build_commands import GulpCommand
        cmd = GulpCommand(dist)
        import tempfile
        cmd.instance_dir = tempfile.mkdtemp()
        from distutils.errors import DistutilsArgError
        import mock
        with mock.patch('build_commands.gulp.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/gulp'
            with pytest.raises(DistutilsArgError):
                cmd.finalize_options()

    def test_finalize_options_notfound_gulpfile(self):
        """ gulpfile not found """
        from setuptools.dist import Distribution
        dist = Distribution(
            dict(name='foo',
                 packages=['foo'],
                 use_2to3=True,
                 version='0.0',
                 ))
        dist.script_name = 'setup.py'
        from build_commands import GulpCommand
        cmd = GulpCommand(dist)
        import tempfile
        cmd.instance_dir = tempfile.mkdtemp()
        cmd.gulpfile = 'notfoundfile'
        from distutils.errors import DistutilsArgError
        import mock
        with mock.patch('build_commands.gulp.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/gulp'
            with pytest.raises(DistutilsArgError):
                cmd.finalize_options()

    def test_finalize_options_ok(self):
        """ finalize options ok """
        from setuptools.dist import Distribution
        dist = Distribution(
            dict(name='foo',
                 packages=['foo'],
                 use_2to3=True,
                 version='0.0',
                 ))
        dist.script_name = 'setup.py'
        from build_commands import GulpCommand
        cmd = GulpCommand(dist)
        import tempfile
        cmd.instance_dir = tempfile.mkdtemp()
        gulpfile = tempfile.mkstemp(dir=cmd.instance_dir)[1]
        import os
        cmd.gulpfile = os.path.basename(gulpfile)
        import mock
        with mock.patch('build_commands.gulp.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/gulp'
            cmd.finalize_options()

    def test_run_ok(self):
        """ Assert spawn is called with the right parameters """
        from setuptools.dist import Distribution
        dist = Distribution(
            dict(name='foo',
                 packages=['foo'],
                 use_2to3=True,
                 version='0.0',
                 ))
        dist.script_name = 'setup.py'
        from build_commands import GulpCommand
        cmd = GulpCommand(dist)
        import tempfile
        cmd.instance_dir = tempfile.mkdtemp()
        gulpfile = tempfile.mkstemp(dir=cmd.instance_dir)[1]
        import os
        cmd.gulpfile = os.path.basename(gulpfile)
        import mock
        with mock.patch('build_commands.gulp.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/gulp'
            cmd.finalize_options()

        spawn_mock = mock.MagicMock()
        cmd.spawn = spawn_mock
        import sys
        old_stdout = sys.stdout
        try:
            cmd.run()
        finally:
            sys.stdout = old_stdout

        expected = ['gulp', 'build', '--base', cmd.instance_dir, '--gulpfile', gulpfile]
        spawn_mock.assert_called_once_with(expected)

    def test_run_ok_custom_executable(self):
        """ Assert spawn is called with the right parameters """
        from setuptools.dist import Distribution
        dist = Distribution(
            dict(name='foo',
                 packages=['foo'],
                 use_2to3=True,
                 version='0.0',
                 ))
        dist.script_name = 'setup.py'
        from build_commands import GulpCommand
        cmd = GulpCommand(dist)
        import tempfile
        cmd.instance_dir = tempfile.mkdtemp()
        gulpfile = tempfile.mkstemp(dir=cmd.instance_dir)[1]
        import os
        cmd.gulpfile = os.path.basename(gulpfile)
        cmd.executable = '/tmp/gulp'
        import mock
        with mock.patch('build_commands.gulp.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/gulp'
            cmd.finalize_options()

        spawn_mock = mock.MagicMock()
        cmd.spawn = spawn_mock
        import sys
        old_stdout = sys.stdout
        try:
            cmd.run()
        finally:
            sys.stdout = old_stdout

        expected = ['/tmp/gulp', 'build', '--base', cmd.instance_dir, '--gulpfile', gulpfile]
        spawn_mock.assert_called_once_with(expected)
