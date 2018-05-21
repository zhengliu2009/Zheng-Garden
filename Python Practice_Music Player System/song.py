class Song:
    def __init__(self, title, artist, album):  # accept 3 parameters
        self.__title = title                   # 3 private data attributes
        self.__artist = artist 
        self.__album = album
        self.__times_played = 0                # additional private data attribute 

    def __str__(self):
        return '{} by {} from {} (played {} times)'.format(self.__title, self.__artist, self.__album, self.__times_played)
    # a __str__ method for the object

    def get_title(self):    # accessor methods of the four data attributes that each Song object will have
        return self.__title

    def get_artist(self):
        return self.__artist

    def get_album(self):
        return self.__album

    def get_times_played(self):
        return self.__times_played

    def play(self):
        self.__times_played += 1  # a play method,increment the __times_played attribute by 1
        
