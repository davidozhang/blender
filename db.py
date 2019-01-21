import random

from display import Display
from emoji_mapper import EmojiMapper
from emoji_types import EmojiTypes
from search import Search

KNOWN_WORD_MARKER = '#'


class Db(object):
    def __init__(self, lines):
        self.data = {}
        self.known_word_count = 0
        self.total_word_count = 0
        self.error_lines = []

        if len(lines) == 0:
            raise Exception('Empty sentences file provided')

        for line in lines:
            words = line.split()

            result = Search.search(line)
            if not result:
                if line:
                    self.error_lines.append(line)
                continue

            key = result.group(1)

            if len(words) > 0 and words[0] == KNOWN_WORD_MARKER:
                self.known_word_count += 1
                key = Db.mark_key(key, EmojiMapper.get(EmojiTypes.THUMBS_UP))

            self.total_word_count += 1
            self.data[key.lower()] = line

    '''
    Returns the underlying dictionary.
    '''
    def get_data(self):
        return self.data

    '''
    Returns the number of error lines.
    '''
    def get_error_lines(self):
        return self.error_lines

    '''
    Returns the next random key/value pair from the dictionary.
    '''
    def get_next_key_value(self):
        k = random.choice(self.data.keys())
        return (k, self.data[k])

    '''
    Returns the known word count.
    '''
    def get_known_word_count(self):
        return self.known_word_count

    '''
    Returns the total word count.
    '''
    def get_total_word_count(self):
        return self.total_word_count

    '''
    Marks a key as known by inserting a marker in both the key and value.
    '''
    def mark(self, k, marker):
        if k in self.data:
            words = self.data[k].split()
            if len(words) > 0 and words[0] == KNOWN_WORD_MARKER:
                return

            self.known_word_count += 1
            self.data[Db.mark_key(k, marker)] = '{} {}'.format(KNOWN_WORD_MARKER, self.data[k])
            self.data.pop(k)

    '''
    Unmarks a key as known by removing markers in both the key and value.
    '''
    def unmark(self, k):
        if k in self.data:
            words = self.data[k].split()
            if len(words) > 0 and words[0] == KNOWN_WORD_MARKER:
                self.known_word_count -= 1
                self.data[Db.strip_key(k)] = ' '.join(words[1:])
                self.data.pop(k)

    '''
    Given a string key, marks it as known by adding a marker.
    '''
    @staticmethod
    def mark_key(k, marker):
        if marker in k:
            return k
        return k + ' ' + marker

    '''
    Given a string key, removes the trailing markers.
    '''
    @staticmethod
    def strip_key(k):
        return k.split()[0]
