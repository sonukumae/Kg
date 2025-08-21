#this prints a raandom jokes
import random

def get_joke():
	jokes = [
		"Why don't scientists trust atoms? Because they make up everything!",
		"Why did the math book look sad? Because it had too many problems.",
		"Why was the computer cold? It left its Windows open!"
	]
	return random.choice(jokes)

# example of pyjokes
import pyjokes
joke = pyjokes.get_joke()
print (joke)

