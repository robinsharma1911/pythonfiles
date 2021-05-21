import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

#     """MAIN WINDOW"""
window = Tk()
window.geometry ("400x500+700+100")
window.title ('music player')
window.config (bg='dark grey')


mixer.init()        #initializing the mixer...
music_state = False       #music_state,play or stop
vol = 0.6               #initial state of volume...
mylist = []             #list to store songs of a directory..
current_song_lbl = StringVar()      #lable to show current running song name


#      """FUNCTIONS START HERE"""


#      """"TOP FRAME FUNCTIONS"""

def all_songs(): #this function is blank for future use , songs_button in Top Frame
    pass
   
def exit():    #to quit to screen
    window.destroy()
    
      
def add_folder():       #add directory ...  
    try:
        global directory
        directory = filedialog.askdirectory()
        os.chdir(directory)
        
        files = os.listdir(directory)
        for song in files:
            if song.endswith(".mp3"):
                mylist.append(song)
        
        for values in mylist: 
            if new is None:      
                add_folder()  
            else:
                new.insert(0,values)
                add_button.pack_forget()          
    except:
         pass



#      """MIDDLE FRAME FUNCTIONS"""

def CurSelet(event): 
    global current_song_lbl       #current selection of song and play from playlist...   
    global index
    b = new.curselection()[0]
    index = len(mylist) - b - 1
    mixer.music.load(mylist[index])
    mixer.music.play()
    current_song_lbl.set(mylist[index])
   
    

#      """Bottom Frame functions"""

def vol_up():       #volume up function
    global vol
    if vol < 1:
        vol=vol+0.1
        mixer.music.set_volume(vol)


def vol_down():     #volume down function
    global vol
    if vol > 0.1:
        vol=vol-0.1
        mixer.music.set_volume(vol)


def music_pause():      #function to pause/unpause 
    global music_state
    if music_state:
        mixer.music.pause()
        
        music_state = False
    else:
        mixer.music.unpause()
        music_state = True


def previous_song():        #play previous song
    global current_song_lbl
    global index
    index += 1
    mixer.pre_init(44100,-16,2, 1024)
    mixer.init()
    mixer.music.load(mylist[index])
    mixer.music.play()
    current_song_lbl.set(mylist[index])


def next_song():           #play next song
    global current_song_lbl
    global index
    index -= 1
    mixer.pre_init(44100,-16,2, 1024)
    mixer.init()
    mixer.music.load(mylist[index])
    mixer.music.play()
    current_song_lbl.set(mylist[index])



#      """TOP FRAME"""

#top side frame having buttons songs,exit,add
top_frame = Frame( window , bg = "dark grey" )
top_frame.pack ( side = TOP , fill = X )

#buttons...of top frame
songs_button = Button( top_frame , bd = 1 , text = "   songs   " , command = all_songs )
songs_button.pack ( side = LEFT ) 

exit_button = Button( top_frame , bd = 1 , text = "   exit   " , command = exit )
exit_button.pack ( side = RIGHT )
 
add_button = Button(top_frame,bd=1,text="    add    " , command = add_folder )
add_button.pack ( side = TOP )


#       """Mid Frame"""

#mid frame having listbox with scrollbar
mid_frame = Frame( window , bg = "dark grey" ) 
mid_frame.pack ( fill = BOTH , expand = True )

#listbox and scrollbar and current selection of song of Middle Frame
new = Listbox( mid_frame )                       
scrollbar = Scrollbar( mid_frame , bg = "grey" )
new.config ( yscrollcommand = scrollbar.set )
scrollbar.config ( command = new.yview ) 
new.bind ( '<<ListboxSelect>>' , CurSelet )         #bind current selection of song function
scrollbar.pack ( side = RIGHT , fill = BOTH )
new.pack ( fill = BOTH , expand = True )


 #     """BOTTOM FRAME"""

#bottom frame having songs play/pause,nxt....
bottom_frame = Frame( window, bg = "dark grey", height = 100, width = 300 ) 
bottom_frame.pack ( side = BOTTOM  )

song_name_lable = Label( bottom_frame , textvariable = current_song_lbl , bg="white",fg="black",font = (4) ,  width=25 , anchor='w' )
song_name_lable.pack ( side = TOP  )

#buttons...of bottom Frame
vol1_button = Button( bottom_frame , bd = 1 , text= "    vol+   " , command = vol_up )      
vol1_button.pack ( side = TOP , expand = True )

vol0_button = Button( bottom_frame , bd = 1 , text = "     vol-    " , command = vol_down )
vol0_button.pack ( side=BOTTOM , expand=True )

previous_button = Button( bottom_frame , bd = 1 , text = " previous " , command = previous_song )
previous_button.pack ( side=LEFT , expand=True )

next_button = Button( bottom_frame , bd = 1 , text = "    next     " , command = next_song )       
next_button.pack ( side=RIGHT , expand=True )

# play_img=PhotoImage(file="play-button.png")
pause_button = Button( bottom_frame ,text = '  pause  ' ,bd=1,  command = music_pause )
pause_button.pack ( side = RIGHT  )

window.mainloop()