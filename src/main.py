import sys
import random
greetingsFile = open('src/greetings.txt','r')
greetings = greetingsFile.read().split('\n')
modelFile = open('src/cat','r')
model = modelFile.read()
out = model.replace('$SAY',random.choice(greetings))
print(out)
