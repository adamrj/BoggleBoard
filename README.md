# BoggleBoard
Week 3 weekend project

Week 3 Day 5
============

This weekend you'll be modeling a [Boggle](http://en.wikipedia.org/wiki/Boggle) board in Python.

#### Step 1:

Create a BoggleBoard class with one method called shake. Your shake method should return a nested array with the randomized letters of the Boggle dice.

```py
board = BoggleBoard()
print(board)

# An unshaken board prints out something sensible, like:
# ____
# ____
# ____
# ____

board.shake()
print(board)

# Prints out:
# DUMV
# KSPD
# HCDA
# ZOHG
```

#### Step 2:

Create another method find_all that finds all possible words greater than 3 or more letters. This can be verified by checking to see if the word exists in dictionary.txt

#### Step 3

Gamify it. Think about how you would like to play. Would you like to guess words with a timer? How about storing high scores to a db? Make this anything you like. Have fun, be creative, see how good of a user experience you can make it.