#!/bin/bash

echo ----------------------------- Unit Tests -----------------------------
python manage.py test firstapp.tests.test_ut
echo ------------------------- Integration Tests --------------------------
python manage.py test firstapp.tests.test_it
echo ------------------------- Coverage --------------------------
coverage run --source=firstapp manage.py test firstapp
