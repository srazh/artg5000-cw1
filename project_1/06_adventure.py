# You can substitute text throughout an entire text using RegEx
import re


wonderland = '''Alice’s Adventures in Wonderland
by Lewis Carroll

CHAPTER I.
Down the Rabbit-Hole
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, “and what is the use of a book,” thought Alice “without pictures or conversations?”'''

new_adventure = re.sub("Alice", "Derek", wonderland)

print("----- Alice's Adventures-----------")
print(wonderland)
print("----- Derek's Adventures-----------")
print(new_adventure)