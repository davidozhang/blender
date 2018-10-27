import emoji

from search import Search

class Display:
    @staticmethod
    def wrap(l):
        border = ''
        max = 0
        for i in l:
            if len(i) > max:
                max = len(i)
        border += '*' * (max + 4)
        max += 4
        print '\n' + border
        for j in l:
            print '* '+j+' '*(max-1-len('* ' + j)) + '*'
        print border + '\n'

    @staticmethod
    def thumbs_up_emoji():
        return emoji.emojize(':thumbs_up:')

    @staticmethod
    def bold_replace(s):
        return '\033[1m' + s + '\033[0m'

    @staticmethod
    def display(line, all_bold=False):
        words = line.split()

        if all_bold:
            print Display.bold_replace(line)
            return

        result = Search.search(line)
        if result:
            actual = result.group(0)
            key = result.group(1)
            replace = Display.bold_replace(key)

            for i in xrange(len(words)):
                if words[i] == actual:
                    words[i] = replace

            print ' '.join(words)

    @staticmethod
    def display_header(twc, kwc):
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

    @staticmethod
    def display_all_words(d, twc, kwc):
        Display.wrap([
            'Start of display',
            'Number of words: {} ({} known/{} unknown)'.format(
                str(twc),
                kwc,
                str(twc - kwc)
            )
        ])
        for k in sorted(d.keys()):
            Display.display(k, True)
        Display.wrap(['End of display'])

    @staticmethod
    def error(s):
        Display.display('[Error] {}'.format(s), True)
