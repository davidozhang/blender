import re

class Search:
    @staticmethod
    def search(line):
        return re.search('\*(.*)\*', line)
