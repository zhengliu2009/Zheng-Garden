import song             # Import the song and music_player modules
import music_player

def main():             # Add a main function and make sure it gets called 
    mp = music_player.MusicPlayer()  # create a MusicPlayer object
    add_song(mp)
    mp.play()
    mp.next()
    mp.next()
    mp.next()
    mp.next()
    mp.next()
    mp.prev()
    mp.prev()
    mp.find("Guns n' Roses")
    mp.find('Times Like These')
    mp.find('Justin Bieber')

def add_song(mp):       # Add an add_songs function
    song1 = song.Song('Welcome to the Jungle',"Guns n' Roses",'Appetite for Destruction')
    song2 = song.Song('Smells Like Teen Spirit','Nirvana','Nevermind')
    song3 = song.Song('Jeremy','Pearl Jam','Ten')
    song4 = song.Song('Times Like These','Foo Fighters','One by One')
    song5 = song.Song('Sweet Child of Mine',"Guns n' Roses",'Appetite for Destruction')
    mp.add_to_playlist(song1)
    mp.add_to_playlist(song2)
    mp.add_to_playlist(song3)
    mp.add_to_playlist(song4)
    mp.add_to_playlist(song5)
    
main()
