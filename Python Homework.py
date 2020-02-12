# importing the time module
import time
# importing the random module
import random

# welcoming the user


print("Press enter to see your codename")
input()
# wait for 1 second
time.sleep(1)


firstName = '''Murderous Wicked The Powerful abrupt bad corrupt destructive hateful heinous hideous malevolent malicious  
unpleasant vicious vile villainous wicked foul low offensive poison reprobate wrong angry atrocious baneful beastly 
depraved disastrous execrable harmful iniquitous injurious loathsome maleficent malignant obscene pernicious rancorous
repugnant repulsive revolting spiteful stinking unpropitious wrathful calamitous damnable nefarious ugly'''

lastName = '''Python Hawk Falcon Anaconda Viper Abomination 
Captain Baboon Ape Tiger Shark King Communist'''

firstName = firstName.split(' ')
lastName = lastName.split(' ')

# randomly choose a secret word from our "someWords" LIST.
word1 = random.choice(firstName)
word2 = random.choice(lastName)

# creates an variable with an empty value
firstName = ''
lastName = ''
word1 = word1.capitalize()
word2 = word2.capitalize()
print("Hello" + " " + word1 + " " + word2 + ".\n")
exitMessage = "This message will disappear in 3 seconds"
exitMessage = exitMessage.capitalize()
print(exitMessage)
time.sleep(2.5)
quit()


