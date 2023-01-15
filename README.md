# PythonLearningGame

<div align="center">

```
----------------------------------------
 >>>>> Hello in an exercise game! <<<<< 
----------------------------------------
```

</div>

## Table of contents:

- [Flow of the game](#flow-of-the-game)
- [The aim of the project](#the-aim-of-the-project)
- [What is my motivation?](#what-is-my-motivation)
- [Technologies & Documentation](#technologies--documentation)
- [Downloading project](#downloading-project)
- [Download & run](#download--run)

## Flow of the game

- Start of the game:

```
----------------------------------------
 >>>>> Hello in an exercise game! <<<<< 
----------------------------------------
Write down your name:
----------------------------------------
```

- Choose mode:

```
----------------------------------------
Welcome in the game <user_name>! What do you want to do?
Learn: type 'a'
Play game: type 'b'
Your choice: 
----------------------------------------
```

- Choose subject of questions:

```
----------------------------------------
Welcome <user_name> in learning mode! Now, you have to choose, which subject you want to use in learning. Choose from below:
Methods on dictionaries: type 'a'
Methods on integers/boolean: type 'b'
Methods on floats: type 'c'
Methods on lists: type 'd'
Methods on sets: type 'e'
Methods on strings: type 'f'
Methods on tuples: type 'g'
Your choice: 
----------------------------------------
```

- Learn:

```
Let the learning begin <user_name>!
----------------------------------------
Method: Copy
Type:
If you want to get description of above method: y
If you want to skip that one: n
If you want to exit: e
Your choice: p
----------------------------------------
Oopsie! Bad answer - type again: n
----------------------------------------
Method: Values
Type:
If you want to get description of above method: y
If you want to skip that one: n
If you want to exit: e
Your choice: y
----------------------------------------
Method: values
Description:  D.values() -> an object providing a view on D's values 
----------------------------------------
Method: Values
Type:
If you want to get description of above method: y
If you want to skip that one: n
If you want to exit: e
Your choice: 
```

- ..or play:

```
Let the game begin <user_name>! Now you will have to answer 10 questions about chosen subject. 
Collect 10 points to win the game! 
Points: 0
----------------------------------------
Question number 1:
What does get method?
Type:
y (yes) -> if you can explain,
n (no) -> if you can't,
e (exit) -> to exit the game.
Answer: p
----------------------------------------
Choose one option from below:
y (yes) -> if you can explain,
n (no) -> if you can't,
e (exit) -> to exit the game.
Answer: y
----------------------------------------
Nice one! You have 1 point!
----------------------------------------
Question number 2:
What does popitem method?
Type:
y (yes) -> if you can explain,
n (no) -> if you can't,
e (exit) -> to exit the game.
Answer: n
----------------------------------------
Next time you'll get it!
Points: 1
----------------------------------------
Here you can see method and the description:
Method:
Popitem

Description:

        Remove and return a (key, value) pair as a 2-tuple.
        
        Pairs are returned in LIFO (last-in, first-out) order.
        Raises KeyError if the dict is empty.
        
```

- Check if user wants to play again:

```
Thanks for playing my game! Do you want to play it once again?
Type:
Play once again: y
Naaah, not this time: n
Your choice: 
```

## The aim of the project

Simple bash app where user can learn things about python.

## What is my motivation?

That app is most efficient way to learn methods on python3 bulit-in variable types.

## Technologies & Documentation

- [Python 3](https://docs.python.org/3/)

## Installation
<details>
<summary>Python:</summary>
Visit https://www.python.org/downloads/ and type which installing package you prefer (by your operating system) and download the package.
After download, go through installation process.
After above, let's check if Python is installed on your computer. To do this, open your terminal or command prompt and type:
For MacOS/Linux:
```
python3 --version
```
For Windows:
```
python --version
```
</details>

##  Download & run
We've seen how to run venv. Keep that running!

<details>
<summary>Now we can simply clone this repo, and see if it's working on our machine (in case we did everything above count creating virtualenv):</summary>

```
git init                                                         # to initialize repository
git clone https://github.com/xwojziarnik/PythonLearningGame      # to clone this repository into your local machine

python3 app/learning_game.py
```
</details>

And that's it! Great job!
