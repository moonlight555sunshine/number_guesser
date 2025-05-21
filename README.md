# Number Guessing Game 🎯

This is a simple command-line number guessing game written in Python.

## 🕹️ How to Play

- The program randomly selects a **secret number** between **1 and 100**.
- Your goal is to guess the number.
- After each guess, the program will tell you if your number is:
  - **Too small**
  - **Too big**
  - Or if you’ve **guessed correctly**!

The game continues until you guess the correct number.

## 🚧 Input Rules

- Only **integers** between **0 and 100** are accepted.
- If you enter:
  - A number outside this range → it will be rejected.
  - A non-integer (like `3.5`) → it will be rejected.
  - A non-number (like `"hello"`) → it will be rejected.

## ▶️ Running the Game

Make sure you have Python 3 installed, then run:

```bash
python main.py
```

## ✅ Example

```
Guess the number: 50
Too small!
Guess the number: 75
Too big!
Guess the number: 62
You win!
```
