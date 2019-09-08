#__author__ = Mohammad Abdin

import sqlite3
import time
import datetime
import random


# define connection and cursor
conn = sqlite3.connect('chinook.db')
c = conn.cursor()


# def create_table():
#     c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

#inputting data into the DB
def add_track():

    c.execute("INSERT INTO tracks (TrackId, Name, AlbumId, MediaTypeId, GenreID, Composer, Milliseconds, Bytes, UnitPrice) VALUES (?, ?, ?, ?, ? , ? , ? , ? , ?)",
              (input("TrackId: "),input("Name: "),input("AlbumId: "),input("MediaTypeId: "),input("GenreID: "),input("Composer: ")
              ,input("Milliseconds: "),input("Bytes: "),input("UnitPrice: ")))
    # save: anytime u modify anything in your DB, U need to conduct commit.
    conn.commit()

#Get a playlist - prints an existing playlist to the user.
def get_playlists():
    c.execute("SELECT DISTINCT Name FROM tracks LEFT JOIN  (\
                SELECT TrackId FROM playlist_track join playlists on playlist_track.PlaylistId = playlists.PlaylistId) as tmp")
    conn.commit()

    rows = c.fetchall()
    for row in rows:
        row = "".join(row)
        print(row)


def create_playlist():

    #Create a playlist - creates a new playlist in the DB.
    c.execute("INSERT INTO playlists (PlaylistId, Name) VALUES (?, ?)", (input("PlaylistId: "), input("Name: ")))
    # save: anytime u modify anything in your DB, U need to conduct commit.
    conn.commit()

#Add a song to a playlist - adds a song to an existing playlist.
def add_song_to_playlist():
    playlist_id = int(input("enter the playlist id: "))
    c.execute("INSERT INTO playlist_track (PlaylistId, TrackId) VALUES (?, ?)",(playlist_id, input("TrackId: ")))
    conn.commit()


def add_employee():
    c.execute( "INSERT INTO employees (EmployeeId, LastName, FirstName, Title, ReportsTo, "
                                      "BirthDate , HireDate, Address , City ,  State,"
                                      " Country,  PostalCode, Phone, Fax  , Email) \
                VALUES (?, ?, ?, ?, ?, ? , ? , ? , ? , ? , ? , ? , ? , ? , ? )",
        (input("EmployeeId: "), input("LastName: "), input("FirstName: "), input("Title: "), input("ReportsTo: "),
         input("BirthDate: ") , input("HireDate: "),input("Address: "), input("City: "), input("State: ") , input("Country: "), input("PostalCode: "), input("Phone: "),input("Fax: "),input("Email: ")))

    # save: anytime u modify anything in your DB, U need to conduct commit.
    conn.commit()

def delete_employee():
    c.execute("DELETE FROM employees  WHERE EmployeeId = ? AND LastName = ? AND FirstName = ?",
                                (input("EmployeeId: "), input("LastName: "), input("FirstName: ")))

    # save: anytime u modify anything in your DB, U need to conduct commit.
    conn.commit()
def close():
    # when U are completely done with the DB -> close
    # close the cursor
    c.close()
    # close the conduct
    conn.close()


#create_table()
#add_track()
#get_playlists()
#create_playlist()
#add_song_to_playlist()
#add_employee()
delete_employee()

#conn.execute("PRAGMA busy_timeout = 30000")



close()