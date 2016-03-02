#!venv/bin/python
from flask import Flask
import random

app = Flask(__name__)
animals = open('files/animals.txt','r').read().split('\n')
things = open('files/things.txt','r').read().split('\n')


def getAnimal():
    return animals[random.randint(0,len(animals)-1)].lower()


def getThing():
    print 'Thing Number: {0}\nRandom Value:{1}'.format(len(things), random.randint(0,len(things)-2))
    return things[random.randint(0,len(things)-2)].lower()


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/phrase')
def phrase():
    animal = getAnimal()
    thing = getThing()
    return 'Get all your {0}s in a {1}'.format(animal, thing)


if __name__ == '__main__':
    app.run(debug=True)
