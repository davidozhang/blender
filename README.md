# Blender
Terminal word flashcard generator for macOS

<img width="721" alt="screen shot 2018-10-26 at 11 18 06 pm" src="https://user-images.githubusercontent.com/6395458/47600405-6d1fc600-d975-11e8-8977-071286bbd1fa.png">

## How to use
Write up sentences in a text file and wrap the keyword you want to learn with asterisks (*). Blender will pick up those words and generate flashcards within the terminal for you to study with!

Run the program and pass the file location into the program with parameter, like this:

```python blender.py --filepath file_location.txt```

For each flashcard word you can:
- Press 'a' if you know it
- Press 's' if you don't quite know it (Blender will open the native dictionary to help you revisit the definition)
- Press 'd' if you want the context of the word in a sentence
- Press 'f' to show all the words you're studying with so far, with the words you know marked with a 👍

Upon exiting, Blender will automatically mark all the lines containing the words you know in the original file with a '#'.

Happy studying!

## Installation
Make sure you have pip installed on your laptop (https://pip.pypa.io/en/stable/installing/).
You can install the requirements with `pip install requirements.txt`

## Issues?
File an issue or make a pull request to suggest a change to Blender!
