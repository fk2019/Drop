#!/usr/bin/bash
# refresh db

cat dropdb.sql | mysql -uroot;
cat getdb.sql | mysql -uroot;
