class WordAssociation(object):
    def __init__(self, lines=[]):
        self.groups = []    # stores all word groups as sets
        self.lookup = {}    # word -> set of indices in self.groups that contain the word
        self.num_groups = 0

        for line in lines:
            self.create_group(line.split())

    '''
    Given a list of words, adds all the words to existing groups keyed by 1 or more of the words. Otherwise,
    creates a new group and adds all the words to that group.
    '''
    def associate(self, words):
        indices = []

        for word in words:
            # Add all words to existing groups if possible
            if self.lookup_indices(word):
                indices += self.lookup_indices(word)

        # If no groups exist for these words, we create a new group
        if len(indices) == 0:
            indices = self.create_group(words)

        for word in words:
            for index in indices:
                self.groups[index].add(word)
            self.update_lookup_indices(word, indices)

    '''
    Given a list of words, creates a group and returns its index as a list.
    '''
    def create_group(self, words):
        self.groups.append(set(words))
        self.num_groups += 1

        indices = [self.num_groups - 1]
        for word in words:
            self.update_lookup_indices(word, indices)
        return indices

    '''
    Given a key and list of indices, updates the lookup entry for the key with the new indices.
    '''
    def update_lookup_indices(self, k, indices):
        if k in self.lookup:
            for index in indices:
                self.lookup[k].add(index)
        else:
            self.lookup[k] = set(indices)

    '''
    Given a key, return the indices that belong to the key, None if the key does not exist.
    '''
    def lookup_indices(self, k):
        return list(self.lookup[k]) if k in self.lookup else None

    def get_num_groups(self):
        return self.num_groups

    def get_groups(self):
        return self.groups
