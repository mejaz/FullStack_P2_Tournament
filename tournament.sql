-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- create table players
DROP TABLE IF EXISTS match_results CASCADE;
DROP TABLE IF EXISTS players CASCADE;
DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament

CREATE TABLE players (
	player_id serial PRIMARY KEY,
	player_name text
);

CREATE TABLE match_results (
	player_id serial REFERENCES players(player_id) ON DELETE CASCADE,
	player_name text,
	wins integer,
	matches integer
);
