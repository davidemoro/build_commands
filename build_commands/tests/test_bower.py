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
            cmd.finalize_options()

    def test_finalize_options_no_instance_dir_fail(self):
        """ instance_dir provided not found """
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
        cmd.instance_dir = 'notfound'
        import mock
        with mock.patch('build_commands.bower.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/bower'
            from distutils.errors import DistutilsArgError
            with pytest.raises(DistutilsArgError):
                cmd.finalize_options()

    def test_finalize_options_no_instance_dir(self):
        """ instance_dir not found (not mandatory) """
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
        import mock
        with mock.patch('build_commands.bower.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/bower'
            cmd.finalize_options()

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
        from build_commands import BowerCommand
        cmd = BowerCommand(dist)
        import tempfile
        cmd.instance_dir = tempfile.mkdtemp()
        import mock
        with mock.patch('build_commands.bower.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/bower'
            cmd.finalize_options()

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

    def test_run_ok_no_instance_dir(self):
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
        import mock
        with mock.patch('build_commands.bower.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/bower'
            cmd.finalize_options()

        spawn_mock = mock.MagicMock()
        cmd.spawn = spawn_mock
        import sys
        old_stdout = sys.stdout
        try:
            cmd.run()
        finally:
            sys.stdout = old_stdout

        expected = ['bower', 'install']
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
            cmd.finalize_options()

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

    def test_run_ok_production_no_instance_dir(self):
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
        import mock
        with mock.patch('build_commands.bower.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/bower'
            cmd.finalize_options()

        spawn_mock = mock.MagicMock()
        cmd.spawn = spawn_mock
        cmd.production = True
        import sys
        old_stdout = sys.stdout
        try:
            cmd.run()
        finally:
            sys.stdout = old_stdout

        expected = ['bower', 'install', '-p']
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
        from build_commands import BowerCommand
        cmd = BowerCommand(dist)
        cmd.executable = '/tmp/bower'
        import tempfile
        import mock
        with mock.patch('build_commands.bower.find_executable') \
                as find_executable:
            find_executable.return_value = '/tmp/bower'
            cmd.finalize_options()

        spawn_mock = mock.MagicMock()
        cmd.spawn = spawn_mock
        cmd.production = True
        import sys
        old_stdout = sys.stdout
        try:
            cmd.run()
        finally:
            sys.stdout = old_stdout

        expected = ['/tmp/bower', 'install', '-p']
        spawn_mock.assert_called_once_with(expected)
