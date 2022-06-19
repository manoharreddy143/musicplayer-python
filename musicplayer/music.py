from playsound import playsound

print ("no. of available songs \n1.Senorita \ n2.believer \ n3.Despacito \ n4.arcade" )
order = input ('enter the music which you want to play :')
if "Senorita" in order:
playsound('C:\\music\\Senorita.mp3')

elif "believer" in order:
playsound ('C:\\music\\believer.mp3')

elif "Despacito" in order:
playsound ('C:\\music\\Despacito.mp3')

elif "arcade" in order:
playsound ('C:\\music\\arcade.mp3')