# Blender
A powerful terminal word flashcard generator for macOS.

## How to use
Write up sentences in a text file and wrap the keyword you want to learn with asterisks (`*`):

`an *objurgation* is expected for coming home after curfew`

Blender will pick up those words and generate flashcards within the terminal for you to study with!

Run the program and pass the sentences file location into the program with parameter `--sentences`, like this:

```bash
python blender.py --sentences file_location.txt
```

For each flashcard you can:
- Mark it as known
- Pass on it
- Show the context that the word is used in
- Open dictionary to revisit definition
- View all the words you're studying with so far, the words you know are marked with a 👍
- View all associations that you have built so far
- View associated words for the word
- Add association between the word to a list of words separated by space

Upon exiting, Blender will automatically prepend all the lines containing the words you know in the original file with a `#`. In addition, it will also store all word associations you have built in `.word_association`.

Happy studying!

## Installation
Make sure you have pip installed on your laptop (https://pip.pypa.io/en/stable/installing/).
You must install the requirements:

```bash
pip install -r requirements.txt
```

## Issues?
File an issue or make a pull request to suggest a change to Blender!
