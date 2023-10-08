def transcribe(dna_rna: str) -> list[str]:
    """
    Translates a dna sequence into rna

    Arguments:
    - dna_rna (str): an arbitrary number of arguments with RNA sequences

    Return:
    - the line with the result of the operation
    """
    rna = []
    for nucleotides in range(len(dna_rna)):
        rna += [dna_rna[nucleotides].replace('T', 'U').replace('t', 'u')]
    if len(dna_rna) > 1:
        return rna
    else:
        return rna[0]


def reverse(dna_rna: str) -> list[str]:
    """
    Returns an inverted sequence

    Arguments:
    - dna_rna (str): an arbitrary number of arguments with RNA sequences

    Return:
    - the line with the result of the operation
    """
    reverse_nucleic_acid = []
    for i in range(len(dna_rna)):
        reverse_nucleic_acid += [dna_rna[i][::-1]]
    if len(dna_rna) > 1:
        return reverse_nucleic_acid
    else:
        return reverse_nucleic_acid[0]


def complement(dna_rna: str) -> list[str]:
    """
    Returns a complementary sequence

    Arguments:
    - dna_rna (str): an arbitrary number of arguments with RNA sequences

    Return:
    - the line with the result of the operation
    """
    complement_nucleic_acid = []
    complement_rule = {'T': 'A', 'A': 'T', 'G': 'C',
                       'C': 'G', 'U': 'A', 't': 'a',
                       'g': 'c', 'c': 'g', 'u': 'a',
                       'a': 't'}
    replacer = complement_rule.get
    for i in range(len(dna_rna)):
        complement_nucleic_acid += [''.join([replacer(n, n) for n in dna_rna[i]])]
    if len(dna_rna) > 1:
        return complement_nucleic_acid
    else:
        return complement_nucleic_acid[0]


def reverse_complement(dna_rna: str) -> list[str]:
    """
    Returns a complementary sequence

    Arguments:
    - dna_rna (str): an arbitrary number of arguments with RNA sequences

    Return:
    - the line with the result of the operation
    """
    complement_nucleic_acid = []
    reverse_complement_nucleic_acid = []
    new_nucleotides = {'T': 'A', 'A': 'T', 'G': 'C',
                       'C': 'G', 'U': 'A', 't': 'a',
                       'g': 'c', 'c': 'g', 'u': 'a',
                       'a': 't'}
    replacer = new_nucleotides.get
    for nucleotides in range(len(dna_rna)):
        complement_nucleic_acid += [''.join([replacer(n, n) for n in dna_rna[nucleotides]])]
    for nucleotides in range(len(complement_nucleic_acid)):
        reverse_complement_nucleic_acid += [complement_nucleic_acid[nucleotides][::-1]]
    if len(dna_rna) > 1:
        return reverse_complement_nucleic_acid
    else:
        return reverse_complement_nucleic_acid[0]



