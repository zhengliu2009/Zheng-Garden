class MusicPlayer:
    def __init__(self):  # an __init__ method that does not accept any parameters 
        self.__playlist = []  # Empty List used to store Song objects
        self.__current_track_index = 0  # int - Index from __playlist. Initialize to 0
        self.__current_track = None  # Initialize this to the special Python value None

    def __str__(self):
        if self.__current_track_index != None:
            return '{} tracks. Currently playing... {}'.format(len(self.__playlist), self.__current_track)
        #return a string that includes a meaningful representation of the object's attributes

    def add_to_playlist(self, s):  # accept one parameter, a Song object
        self.__playlist.append(s)  # append it to the object's __playlist attribute

    def play(self):                # Implement a play method
        if self.__current_track_index >= 0 and self.__current_track_index < len(self.__playlist):
            self.__current_track = self.__playlist[self.__current_track_index]
            self.__current_track.play()
            print('Currently playing... {}'.format(self.__current_track))
        else:
            print('{} is not a valid track number'.format(self.__current_track_index))


    def prev(self):                # Implement a prev method
        self.__current_track_index -= 1  # subtract 1 from __current_track_index
        if self.__current_track_index < 0:
            self.__current_track_index = len(self.__playlist)-1
        # If the new value is less than 0, it should be set to the length of the __playlist attribute - 1
        self.play()                # call the play method

    def next(self):                # Implement a next method
        self.__current_track_index += 1  # add 1 from __current_track_index
        if self.__current_track_index == len(self.__playlist):
            self.__current_track_index = 0
        # If the new value is equal to the length of the __playlist attribute, it should be set to 0
        self.play()                # call the play method

    def find(self,search):         # Implement a find method,accept one parameter named search 
        f=False
        for i in range(len(self.__playlist)):
            if search == self.__playlist[i].get_title() or search == self.__playlist[i].get_artist():
                print('Found track {}...{}'.format(i, self.__playlist[i]))
                f=True
        if f==False:
            print('No matching Songs found for \"{}\"'.format(search))
        # ○	If no Songs match, you should print "No matching Songs found for X" where X is replaced with the search parameter passed into the method.
                
    
            

    
            
            
        
                                          
