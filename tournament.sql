-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- create table players

CREATE TABLE players (
	player_id serial primary key,
	player_name text
);

CREATE TABLE match_results (
	id integer,
	player_name text,
	wins integer,
	matches integer
);