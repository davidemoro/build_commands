"""npm tests
"""

import pytest


class TestNpmTest:

    def test_finalize_options_no_command(self):
        """ npm command not found """
        from setuptools.dist import Distribution
        dist = Distribution(
            dict(name='foo',
                 packages=['foo'],
                 use_2to3=True,
                 version='0.0',
                 ))
        dist.script_name = 'setup.py'
        from build_commands import NpmCommand
        cmd = NpmCommand(dist)
        from distutils.errors import DistutilsArgError
        with pytest.raises(DistutilsArgError):
            cmd.ensure_finalized()

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
        from build_commands import NpmCommand
        cmd = NpmCommand(dist)
        from distutils.errors import DistutilsArgError
        import mock
        with mock.patch('build_commands.npm.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/npm'
            with pytest.raises(DistutilsArgError):
                cmd.ensure_finalized()

    def test_finalize_options_ok(self):
        """ instance_dir and command ok """
        from setuptools.dist import Distribution
        dist = Distribution(
            dict(name='foo',
                 packages=['foo'],
                 use_2to3=True,
                 version='0.0',
                 ))
        dist.script_name = 'setup.py'
        from build_commands import NpmCommand
        cmd = NpmCommand(dist)
        import tempfile
        cmd.instance_dir = tempfile.mkdtemp()
        import mock
        with mock.patch('build_commands.npm.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/npm'
            cmd.ensure_finalized()

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
        from build_commands import NpmCommand
        cmd = NpmCommand(dist)
        import tempfile
        cmd.instance_dir = tempfile.mkdtemp()
        import mock
        with mock.patch('build_commands.npm.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/npm'
            cmd.ensure_finalized()

        spawn_mock = mock.MagicMock()
        cmd.spawn = spawn_mock
        import sys
        old_stdout = sys.stdout
        try:
            cmd.run()
        finally:
            sys.stdout = old_stdout

        expected = ['npm', 'install', '--prefix', cmd.instance_dir, cmd.instance_dir]
        spawn_mock.assert_called_once_with(expected)
