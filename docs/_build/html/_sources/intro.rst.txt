Install the package
-------------------

Install by cloning the gitlab repository::

  $ git clone https://gitlab.in2p3.fr/constance.ganot/mastermind  # cloning
  $ cd mastermind
  [mastermind/]$ pip install .                           # local installation

Test the installation
---------------------

To test the package from Python (preferentially not from top-level directory):

>>> import mastermind


Build the documentation
-----------------------

To build the documentation from documentation directory::

  [docs/]$ make html
  [docs/]$ firefox _build/html/index.html
  [docs/]$ make latexpdf
  [docs/]$ evince _build/latex/mastermind.pdf

Run the tests
-------------


To run the tests from top-level directory::

  $ pytest

To assess test coverage::

  $ coverage run -m pytest
  $ coverage report
  $ coverage html
  Wrote HTML report to htmlcov/index.html
  $ firefox htmlcov/index.html


