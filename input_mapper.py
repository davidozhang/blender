from command import Command

class InputMapper:
    mapping = {
        'a': Command.KNOW_IT,
        's': Command.NOT_QUITE_KNOW_IT,
        'c': Command.SHOW_CONTEXT,
        'd': Command.OPEN_DICTIONARY,
        'f': Command.DISPLAY_ALL_WORDS,
        'q': Command.ASSOCIATE,
        'w': Command.DISPLAY_ASSOCIATED_WORDS,
        'e': Command.DISPLAY_ALL_ASSOCIATIONS,
    }

    '''
    Given a user input containing commands, maps it to a list of Command enums.
    Checks for conflicting operations.
    '''
    @staticmethod
    def get_commands(inp):
        s = set()
        for w in inp:
            if w not in InputMapper.mapping:
                return [Command.UNKNOWN]
            s.add(InputMapper.mapping[w])

        if Command.KNOW_IT in s and Command.NOT_QUITE_KNOW_IT in s:
            return [Command.CONFLICTING]

        return list(s)

    '''
    Generates an input prompt using the input mapping keys.
    '''
    @staticmethod
    def get_main_prompt():
        return '/'.join(sorted(InputMapper.mapping.keys())) + ': '

    '''
    Generates input descriptions by transforming the Command enum names.
    '''
    @staticmethod
    def get_descriptions():
        l = sorted(InputMapper.mapping.keys())
        return [
            '{} - {}'.format(l[i], ' '.join(InputMapper.mapping[l[i]].name.lower().split('_'))) for i in xrange(len(l))
        ]
