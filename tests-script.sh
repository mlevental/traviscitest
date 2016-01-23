#!/bin/bash

echo ----------------------------- Unit Tests -----------------------------
coverage run -p --source=. \
    --omit *test_*.py,*migrations*,*__init__.py,*apps.py,*admin.py,*wsgi.py,*settings.py,manage.py \
    manage.py test firstapp.tests.test_ut

echo ------------------------- Integration Tests --------------------------
coverage run -p --source=. \
    --omit *test_*.py,*migrations*,*__init__.py,*apps.py,*admin.py,*wsgi.py,*settings.py,manage.py \
    manage.py test firstapp.tests.test_it
    
echo ---------------------- Combine Coverage Reports ----------------------
coverage combine