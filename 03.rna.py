def to_rna(strand):
    strand = strand.lower()
    rna = {"a": "U", "t": "A", "c": "G", "g": "C"}
    for o, r in rna.items():
        strand = strand.replace(o, r)
    print (strand)

strand = "gccccagcaatccaagtata"
to_rna(strand)
