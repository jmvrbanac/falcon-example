Example Falcon Service
=======================

This project is an example of a full fledged Falcon API service.
The intended purpose is to show one of the many ways people can build services
with the following features:

* Input Validation
* Simple ORM usage
* Testing
* CLI entrypoint
* Middleware
* Custom Gunicorn Workers

Installation
------------

From the cloned source, execute:

.. code-block:: shell

    pip install -e .

Running
-------

Once installed you can run the service using the ``falcon-example`` command.

.. note::

    The service connects to a MySQL database. You'll need to edit the service
    config in ``etc/example/config.yml`` to match your configuration.
  
You can also use the Docker Compose setup:

.. code-block:: shell

    docker-compose run --service-ports 8000:8000 app bash
    pip install -e .
    falcon-example

Running Tests
-------------

Install test requirements

.. code-block:: shell

    pip install -r dev-requirements.txt

Execute the tests by running the ``tox`` command:
