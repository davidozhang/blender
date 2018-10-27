'''
Blender - Terminal word flashcard generator for macOS
v1.6

Generate flashcards from a file containing sentences with a marked key word, like this:
an *objurgation* is expected for coming home after curfew
'''

import argparse
import os
import sys

from db import Db
from display import Display
from file_io import FileIO
from search import Search


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filepath', help='file path', type=str)

    args = parser.parse_args()
    fp = args.filepath
    lines = FileIO.read(fp)
    db = Db(lines)

    error_lines = db.get_error_lines()
    if len(error_lines) > 0:
        Display.error('Keyword was not properly marked in the following lines:')
        for line in error_lines:
            print line
        sys.exit()

    kwc = db.get_known_word_count()
    twc = db.get_total_word_count()

    Display.wrap([
        'Blender - Word flashcard generator',
        'Number of words: {} ({} known/{} unknown)'.format(
            str(twc),
            kwc,
            str(twc - kwc)),
        'Keyboard shortcuts: {} - know it, {} - not quite (opens dictionary), {} - get context, {} - all words'.format(
            'a',
            's',
            'd',
            'f'
        ),
        'A word that you already know is marked with a ' + Display.thumbs_up_emoji()
    ])

    try:
        context_required = False
        error = False
        k = None
        while True:
            kwc = db.get_known_word_count()

            if not context_required and not error:
                k, v = db.get_next_key_value()

            Display.display(v) if context_required else Display.display(k, True)
            context_required = False
            error = False

            inp = raw_input('a/s/d/f: ').lower()
            if inp == 'a':
                db.mark(k)
            elif inp == 's':
                db.unmark(k)
                os.system('open dict://{}'.format(k.split()[0]))
            elif inp == 'd':
                context_required = True
            elif inp == 'f':
                Display.display_all_words(db.get_data())
            else:
                Display.error('Invalid command!\n')
                error = True

    except KeyboardInterrupt:
        pass
    finally:
        FileIO.write(fp, db.get_data())

if __name__ == '__main__':
    main()
