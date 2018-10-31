# Blender
Terminal word flashcard generator for macOS

<img width="802" alt="screen shot 2018-10-30 at 9 19 53 pm" src="https://user-images.githubusercontent.com/6395458/47765943-9a2beb80-dc89-11e8-91aa-d7b2925bbe84.png">

## How to use
Write up sentences in a text file and wrap the keyword you want to learn with asterisks (`*`):

`an *objurgation* is expected for coming home after curfew`

Blender will pick up those words and generate flashcards within the terminal for you to study with!

Run the program and pass the file location into the program with parameter, like this:

```bash
python blender.py --filepath file_location.txt
```

For each flashcard you can:
- Mark it as known
- Pass on it
- Show the context that the word is used in
- Open dictionary to revisit definition
- View all the words you're studying with so far, the words you know are marked with a 👍

Upon exiting, Blender will automatically prepend all the lines containing the words you know in the original file with a `#`.

Happy studying!

## Installation
Make sure you have pip installed on your laptop (https://pip.pypa.io/en/stable/installing/).
You must install the requirements:

```bash
pip install -r requirements.txt
```

## Issues?
File an issue or make a pull request to suggest a change to Blender!
