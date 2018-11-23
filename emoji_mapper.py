import emoji

from emoji_types import EmojiTypes


class EmojiMapper:
    mapping = {
        EmojiTypes.THUMBS_UP: ':thumbs_up:',
        EmojiTypes.EYES: ':eyes:',
    }

    @staticmethod
    def get(emoji_type):
        if emoji_type not in EmojiMapper.mapping:
            return None
        return emoji.emojize(EmojiMapper.mapping[emoji_type])
