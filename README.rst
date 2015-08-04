build_commands
==============

This package provides common setuptools command utilities if you
need to initialize your package with ``npm``, ``bower``
or ``gulp`` commands.

Usage
-----

You are supposed to create in your own package a ``Yeoman`` like
project folder (for example: ``your_package/templates``).

Add the ``build_commands`` dependency to your pretend ``your_package``.

Update your ``setup.cfg`` adding the following::

    [aliases]
    npm = npm -i your_package/templates
    bower = bower -i your_package/templates
    gulp = gulp -i your_package/templates -g gulpfile.babel.js

This way once installed your ``your_package`` you can initialize your
Yeoman project with::

    $ python setup.py install/develop
    $ python setup.py npm
    $ python setup.py bower
    $ python setup.py gulp

And all your frontend stuff will be processed automatically (SASS, minification,
uglyfication, etc).

A big ``TODO``:

* provide tests

Authors
=======

* Davide Moro <https://twitter.com/davidemoro>
