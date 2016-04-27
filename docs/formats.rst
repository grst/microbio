File Formats (Input/Output)
===========================

.. automodule:: formats 

Fasta
-----

Reading fasta
~~~~~~~~~~~~~
is as easy as 

::

  r = FastaReader(file)
  for header, seq in r.get_entries():
      print header
      print seq

file can either be a path or a file object. 

.. autoclass:: fasta.FastaReader
    :members:

Writing fasta
~~~~~~~~~~~~~    

::

    w = FastaWriter(file, split=60)
    header = "some_random_nucleotides"
    seq = "ACTGACATT"
    w.write_entry(header, seq)
    w.close()

again, file can be a path of a file object. 
``split`` speficies, after how many characters a sequence will be wrapped in multiple lines. Default is 80.

.. automodule:: formats.fasta
    :members:

Fast5
-----
.. automodule:: formats.fast5 
    :members:


