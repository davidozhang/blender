class WordAssociation(object):
    def __init__(self, lines=[]):
        self.groups = []
        self.num_groups = 0

        for line in lines:
            self.create_group(line.split())

    def associate(self, w, words):
        group_existing = False
        for word in words:
            for i in xrange(self.num_groups):
                if word in self.groups[i] or w in self.groups[i]:
                    group_existing = True
                    self.groups[i].add(word)
                    self.groups[i].add(w)
        if len(words) > 0 and not group_existing:
            words.append(w)
            self.create_group(words)

    def create_group(self, words):
        self.groups.append(set(words))
        self.num_groups += 1

    def get_num_groups(self):
        return self.num_groups

    def get_groups(self):
        return self.groups
