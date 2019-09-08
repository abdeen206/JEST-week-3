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

    print("please fill in the blanks to add a track :\n")
    #print("type r to return to menu \n")
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
    print("please fill in the blanks to create a playlist :\n")
    #Create a playlist - creates a new playlist in the DB.
    c.execute("INSERT INTO playlists (PlaylistId, Name) VALUES (?, ?)", (input("PlaylistId: "), input("Name: ")))
    # save: anytime u modify anything in your DB, U need to conduct commit.
    conn.commit()

#Add a song to a playlist - adds a song to an existing playlist.
def add_song_to_playlist():
    print("please fill in the blanks to add song to a playlist :\n")
    playlist_id = int(input("enter the playlist id: "))
    c.execute("INSERT INTO playlist_track (PlaylistId, TrackId) VALUES (?, ?)",(playlist_id, input("TrackId: ")))
    conn.commit()


def add_employee():
    print("please fill in the blanks to add an employee :\n")
    c.execute( "INSERT INTO employees (EmployeeId, LastName, FirstName, Title, ReportsTo, "
                                      "BirthDate , HireDate, Address , City ,  State,"
                                      " Country,  PostalCode, Phone, Fax  , Email) \
                VALUES (?, ?, ?, ?, ?, ? , ? , ? , ? , ? , ? , ? , ? , ? , ? )",
        (input("EmployeeId: "), input("LastName: "), input("FirstName: "), input("Title: "), input("ReportsTo: "),
         input("BirthDate: ") , input("HireDate: "),input("Address: "), input("City: "), input("State: ") , input("Country: "), input("PostalCode: "), input("Phone: "),input("Fax: "),input("Email: ")))

    # save: anytime u modify anything in your DB, U need to conduct commit.
    conn.commit()

def delete_employee():
    print("please fill in the blanks to remove an employee :\n")
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

#Report on a purchase - adds information about a purchase to the DB.
def add_purchase():
    print("please fill in the blanks to add a purchase :\n")
    c.execute(
        "INSERT INTO invoices (InvoiceId, CustomerId, InvoiceDate, BillingAddress, BillingCity, BillingState, BillingCountry, BillingPostalCode, Total) VALUES (?, ?, ?, ?, ? , ? , ? , ? , ?)",
        (input("InvoiceId: "), input("CustomerId: "), input("InvoiceDate: "), input("BillingAddress: "), input("BillingCity: "),
         input("BillingState: ")
         , input("BillingCountry: "), input("BillingPostalCode: "), input("Total: ")))
    # save: anytime u modify anything in your DB, U need to conduct commit.
    conn.commit()



def exit_the_program():
    print("BYEEE !!!")
    close()
    exit(0)

def second_menu():
    pass

def menu():

    choice = '0'
    while choice == '0':

        print(" 1 : add a track")
        print(" 2 : get playlists")
        print(" 3 : create a playlist")
        print(" 4 : add_song_to_playlist")
        print(" 5 : add_employee")
        print(" 6 : delete_employee")
        print(" 7 : add a purchase")
        print(" x : exit the program")


        choice = input("Please make a choice:  ")

        # if choice == "5":
        #     print("Go to another menu")
            #second_menu()
        if choice == "1":
            add_track()
            menu()
        elif choice == "2":
            get_playlists()
            menu()
        elif choice == "3":
            create_playlist()
            menu()
        elif choice == "4":
            add_song_to_playlist()
            menu()
        elif choice == "5":
            add_employee()
            menu()
        elif choice == "6":
            delete_employee()
            menu()
        elif choice == "7":
            add_purchase()
            menu()
        elif choice == "x":
            exit_the_program()
        else:
            print("I don't understand your choice..try again")
            menu()

def main():

    menu()




    # menu ={
    #     '1' : add_track(),
    #     '2' : get_playlists(),
    #     '3' : create_playlist(),
    #     '4' : add_song_to_playlist(),
    #     '5' : add_employee(),
    #     '6' : delete_employee(),
    #     '7' : add_purchase(),
    #     'x' : exit_the_program(),
    # }
    # # adding the .__name__ method allowed me to print the function names as a string.
    # for key in sorted(menu):
    #     print(key, '=>', menu[key].__name__)

    # selected = input("please select an option from the list:    ")
    # while True:
    #     menu.get(selectedaction, errhandler)()
    #     selectedaction = input("please select an option from the list:    ")

    #create_table()
    #add_track()
    #get_playlists()
    #create_playlist()
    #add_song_to_playlist()
    #add_employee()
    #delete_employee()

    #conn.execute("PRAGMA busy_timeout = 30000")



    close()

if __name__ == '__main__':
    main()