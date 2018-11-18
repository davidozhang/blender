'''
Blender - Terminal word flashcard generator for macOS
v3.0

Generate flashcards from a file containing sentences with a marked key word, like this:
an *objurgation* is expected for coming home after curfew
'''

import argparse
import os
import sys

from db import Db
from display import Display
from input_mapper import InputMapper
from command import Command
from file_io import FileIO
from word_association import WordAssociation


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sentences', help='path to sentences file', type=str)
    # parser.add_argument('--associations', help='path to associations file', type=str)

    args = parser.parse_args()
    sentences = args.sentences
    db = Db(FileIO.read(sentences))
    wa = WordAssociation()

    error_lines = db.get_error_lines()
    if len(error_lines) > 0:
        Display.error('Keyword was not properly marked in the following line(s):')
        for line in error_lines:
            Display.display(line)
        sys.exit()

    twc = db.get_total_word_count()
    kwc = db.get_known_word_count()

    Display.display_header(twc, kwc)

    try:
        error = False
        next_word = True

        k, v = None, None
        prompt = InputMapper.get_main_prompt()

        while True:
            if not error and next_word:
                k, v = db.get_next_key_value()

            Display.display(k, True)

            error = False
            next_word = False

            inp = raw_input(prompt).lower()
            commands = InputMapper.get_commands(inp)

            for command in commands:
                if command == Command.KNOW_IT:
                    db.mark(k)
                    next_word = True
                elif command == Command.NOT_QUITE_KNOW_IT:
                    db.unmark(k)
                    next_word = True
                elif command == Command.OPEN_DICTIONARY:
                    w = k.split()[0]
                    Display.info('Opening dictionary for ' + Display.bold_replace(w))
                    os.system('open dict://{}'.format(w))
                elif command == Command.SHOW_CONTEXT:
                    Display.display(v)
                elif command == Command.DISPLAY_ALL_WORDS:
                    Display.display_all_words(
                        db.get_data(),
                        db.get_total_word_count(),
                        db.get_known_word_count()
                    )
                elif command == Command.ASSOCIATE:
                    word = Db.strip_key(k)
                    assoc = raw_input('Enter words to associate \'{}\' with, separated by space: '.format(word)).split()
                    assoc = [w.lower() for w in assoc]
                    assoc.append(word)
                    wa.associate(assoc)
                elif command == Command.DISPLAY_ALL_WORD_ASSOCIATION_GROUPS:
                    Display.display_all_groups(wa.get_groups(), wa.get_num_groups())
                elif command == Command.CONFLICTING:
                    Display.error('Conflicting command')
                    error = True
                else:
                    Display.error('Unknown command')
                    error = True
            Display.new_line()

    except KeyboardInterrupt:
        pass
    finally:
        FileIO.write(sentences, db.get_data())

if __name__ == '__main__':
    main()
