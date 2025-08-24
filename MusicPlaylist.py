import mysql.connector
from tabulate import tabulate

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sreehari",
        database="musicplaylist"
    )
def add_song():
    song = input("Enter Song Name: ").strip()
    artist = input("Enter Artist name: ").strip()

    mydb = connect_db()
    c = mydb.cursor()
    a=("INSERT INTO playlist (song, artist) values(%s, %s)")
    b=(song, artist)
    c.execute(a,b)
    mydb.commit()
    mydb.close()
    print(f"{song} by {artist} added to playlist")
    print(f"{artist}'s {song} is added to playlist")


def view_playlist():
    mydb = connect_db()
    c= mydb.cursor()
    c.execute("SELECT * FROM playlist")
    songs = c.fetchall()
    mydb.close()

    if songs:
        headers = ["ID", "Songs", "Artist"]
        print("=============== Your Playlist ===============")
        print(tabulate(songs, headers, tablefmt="fancy_grid"))
    else:
        print("Your Playlist is Empty")

def update_song():
    view_playlist()
    song_id = input("Enter Song ID: ")
    new_song = input("Enter new Song: ").strip()
    new_artist = input("Enter new Artist: ").strip()

    mydb = connect_db()
    c = mydb.cursor()
    s=("UPDATE playlist SET song=%s, artist=%s WHERE id=%s")
    v=(new_song, new_artist, song_id)
    c.execute(s,v)
    mydb.commit()
    mydb.close()
    print("Song Updated Successfully")

def delete_song():
    view_playlist()
    song_id = input("Enter the Song ID to delete: ")
    mydb = connect_db()
    c = mydb.cursor()
    e=("DELETE FROM playlist WHERE song_id=%s")
    f=(song_id)
    mydb.commit()
    mydb.close()
    print(f"{song_id} Deleted Successfully")

def menu():
    while True:
        print("\n. === Music Playlist Manager ===")
        print("1) Add Song")
        print("2) View Playlist")
        print("3) Update Playlist")
        print("4) Delete Song")
        print("E) Exit")

        choice = input("Select your Choice: ")

        if choice =="1":
            add_song()
        elif choice =="2":
            view_playlist()
        elif choice=="3":
            update_song()
        elif choice=="4":
            delete_song()
        elif choice=="5":
            print("Exiting")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    menu()