import emoji

from emoji_mapper import EmojiMapper
from emoji_types import EmojiTypes
from input_mapper import InputMapper
from search import Search


class Display:
    '''
    Given a list of strings, wraps the content neatly within a box consisting of asterisks.
    '''
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

    '''
    Given a string, returns it bolded.
    '''
    @staticmethod
    def bold_replace(s):
        return '\033[1m' + s + '\033[0m'

    '''
    Given a string, this will display it, with the exception of bolding a keyword if it is found within asterisks.
    Alternatively, if all_bold is set to true, the entire string will be bolded.
    '''
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
        else:
            print line

    '''
    Retuns a string that encodes word count info
    '''
    @staticmethod
    def get_number_of_words_string(twc, kwc):
        return 'Number of words: {} ({} known/{} unknown)'.format(
            str(twc),
            kwc,
            str(twc - kwc)
        )

    '''
    Returns the display header that is shown upon starting Blender.
    '''
    @staticmethod
    def display_header(twc, kwc):
        header_list = [
            'Blender - Word flashcard generator',
            Display.get_number_of_words_string(twc, kwc),
            'A word that you already know is marked with a ' + EmojiMapper.get(EmojiTypes.THUMBS_UP),
            'If word associations exist for the word, it will be marked with a ' + EmojiMapper.get(EmojiTypes.EYES),
            'Keyboard shortcuts: ',
        ]

        for desc in InputMapper.get_descriptions():
            header_list.append(desc)

        Display.wrap(header_list)

    '''
    Displays all words, wrapped with starting and ending indicator blocks.
    '''
    @staticmethod
    def display_all_words(d, twc, kwc):
        Display.wrap([
            'Start of display',
            Display.get_number_of_words_string(twc, kwc)
        ])
        for k in sorted(d.keys()):
            Display.display(k, True)
        Display.wrap([
            'End of display',
            Display.get_number_of_words_string(twc, kwc)
        ])

    '''
    Displays all associations, wrapping with starting and ending indicator blocks.
    '''
    @staticmethod
    def display_all_associations(associations, num_associations):
        Display.wrap([
            'Start of display',
            'Number of word associations: {}'.format(num_associations)
        ])
        for i, association in enumerate(associations):
            Display.display('Association #{}'.format(i+1), True)
            Display.display(' '.join(sorted(list(association))))
            if i < num_associations - 1:
                Display.new_line()
        Display.wrap([
            'End of display'
        ])

    '''
    Displays associated words for a word.
    '''
    @staticmethod
    def display_associated_words(words):
        if len(words) == 0:
            Display.info('No associated words found. Consider adding some associations?')
        else:
            Display.display(' '.join(sorted(words)))

    '''
    Returns the prompt for adding an association
    '''
    @staticmethod
    def get_association_prompt(word):
        return 'Enter words to associate {} with, separated by space: '.format(Display.bold_replace(word))

    '''
    Given a string, wraps it within an error log.
    '''
    @staticmethod
    def error(s):
        Display.display('[Error] {}'.format(s), True)

    '''
    Given a string, wraps it within an info log.
    '''
    @staticmethod
    def info(s):
        Display.display('[Info] {}'.format(s))

    '''
    Very extra method.
    '''
    @staticmethod
    def new_line():
        Display.display('')
