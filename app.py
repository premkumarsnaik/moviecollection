movies_collection = []                                #movie storage


def adding_movie(name , director , realising_year):   #adding movie information to the all_movie list
    movies_collection.append({ 'name' : name,
                               'director' : director,
                               'realising_year' : realising_year})


def add_new_movie():                                  #asking user for the movie information
    name = input('enter movie name: ')
    director = input('enter movie director name: ')
    realising_year = input('enter realising year: ')
    adding_movie(name , director , realising_year)
    print('movie successfully added')


def view_movies():                                     #function for viewing movie collection
    print('your movie collection: ')
    for movie in movies_collection:
        print(f'name: {movie["name"]}')
        print(f'director: {movie["director"]}')
        print(f'year: {movie["realising_year"]}')


def find_movie(a):                  #finding movie directed by a director
    movie_directedby_director =[]
    for i in range(len(movies_collection)):
        if (movies_collection[i]['director']) == a or (movies_collection[i]['realising_year']) == a :
            movie_directedby_director.append(movies_collection[i]['name'])
    print('your desired movies list: ')
    print(movie_directedby_director)


print('enter "a" to add a movie, '
       'enter "v" to view your movies,'
       'enter "f" to find your movie '
      'enter "exit" to end the programm')

while True:
    user_input = input('\n enter the key word to perform disired work: ')

    if user_input=='a':
       add_new_movie()
    elif user_input=='v':
       view_movies()
    elif user_input=='f':
       a = input('enter movie year or director name that you want: ')
       find_movie(a)
    elif user_input=='exit':
        print('exiting')
        break
    else :
       print('not a valid input ')




