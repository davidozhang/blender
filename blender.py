'''
Blender - Terminal word flashcard generator for macOS
v3.0

Generate flashcards from a file containing sentences with a marked key word, like this:
an *objurgation* is expected for coming home after curfew

Also optionally supports generating word association map.
'''

import argparse
import os
import sys

from command import Command
from db import Db
from display import Display
from emoji_mapper import EmojiMapper
from emoji_types import EmojiTypes
from input_mapper import InputMapper
from file_io import FileIO
from word_association import WordAssociation

WORD_ASSOCIATION_DEFAULT_FILE = '.word_association'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sentences', help='path to sentences file', type=str)

    args = parser.parse_args()
    sentences_file = args.sentences

    try:
        db = Db(FileIO.read(sentences_file))
    except Exception:
        Display.error('Error occurred while processing sentences file.')
        sys.exit()

    wa = WordAssociation(FileIO.read_optional(WORD_ASSOCIATION_DEFAULT_FILE))

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

            disp = k
            associations = wa.get_associations_for_word(Db.strip_key(k))
            if len(associations) > 0:
                disp = Db.mark_key(k, EmojiMapper.get(EmojiTypes.EYES))

            Display.display(disp, True)

            error = False
            next_word = False

            inp = raw_input(prompt).lower()
            commands = InputMapper.get_commands(inp)
            word = Db.strip_key(k)

            for command in commands:
                if command == Command.KNOW_IT:
                    db.mark(k, EmojiMapper.get(EmojiTypes.THUMBS_UP))
                    next_word = True
                elif command == Command.SKIP:
                    db.unmark(k)
                    next_word = True
                elif command == Command.OPEN_DICTIONARY:
                    Display.info('Opening dictionary for ' + Display.bold_replace(word))
                    os.system('open dict://{}'.format(word))
                elif command == Command.SHOW_CONTEXT:
                    Display.display(v)
                elif command == Command.DISPLAY_ALL_WORDS:
                    Display.display_all_words(
                        db.get_data(),
                        db.get_total_word_count(),
                        db.get_known_word_count()
                    )
                elif command == Command.ASSOCIATE:
                    word_prompt = Display.get_association_prompt(word)
                    associations = raw_input(word_prompt).split()
                    associations = [w.lower() for w in associations]
                    associations.append(word)
                    wa.associate(associations)
                elif command == Command.DISPLAY_ASSOCIATED_WORDS:
                    Display.display_associated_words(associations)
                elif command == Command.DISPLAY_ALL_ASSOCIATIONS:
                    Display.display_all_associations(
                        wa.get_all_associations(),
                        wa.get_num_associations()
                    )
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
        FileIO.write_db(sentences_file, db.get_data())
        FileIO.write_associations(WORD_ASSOCIATION_DEFAULT_FILE, wa.get_all_associations())

if __name__ == '__main__':
    main()
