#!/bin/bash

echo ----------------------------- Unit Tests -----------------------------
coverage run --source=firstapp manage.py test firstapp.tests.test_ut
echo ------------------------- Integration Tests --------------------------
coverage run --source=firstapp manage.py test firstapp.tests.test_it
