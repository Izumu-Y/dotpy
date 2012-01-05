DEVELOPMENT
===========

* Local Development Setup

    Check [[Local Development Setup Steps]] for details.

* Generating testing data (fixture)

    `django dumpdata --indent=2 -e contenttypes -e auth.permission -e sites > common/fixtures/testing_data.json`

    (`django` here means `python manage.py`, same below)

* Loading testing data (fixture)

    `django loaddata testing_data`


