"""
Read and write [fasta format](http://blast.ncbi.nlm.nih.gov/blastcgihelp.shtml)
"""
from itertools import groupby


class FastaReader(object):
    """
    Read fasta files into tuples (header, seq).
    """
    def __init__(self, file):
        """
        Args:
            file: The fasta file. Can either be a name or a handle.

        """

        if not hasattr(file, 'read'):
            self.file = open(file, 'r')
        else:
            self.file = file

    def get_entries(self):
        """
        Get the next Entry from the fasta file.

        Returns:
            Generator, which yields (header, sequence) tuples

        """
        for isheader, group in groupby(self.file, lambda line: line[0] == ">"):
            if isheader:
                header = next(group)[1:]
            else:
                seq = "".join(line.strip() for line in group)
                yield header, seq

    def close(self):
        """Close file handle"""
        self.file.close()


class FastaWriter(object):
    """
    Write fasta files from tuples (header, seq)
    """
    SPLIT = 80

    def __init__(self, file, split = SPLIT):
        """
        Args:
            file: The output fasta file. Can either be a (writeable) file handle or a path
            split: specifies after how many characters a sequence line will be wrapped.

        """
        self.split = split
        if not hasattr(file, 'write'):
            self.file = open(file, 'w')
        else:
            self.file = file

    def write_entry(self, header, sequence):
        """
        Write Entry to File

        Args:
            header: >sequence_header (without >)
            sequence: ACTGATT...
        """
        sequence = [sequence[i:i+self.split] for i in range(0, len(sequence), self.split)]
        self.file.write(">{0}\n".format(header))
        for s in sequence:
            self.file.write(s + "\n")

    def flush(self):
        self.file.flush()

    def close(self):
        """Close file handle"""
        self.file.close()

