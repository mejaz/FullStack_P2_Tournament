Tournament Results - Swiss Pairing Version 1.0 07/26/2015

Introduction:
-------------
This program can be used to determine a winner of a game played by even number of contestants.
It has the features to register a player, determine player standings, to pair the winnners and losers
for the next round and finally determine the tournament winner.



Python Librarie(s) required:
----------------------------
psycopg2 python library is used to connect to the Postgresql DB.



Database:
---------
1. The name of the database : tournament
2. Import the SQL file to psql using the command : \i tournament.sql
3. Connect the tournament DB using the command : \c tournament.sql
4. Check for the tournament DB if it already exist, Drop and recreate one : DROP DATABASE IF EXISTS tournament;
5. Create a new DB : CREATE DATABASE tournament;



Steps to run the test file:
-------------------------------
1. Navigate to the tournament directory path : /vagrant/tournament
2. Following files should be present in this directory : tournament.py , tournament.sql, tournament_test.py
3. To run the test file, run the command in the Unix command line : python tournament_test.py




Contact Us:
Email : mohdejazsiddiqui@gmail.com