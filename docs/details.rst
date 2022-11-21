Packaging (`setup.cfg`)
-----------------------

The :ref:`setup.cfg` allows for easy packaging and installation::

  $ python -m pip install git+https://gitlab.in2p3.fr/constance.ganot/mastermind.git

or through the complete cloning of the gitlab repository::

  $ git clone https://gitlab.in2p3.fr/constance.ganot/mastermind  # cloning
  $ cd mastermind
  $ pip install .                                  # local installation

Package initialization (`__init__.py`)
--------------------------------------

The `__init__.py` file in each package directory describes the
initialization of the package, i.e. the actions (usually imports, but
also definitions, etc.) to be performed at package import.

.. code-block:: python

   >>> import mastermind  # Will run mastermind/__init__.py and all subsequent initializations
   Initialization top-level module

Main entries (`__main__.py`)
----------------------------

The *main* program can be called in different ways:

* as the :ref:`__main__.py <main.py>` entry of a module, e.g.::

    $ python -m mastermind     # Execute top-level pyyc/__main__.py
    Initialization top-level module
    ---------------------- MAIN ----------------------

  There can be only *one* package main, corresponding to the `if
  __name == "__main__"` part of the `__main__.py` file.


* as console scripts defined as *entry points* in :ref:`setup.cfg`:

  .. literalinclude:: ../setup.cfg
     :language: cfg

Documentation
-------------

The sample code is documented using the documentation generator `sphinx`
within the dedicated directory `docs/`, typically for a first use::

  [docs/]$ sphinx-quickstart  # initiate the documentation tool
  [docs/]$ # edit 'conf.py' to your needs (see below)
  [docs/]$ sphinx-apidoc -o . ../pyyc  # automatic generation of documentation files
  Creating file ./mastermind.rst.
  [docs/]$ # include these documentation files in 'index.rst' (see below)
  [docs/]$ make html          # build the documentation as a website
  [docs/]$ firefox _build/html/index.html

`conf.py`
.........

In particular, the use of the auto-documentation extension `sphinx.ext.autodoc`
requires few non-trivial lines in :ref:`conf.py`:

* set-up the path to code sources for extraction of docstrings:

  .. literalinclude:: conf.py
     :language: python

* add `sphinx.ext.autodoc` in the list of sphinx extensions `extensions =
  [...]`
* configure the `autodoc` extension:

  .. literalinclude:: conf.py
     :language: python
     :start-at: Autodoc configuration
     :end-at: autodoc_member_order

`index.rst`
...........

The `index.rst` file is the top-level documentation file, which will include
links to all the other documentation `.rst` files under the specific
`.. toctree::` command, e.g.:

.. code-block:: rest

   .. toctree::
      :caption: Code documentation
      :titlesonly:

      mastermind

`setup.cfg`
...........

The packaging configuration of the documentation is controlled by
dedicated sections in :ref:`setup.cfg`:

.. literalinclude:: ../setup.cfg
   :language: cfg

This adds a new command in the `setup.py`::

  $ python setup.py build_sphinx

Testing
-------

.. Warning:: With the current configuration :ref:`setup.cfg` (considered
   deprecated for tests), it is not possible to run the tests directly from
   `setup.py`. It is therefore necessary to run the tests manually.



Dedicated tests
...............

Tests gathered in the `tests/` directory shall be performed using
`pytest`, e.g.::

  [tests/]$ pytest -v test_game.py

`pytest` will actually auto-discover all the tests from top-level directory::

  $ pytest

Test coverage
.............

`coverage` will run the test suite and look for parts of the code which
have been (and more importantly *not been*) tested.

::

  $ coverage run -m pytest
  $ coverage report
  Name                     Stmts   Miss  Cover
  --------------------------------------------
  mastermind/__init__.py       5      0   100%
  mastermind/__main__.py      19      1    95%
  mastermind/game.py          51      0   100%
  tests/__init__.py            0      0   100%
  tests/test_game.py          75      0   100%
  --------------------------------------------
  TOTAL                      150      1    99%

To visualize which parts of the code is documented or not::

  $ coverage html
  Wrote HTML report to htmlcov/index.html
  $ firefox htmlcov/index.html




