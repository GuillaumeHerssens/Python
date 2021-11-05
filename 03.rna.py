

def to_rna(strand):
    strand = strand.upper()
    rna = {"A": "U", "T": "A", "C": "G", "G": "C"}
    for o, r in rna.items():
        strand = strand.replace(o, r)
    print (strand)


to_rna("gccccagcaatccaagtata")