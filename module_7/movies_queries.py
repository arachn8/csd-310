import mysql.connector
from mysql.connector import errorcode
config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "port": "3006",
    "database": "movies",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")

    myCursor = db.cursor()
    myCursor.execute("SELECT * FROM studio")
    studios = myCursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print("Studio id: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

    myCursor.execute("SELECT * FROM genre")
    genres = myCursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print("Genre id: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    myCursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime <= 120")
    shorts = myCursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for short in shorts:
        print("Film Name: {}\nRuntime: {}\n".format(short[0], short[1]))

    myCursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    directors = myCursor.fetchall()
    print("-- DISPLAYING Director RECORDS in Order")
    for director in directors:
        print("Film Name: {}\nDirector: {}\n".format(director[0], director[1]))



except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
