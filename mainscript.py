import pandas as PS
from Bio import Entrez
from Bio import ExPASy
from Bio import SeqIO
from Bio.Align import Alignment
from Bio.Data import CodonTable
from Bio.Seq import MutableSeq
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import gc_fraction


# === FILE PARSING === #
ii=0
for i in SeqIO.parse("seq.fasta", "fasta"):   # for every record in the file...
    ii=ii+1
    print("=== SEQUENCE N°"+str(ii)+" ===")
    print("- ID: "+i.id)   # ...shows its id
    print("- name: "+i.name)   # ...shows its name
    print("- description: "+i.description)   # ...shows its description
    print("- sequence: "+i.seq)   # ...shows its sequence

    # === DNA/RNA SEQUENCE ANALYSIS === #

    # === TRANSCRIPTION/TRANSLATION === #
    print("")   # (separator)
    print("- transcribed sequence: "+i.seq.transcribe())   # ...shows its corresponding mRNA
    print("")   # (separator)
    print("- translated sequence: "+i.seq.translate())   # ...shows its corresponding proteic sequence

    # === GC-CONTENT === #
    print("")   # (separator)
    print("- C/G content (on 1): "+str(gc_fraction(i.seq)))   # ...shows its C/G content

    # === ALIGNMENT === #

    # === BASIC SEQUENCE STATISTICS === #

    # === CSV/JSON REPORTING === #
