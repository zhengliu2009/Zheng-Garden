#!/usr/bin/python3
import time
import sys

# Multi-line string variable for the main program menu.
MAIN_MENU = (
'''======================================================================
\tEnter 1 to Search for a Movie Title and See its Cast
\tEnter 2 to Search for an Actor/Actress and See their Movies
\tEnter 3 to Search for movies released in a given year
\tEnter anything else to exit.
======================================================================
Please type an option from the list above:
>>> ''')

# Filename for the IMDB database
IMDB_FILE = 'imdb_data.tsv'

def main():
    """Main program execution function.

    This is already written for you and should not be be modified.
    """
    # Two dict objects will serve as efficient data structures for look ups
    titles_index = {}
    actors_index = {}
    year_index = {}                      # build year_index for extra credit
    start = time.time()
    rows = build_indexes(titles_index, actors_index, year_index)
    print('Indexed {:,} rows from {} in {:,.2f}s'.format(
        rows, IMDB_FILE, time.time() - start))
    memory_used = sys.getsizeof(titles_index) + sys.getsizeof(actors_index)
    print('Using {:,.2f}MB of memory'.format(memory_used / 2 ** 20))

    # Stay in the loop until an invalid action is received.
    while True:
        action = input(MAIN_MENU)
        if action == '1':                              
            search_for_title(titles_index)
        elif action == '2':
            movies_for_actor(actors_index)            
        elif action =='3':              # build year_index for extra credit
            year_movie(year_index)                    
        else:
            print('"{}" is not a valid action. Goodbye!'.format(action))
            break


def build_indexes(titles_index, actors_index, year_index):
    """Processes IMDB_FILE and populates two dict data structures.

    Args:
        titles_index: Dict data structure keyed by title values from IMDB_FILE
        actors_index: Dict data structure keyed by actor values from IMDB_FILE
    Returns:
        Number of rows read from IMDB_FILE
    """
    
    f = open(IMDB_FILE, 'r')     #open up the imdb_data.tsv file
    count = 0                    #keep a count of number of lines I process
    for line in f:
        line = line.rstrip()
        data = line.split('\t')  #split data
        entry = {}               #build an empty dictionary
        entry['year'] = data[0]
        entry['title'] = data[1]
        entry['name'] = data[2] + " " + data[3]  #combine first name and last name
        entry['gender'] = data[4]
        entry['character'] = data[5]
        
        try:                     #build titles_index
            titles_index[entry['title'].lower()].append(entry)      # make keys in lower case
        except KeyError:
            titles_index[entry['title'].lower().strip()] = [entry]

        try:                     #build actors_index
            actors_index[entry['name'].lower()].append(entry)       # make keys in lower case
        except KeyError:
            actors_index[entry['name'].lower()] = [entry]

        try:
            year_index[entry['year']].append(entry)                 #build year_index
        except KeyError:
            year_index[entry['year']] = [entry] 

        count +=1
    f.close()                    #Do I need to close file here?
    return count                 #return number of lines I processed
 
def sort_by_name(data):
    """Helper function to be passed to the sort() method for titles_index values.

    Args:
        data: dict object
    Return:
        data['name'] Value
    """
    return data['name']

def sort_by_year(data):
    """Helper function to be passed to the sort() method for actors_index values.

    Args:
        data: dict object
    Return:
        data['year'] Value
    """
    return data['year']

def search_for_title(titles_index):
    """Lookup and print the actors/actresses from a movie by title.

    Args:
        titles_index: Dict data structure keyed by title
    """
    
    movie_title = input('Please type in the movie\'s title: ')    # Prompt the user to type a movie title.
    movie_title = movie_title.lower()                             # make search case-insensitive
    if movie_title in titles_index:                               # Check to see if that title is found in the database 
                                                                  # you passed in via the titles_index variable.
        film_data = titles_index[movie_title]
        year = film_data[0]['year']
        print('\"{}\" was released in {}'.format(movie_title, year))   #"Deadpool" was released in 2016  

        for entry in film_data:                                   # Some one played the character "Character"                         
            print()
            output = entry['name'] + " played the character " + entry['character']
            print(output)
 
    elif movie_title not in titles_index:                         # Sorry, "Bad Movie" could not be found
        print('Sorry, \"{}\" could not be found'.format(movie_title))           # Sorry, "Bad Movie" could not be found
        print()

def movies_for_actor(actors_index):
    """Lookup and print the movies that an actor/actress starred in.

    Args:
        actors_index: Dict data structure keyed by year
    """
    actor_name = input('Please type in name of the actor or actress: ')  # Prompt the user to type the name of an actor or actress.
    actor_name = actor_name.lower()                                      # make search case-insensitive
    if actor_name in actors_index:                                       # If the name is found, you'll want to print output 
        for entry in actors_index[actor_name]:
            print('Played \'{}\' in {} ({})'.format(entry['character'], entry['title'], entry['year']))
            print()                                                      # looks better with an empty line
    elif actor_name not in actors_index:                                 # Sorry, "Jason Prodonovich" could not be found
        print('Sorry, \"{}\" could not be found'.format(actor_name))
        print()                                                          # looks better with an empty line

def year_movie(year_index):
    year = input('Please type in the year you want to look up: ')        # movies for a certain year
    if year in year_index:
        for entry in year_index[year]:
            print(entry['title'])
    else:
        print('Invalid year.')
    
main()

