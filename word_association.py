class WordAssociation(object):
    def __init__(self, lines=[]):
        self.associations = []    # stores all word associations as sets
        self.lookup = {}    # word -> set of indices in self.associations that contain the word
        self.num_associations = 0

        for line in lines:
            self.__create_association(line.split())

    '''
    Given a list of words, adds all the words to existing associations keyed by 1 or more of the words.
    Otherwise, creates a new association and adds all the words to it.
    '''
    def associate(self, words):
        indices = []

        for word in words:
            # Add all words to existing associations if possible
            if len(self.__lookup_indices(word)) > 0:
                indices += self.__lookup_indices(word)

        # If no associations exist for these words, we create a new association
        if len(indices) == 0:
            indices = self.__create_association(words)

        for word in words:
            for index in indices:
                self.associations[index].add(word)
            self.__update_lookup_indices(word, indices)

    '''
    Given a word, returns all the words that are associated to the word.
    Otherwise, it returns [] if the word does not have any associations.
    '''
    def get_associations_for_word(self, word):
        result = set()
        indices = self.__lookup_indices(word)
        for index in indices:
            association = self.associations[index]
            for word in association:
                result.add(word)
        return list(result)

    def get_num_associations(self):
        return self.num_associations

    def get_all_associations(self):
        return self.associations

    '''
    Given a list of words, creates an association and returns its index as a list.
    '''
    def __create_association(self, words):
        self.associations.append(set(words))
        self.num_associations += 1

        indices = [self.num_associations - 1]
        for word in words:
            self.__update_lookup_indices(word, indices)
        return indices

    '''
    Given a key and list of indices, updates the lookup entry for the key with the new indices.
    '''
    def __update_lookup_indices(self, k, indices):
        if k in self.lookup:
            for index in indices:
                self.lookup[k].add(index)
        else:
            self.lookup[k] = set(indices)

    '''
    Given a key, return the indices that belong to the key.
    Otherwise, returns [] if the key does not exist.
    '''
    def __lookup_indices(self, k):
        return list(self.lookup[k]) if k in self.lookup else []
