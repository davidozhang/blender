import random

from display import Display
from search import Search

KNOWN_WORD_MARKER = '#'


class Db(object):
    def __init__(self, lines):
        self.data = {}
        self.known_word_count = 0
        self.total_word_count = 0
        self.error_lines = []

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
                key = Db.mark_key_as_known(key)

            self.total_word_count += 1
            self.data[key.lower()] = line

    def get_data(self):
        return self.data

    def get_error_lines(self):
        return self.error_lines

    def get_next_key_value(self):
        k = random.choice(self.data.keys())
        return (k, self.data[k])

    def get_known_word_count(self):
        return self.known_word_count

    def get_total_word_count(self):
        return self.total_word_count

    def mark(self, k):
        if k in self.data:
            words = self.data[k].split()
            if len(words) > 0 and words[0] == KNOWN_WORD_MARKER:
                return

            self.known_word_count += 1
            self.data[Db.mark_key_as_known(k)] = '{} {}'.format(KNOWN_WORD_MARKER, self.data[k])
            self.data.pop(k)

    def unmark(self, k):
        if k in self.data:
            words = self.data[k].split()
            if len(words) > 0 and words[0] == KNOWN_WORD_MARKER:
                self.known_word_count -= 1
                self.data[Db.strip_key(k)] = ' '.join(words[1:])
                self.data.pop(k)

    @staticmethod
    def mark_key_as_known(k):
        return k + ' ' + Display.thumbs_up_emoji()

    @staticmethod
    def strip_key(k):
        return k.split()[0]
