# importing the time module
import time
# importing the random module
import random

# welcoming the user


print("Press any character to see your cool nickname")
input()
# wait for 1 second
time.sleep(1)


firstName = '''Murderous Wicked The Powerful abrupt bad corrupt destructive hateful heinous hideous malevolent malicious nefarious ugly unpleasant vicious
vile villainous wicked base foul low offensive poison reprobate wrong angry atrocious baneful beastly calamitous damnable
depraved disastrous execrable harmful iniquitous injurious loathsome maleficent malignant obscene pernicious rancorous repugnant repulsive revolting spiteful stinking unpropitious wrathful '''

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
print("Hello" + " " + word1 + " " + word2 + ".")


