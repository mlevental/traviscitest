#!/bin/bash

echo ----------------------------- Unit Tests -----------------------------
coverage run -p --source=firstapp --omit *test_*.py manage.py test firstapp.tests.test_ut
echo ------------------------- Integration Tests --------------------------
coverage run -p --source=firstapp --omit *test_*.py manage.py test firstapp.tests.test_it
echo ---------------------- Combine Coverage Reports ----------------------
coverage combine