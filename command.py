from enum import Enum


'''
A class that encodes all the available commands in Blender.
'''
class Command(Enum):
    KNOW_IT = 1
    SKIP = 2
    OPEN_DICTIONARY = 3
    SHOW_CONTEXT = 4
    DISPLAY_ALL_WORDS = 5
    ASSOCIATE = 6
    DISPLAY_ASSOCIATED_WORDS = 7
    DISPLAY_ALL_ASSOCIATIONS = 8
    UNKNOWN = 9
    CONFLICTING = 10
