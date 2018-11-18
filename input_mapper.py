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

    @staticmethod
    def get_main_prompt():
        return '/'.join(sorted(InputMapper.mapping.keys())) + ': '

    @staticmethod
    def get_descriptions():
        l = sorted(InputMapper.mapping.keys())
        return [
            '{} - {}'.format(l[i], ' '.join(InputMapper.mapping[l[i]].name.lower().split('_'))) for i in xrange(len(l))
        ]
