"""bower tests
"""

import pytest


class TestBowerTest:

    def test_finalize_options_no_command(self):
        """ bower command not found """
        from setuptools.dist import Distribution
        dist = Distribution(
            dict(name='foo',
                 packages=['foo'],
                 use_2to3=True,
                 version='0.0',
                 ))
        dist.script_name = 'setup.py'
        from build_commands import BowerCommand
        cmd = BowerCommand(dist)
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
        from build_commands import BowerCommand
        cmd = BowerCommand(dist)
        from distutils.errors import DistutilsArgError
        import mock
        with mock.patch('build_commands.bower.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/bower'
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
        from build_commands import BowerCommand
        cmd = BowerCommand(dist)
        import tempfile
        cmd.instance_dir = tempfile.mkdtemp()
        import mock
        with mock.patch('build_commands.bower.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/bower'
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
        from build_commands import BowerCommand
        cmd = BowerCommand(dist)
        import tempfile
        cmd.instance_dir = tempfile.mkdtemp()
        import mock
        with mock.patch('build_commands.bower.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/bower'
            cmd.ensure_finalized()

        spawn_mock = mock.MagicMock()
        cmd.spawn = spawn_mock
        import sys
        old_stdout = sys.stdout
        try:
            cmd.run()
        finally:
            sys.stdout = old_stdout

        expected = ['bower', 'install', cmd.instance_dir]
        spawn_mock.assert_called_once_with(expected)

    def test_run_ok_production(self):
        """ Assert spawn is called with the right parameters """
        from setuptools.dist import Distribution
        dist = Distribution(
            dict(name='foo',
                 packages=['foo'],
                 use_2to3=True,
                 version='0.0',
                 ))
        dist.script_name = 'setup.py'
        from build_commands import BowerCommand
        cmd = BowerCommand(dist)
        import tempfile
        cmd.instance_dir = tempfile.mkdtemp()
        import mock
        with mock.patch('build_commands.bower.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/bower'
            cmd.ensure_finalized()

        spawn_mock = mock.MagicMock()
        cmd.spawn = spawn_mock
        cmd.production = True
        import sys
        old_stdout = sys.stdout
        try:
            cmd.run()
        finally:
            sys.stdout = old_stdout

        expected = ['bower', 'install', cmd.instance_dir, '-p']
        spawn_mock.assert_called_once_with(expected)
