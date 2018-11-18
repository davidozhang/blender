class FileIO:
    '''
    Given a file path, reads the content into a list of strings.
    '''
    @staticmethod
    def read(fp):
        lines = []
        with open(fp, 'r') as f:
            lines = f.read().splitlines()
        return lines

    '''
    Given a file path, reads the content into a list of strings if the file path exists.
    Otherwise, returns [].
    '''
    @staticmethod
    def read_optional(fp):
        try:
            return FileIO.read(fp)
        except IOError:
            return []

    '''
    Given a file path and dictionary, writes the content of the dictionary to the file.
    '''
    @staticmethod
    def write_db(fp, db):
        written = 0
        l = len(db.keys())
        with open(fp, 'w') as f:
            for k in sorted(db.keys()):
                if written == l - 1:
                    f.write(db[k] + '\n')
                else:
                    f.write(db[k] + '\n\n')
                written += 1

    '''
    Given a file path and list of associations, writes the content of the associations to the file.
    '''
    @staticmethod
    def write_associations(fp, associations):
        l = len(associations)
        if l == 0:
            return

        with open(fp, 'w') as f:
            for a in associations:
                l = len(a)
                written = 0
                for word in sorted(a):
                    if written == l -1:
                        f.write(word)
                    else:
                        f.write(word + ' ')
                f.write('\n')
