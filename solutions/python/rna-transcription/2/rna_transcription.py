def to_rna(dna_strand):

    result = ""

    for ch in dna_strand:
        if ch == "G":
            result += "C"
        elif ch == "C":
            result += "G"
        elif ch == "T":
            result += "A"
        elif ch == "A":
            result += "U"

    return result