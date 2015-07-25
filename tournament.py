#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(db_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(db_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Connection failed.")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    cursor.execute("DELETE FROM match_results;")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    cursor.execute("DELETE FROM players;")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    cursor.execute("SELECT Count(player_name) FROM players;")
    noOfPlayers = cursor.fetchall()
    db.close()
    return noOfPlayers[0][0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()
    cursor.execute("INSERT INTO players (player_name) VALUES (%s);", (name,))
    cursor.execute("INSERT INTO match_results (player_id, player_name, wins, matches) SELECT player_id, player_name, 0, 0 FROM players Order By player_id DESC Limit 1;")
    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    cursor.execute("SELECT * FROM match_results ORDER By wins DESC;")
    finList = cursor.fetchall()
    db.close()
    return finList

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()
    cursor.execute("Update match_results set wins = wins + 1, matches = matches + 1 where player_id = %s;", (winner,))
    cursor.execute("Update match_results set wins = wins + 0, matches = matches + 1 where player_id = %s;", (loser,))
    db.commit()
    db.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db, cursor = connect()

    cursor.execute("SELECT player_id, player_name FROM match_results ORDER By wins DESC;")
    finList = cursor.fetchall()
    list1 = []
    for i in xrange(0, (len(finList) - 1), 2):
        list1.append((finList[i][0], finList[i][1], finList[i+1][0], finList[i+1][1]))
    db.close()
    return list1