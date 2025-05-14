def get_most_likely_ancestor_consensus(dna_string1, dna_string2):

    positions = []
    for position in range(len(dna_string1)):
        if dna_string1[position:position+len(dna_string2)] == dna_string2:
            positions.append(position+1)
    return tuple(positions)