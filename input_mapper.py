from command import Command

class InputMapper:
    mapping = {
        'a': Command.KNOW_IT,
        's': Command.NOT_QUITE,
        'c': Command.SHOW_CONTEXT,
        'd': Command.OPEN_DICTIONARY,
        'f': Command.DISPLAY_ALL_WORDS,
    }

    @staticmethod
    def get_commands(inp):
        s = set()
        for w in inp:
            if w not in InputMapper.mapping:
                return [Command.UNKNOWN]
            s.add(InputMapper.mapping[w])

        if Command.KNOW_IT in s and Command.NOT_QUITE in s:
            return [Command.CONFLICTING]

        return list(s)

    @staticmethod
    def get_prompt():
        return '/'.join(sorted(InputMapper.mapping.keys())) + ': '

    @staticmethod
    def get_description():
        l = sorted(InputMapper.mapping.keys())
        return ', '.join([
            '{} - {}'.format(l[i], ' '.join(InputMapper.mapping[l[i]].name.lower().split('_'))) for i in xrange(len(l))
        ])
