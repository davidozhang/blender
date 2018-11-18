import re

class Search:
    '''
    Given a string, returns the regex search result for string wrapped within asterisks.
    '''
    @staticmethod
    def search(line):
        return re.search('\*(.*)\*', line)
