'''
Blender - Terminal word flashcard generator for macOS
v1.6

Generate flashcards from a file containing sentences with a marked key word, like this:
an *objurgation* is expected for coming home after curfew
'''

import argparse
import emoji
import os
import random
import re
import sys

KNOWN_WORD_MARKER = '#'

def read(fp):
    lines = []
    with open(fp, 'r') as f:
        lines = f.read().splitlines()
    return lines

def search(line):
    return re.search('\*(.*)\*', line)

def mapper(lines):
    data = {}
    known_word_count = 0
    error_lines = []

    for line in lines:
        words = line.split()

        result = search(line)
        if not result:
            if line:
                error_lines.append(line)
        else:
            key = result.group(1)

            if len(words) > 0 and words[0] == KNOWN_WORD_MARKER:
                known_word_count += 1
                key = known_key(key)
            data[key.lower()] = line

    if len(error_lines) > 0:
        display('[Error] Keyword was not properly marked in the following lines:', True)
        for line in error_lines:
            print line
        sys.exit()

    return (data, known_word_count)

def bold_replace(s):
    return '\033[1m' + s + '\033[0m'

def display(line, all_bold=False):
    words = line.split()

    if all_bold:
        print bold_replace(line)
        return

    result = search(line)
    if result:
        actual = result.group(0)
        key = result.group(1)
        replace = bold_replace(key)

        for i in xrange(len(words)):
            if words[i] == actual:
                words[i] = replace

        print ' '.join(words)

def get_next_key(d):
    return random.choice(d.keys())

def mark_as_known(d, k, m):
    if k in d:
        words = d[k].split()
        if len(words) > 0 and words[0] == m:
            return d
        d[known_key(k)] = '{} {}'.format(m, d[k])
        d.pop(k)
    return d

def unmark(d, k, m):
    if k in d:
        words = d[k].split()
        if len(words) > 0 and words[0] == m:
            d[unknown_key(k)] = ' '.join(words[1:])
            d.pop(k)
    return d

def write(fp, d):
    written = 0
    l = len(d.keys())
    with open(fp, 'w') as f:
        for k in sorted(d.keys()):
            if written == l - 1:
                f.write(d[k] + '\n')
            else:
                f.write(d[k] + '\n\n')
            written += 1

def thumbs_up_emoji():
    return emoji.emojize(':thumbs_up:')

def known_key(k):
    return k + ' ' + thumbs_up_emoji()

def unknown_key(k):
    return k.split()[0]

def wrap(lst):
	border = ''
	max = 0
	for i in lst:
		if len(i) > max:
			max = len(i)
	border += '*' * (max + 4)
	max += 4
	print '\n' + border
	for j in lst:
		print '* '+j+' '*(max-1-len('* ' + j)) + '*'
	print border + '\n'

def display_all_words(d):
    wrap(['Start of display'])
    for k in sorted(d.keys()):
        display(k, True)
    wrap(['End of display'])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filepath', help='file path', type=str)

    args = parser.parse_args()
    fp = args.filepath
    lines = read(fp)
    data, kwc = mapper(lines)

    wrap([
        'Blender - Word flashcard generator',
        'Number of words: {} ({} known/{} unknown)'.format(
            str(len(data)),
            kwc,
            str(len(data) - kwc)),
        'Known word marker: {}'.format(KNOWN_WORD_MARKER),
        'Keyboard shortcuts: {} - know it, {} - not quite (opens dictionary), {} - get context, {} - all words'.format(
            'a',
            's',
            'd',
            'f'
        ),
        'A word that you already know is marked with a ' + thumbs_up_emoji()
    ])

    try:
        context_required = False
        error = False
        k = None
        while True:
            if not context_required and not error:
                k = get_next_key(data)

            display(data[k]) if context_required else display(k, True)
            context_required = False
            error = False

            inp = raw_input('a/s/d/f: ').lower()
            if inp == 'a':
                data = mark_as_known(data, k, KNOWN_WORD_MARKER)
            elif inp == 's':
                data = unmark(data, k, KNOWN_WORD_MARKER)
                os.system('open dict://{}'.format(k.split()[0]))
            elif inp == 'd':
                context_required = True
            elif inp == 'f':
                display_all_words(data)
            else:
                display('[Error] Invalid command!\n', True)
                error = True

    except KeyboardInterrupt:
        pass
    finally:
        write(fp, data)

if __name__ == '__main__':
    main()
