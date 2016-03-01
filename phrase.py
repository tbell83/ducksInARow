#!venv/bin/python
from flask import Flask
import random

app = Flask(__name__)
animals = open('files/animals.txt','r').read().split('\n')
collectiveNouns = open('files/things.txt','r').read().split('\n')


def getAnimal():
    return animals[random.randint(0,len(animals)-1)].lower()


def getCollectiveNoun():
    return collectiveNouns[random.randint(0,len(collectiveNouns)-2)].lower()


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/phrase')
def phrase():
    animal = getAnimal()
    thing = getCollectiveNoun()
    return 'Get all your {0}s in a {1}'.format(animal, thing)


if __name__ == '__main__':
    app.run(debug=True)
