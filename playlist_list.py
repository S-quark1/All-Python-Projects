playlist=[]

print("Hello")
print("Type 'add' to add a song")
print("Type 'remove' to remove a song")
print("Type 'show' to show a song")
print("Type 'stop' to close the playlist")
print(" ")

while True:
    command=input("Please,enter a command: ")
    if command=="add":
        song=input("Please, enter a song: ")
        if song not in playlist:
            playlist.append(song)
            print("Your song is added!")
        else:
            print("The song is already added")
    if command=="remove":
        song=input("Please,enter a song: ")
        if song in playlist:
            playlist.remove(song)
            print("Done")
        else:
            print("I couldn't find the song")
    if command=="show":
        print(playlist)
    if command=="stop":
        print("Bye")
        break
        
