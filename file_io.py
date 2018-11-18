class FileIO:
    @staticmethod
    def read(fp):
        lines = []
        with open(fp, 'r') as f:
            lines = f.read().splitlines()
        return lines

    @staticmethod
    def read_optional(fp):
        try:
            return FileIO.read(fp)
        except IOError:
            return []

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
