Data Project
************

Requirements
************

* Python 3.6
* Flask 1.1.2
* Pandas 0.22.0

Installation on Linux-Ubuntu 18.04
**********************************

First we will create a virtual environment to isolate resources using virtualenv.
To use the virtual environment install virtualenv, as a requirement you must have pip installed.

Setting the enviroment
======================

Installing Pip
--------------

   sudo apt-get install python3-pip

Installing virtualenv
---------------------

   python3 -m pip install virtualenv

Create and activate the virtual enviroment
------------------------------------------

   virtualenv sw-env -p python3
   source sw-env/bin/activate

Starting the project
====================

Installing Project's requirements
---------------------------------
Within the root of the star_wars project run:

   pip3 install -r requirements.txt

Running Server
--------------

   $ python -m flask run

Structure (Endpoints)
=====================

=============================  ===========  ===========  =============================
Endpoint                       HTTP Method  CRUD Method  Result
=============================  ===========  ===========  =============================
/countries_by?
indicator=$indicator
&index_value=$index_value         GET          Read      return countries
                                                         with their index value,
                                                         greater than the input value,
                                                         using only life satisfaction
                                                         index and total inequality
=============================  ===========  ===========  =============================

Tests
*****
Running tests
=============

In order to run the tests you have run

   python tests.py
