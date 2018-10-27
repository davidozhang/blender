class FileIO:
    @staticmethod
    def read(fp):
        lines = []
        with open(fp, 'r') as f:
            lines = f.read().splitlines()
        return lines

    @staticmethod
    def write(fp, d):
        written = 0
        l = len(d.keys())
        with open(fp, 'w') as f:
            for k in sorted(d.keys()):
                if written == l - 1:
                    f.write(d[k] + '\n')
                else:
                    f.write(d[k] + '\n\n')
                written += 1
