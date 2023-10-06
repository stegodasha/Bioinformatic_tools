def filter_dna(seqs: dict, gc_bounds=0, length_bounds=0, quality_threshold=0):
    seqs_qualities = list(seqs.values())
    sequences = []
    qualities = []
    for sequence in range(len(seqs_qualities)):
        sequences.append(seqs_qualities[sequence][0])
    for quality in range(len(seqs_qualities)):
        qualities.append(seqs_qualities[quality][1])
    pass


def gc_count_filter(sequences: list, gc_bounds=(0, 100)):
    gc = []
    gc_answer = []
    for sequence in range(len(sequences)):
        gc.append((sequences[sequence].upper().count('G') + sequences[sequence].upper().count('C')) / len(
            sequences[sequence]) * 100)
    print(gc)
    for gc_content in gc:
        if gc_bounds[0] < gc_content < gc_bounds[1]:
            gc_answer.append(True)
        else:
            gc_answer.append(False)
    return gc_answer
    print(gc)


def length_filter(sequences, length_bounds=(0, 1000)):
    length_sequences = []
    length_sequences_answer = []
    for sequence in range(len(sequences)):
        length_sequences.append(len(sequences[sequence]))
    for length in length_sequences:
        if length_bounds[0] < length < length_bounds[1]:
            length_sequences_answer.append(True)
        else:
            length_sequences_answer.append(False)
    return length_sequences_answer


def quality_threshold_filter(qualities, quality_threshold=0):
    quality_answers = []
    for quality in qualities:
        summ_qualities = 0
        for symbol in range(len(quality)):
            letter = ord(quality[symbol]) - 33
            summ_qualities += letter
        avg_quality = summ_qualities / len(quality)
        print(avg_quality)
        if avg_quality > quality_threshold :
            quality_answers.append(True)
        else:
            quality_answers.append(False)
    return quality_answers


    # print(qualities)
    # print(sequences)
    # print(seqs_qualities)
    # sequence = seqs_name[0:len(seqs_name)-1]


EXAMPLE_FASTQ = {
    # 'name' : ('sequence', 'quality')
    '@SRX079804:1:SRR292678:1:1101:21885:21885': (
        'ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA',
        'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'),
    '@SRX079804:1:SRR292678:1:1101:24563:24563': (
        'ATTAGCGAGGAGGAGTGCTGAGAAGATGTCGCCTACGCCGTTGAAATTCCCTTCAATCAGGGGGTACTGGAGGATACGAGTTTGTGTG',
        'BFFFFFFFB@B@A<@D>BDDACDDDEBEDEFFFBFFFEFFDFFF=CC@DDFD8FFFFFFF8/+.2,@7<<:?B/:<><-><@.A*C>D'),
    '@SRX079804:1:SRR292678:1:1101:30161:30161': (
        'GAACGACAGCAGCTCCTGCATAACCGCGTCCTTCTTCTTTAGCGTTGTGCAAAGCATGTTTTGTATTACGGGCATCTCGAGCGAATC',
        'DFFFEGDGGGGFGGEDCCDCEFFFFCCCCCB>CEBFGFBGGG?DE=:6@=>A<A>D?D8DCEE:>EEABE5D@5:DDCA;EEE-DCD'),
    '@SRX079804:1:SRR292678:1:1101:47176:47176': (
        'TGAAGCGTCGATAGAAGTTAGCAAACCCGCGGAACTTCCGTACATCAGACACATTCCGGGGGGTGGGCCAATCCATGATGCCTTTG',
        'FF@FFBEEEEFFEFFD@EDEFFB=DFEEFFFE8FFE8EEDBFDFEEBE+E<C<C@FFFFF;;338<??D:@=DD:8DDDD@EE?EB'),
    '@SRX079804:1:SRR292678:1:1101:149302:149302': (
        'TAGGGTTGTATTTGCAGATCCATGGCATGCCAAAAAGAACATCGTCCCGTCCAATATCTGCAACATACCAGTTGGTTGGTA',
        '@;CBA=:@;@DBDCDEEE/EEEEEEF@>FBEEB=EFA>EEBD=DAEEEEB9)99>B99BC)@,@<9CDD=C,5;B::?@;A'),
    '@SRX079804:1:SRR292678:1:1101:170868:170868': (
        'CTGCCGAGACTGTTCTCAGACATGGAAAGCTCGATTCGCATACACTCGCTGAGTAAGAGAGTCACACCAAATCACAGATT',
        'E;FFFEGFGIGGFBG;C6D<@C7CDGFEFGFHDFEHHHBBHHFDFEFBAEEEEDE@A2=DA:??C3<BCA7@DCDEG*EB'),
    '@SRX079804:1:SRR292678:1:1101:171075:171075': (
        'CATTATAGTAATACGGAAGATGACTTGCTGTTATCATTACAGCTCCATCGCATGAATAATTCTCTAATATAGTTGTCAT',
        'HGHHHHGFHHHHFHHEHHHHFGEHFGFGGGHHEEGHHEEHBHHFGDDECEGGGEFGF<FGGIIGEBGDFFFGFFGGFGF'),
    '@SRX079804:1:SRR292678:1:1101:175500:175500': (
        'GACGCCGTGGCTGCACTATTTGAGGCACCTGTCCTCGAAGGGAAGTTCATCTCGACGCGTGTCACTATGACATGAATG',
        'GGGGGFFCFEEEFFDGFBGGGA5DG@5DDCBDDE=GFADDFF5BE49<<<BDD?CE<A<8:59;@C.C9CECBAC=DE'),
    '@SRX079804:1:SRR292678:1:1101:190136:190136': (
        'GAACCTTCTTTAATTTATCTAGAGCCCAAATTTTAGTCAATCTATCAACTAAAATACCTACTGCTACTACAAGTATT',
        'DACD@BEECEDE.BEDDDDD,>:@>EEBEEHEFEHHFFHH?FGBGFBBD77B;;C?FFFFGGFED.BBABBG@DBBE'),
    '@SRX079804:1:SRR292678:1:1101:190845:190845': (
        'CCTCAGCGTGGATTGCCGCTCATGCAGGAGCAGATAATCCCTTCGCCATCCCATTAAGCGCCGTTGTCGGTATTCC',
        'FF@FFCFEECEBEC@@BBBBDFBBFFDFFEFFEB8FFFFFFFFEFCEB/>BBA@AFFFEEEEECE;ACD@DBBEEE'),
    '@SRX079804:1:SRR292678:1:1101:198993:198993': (
        'AGTTATTTATGCATCATTCTCATGTATGAGCCAACAAGATAGTACAAGTTTTATTGCTATGAGTTCAGTACAACA',
        '<<<=;@B??@<>@><48876EADEG6B<A@*;398@.=BB<7:>.BB@.?+98204<:<>@?A=@EFEFFFEEFB'),
    '@SRX079804:1:SRR292678:1:1101:204480:204480': (
        'AGTGAGACACCCCTGAACATTCCTAGTAAGACATCTTTGAATATTACTAGTTAGCCACACTTTAAAATGACCCG',
        '<98;<@@@:@CD@BCCDD=DBBCEBBAAA@9???@BCDBCGF=GEGDFGDBEEEEEFFFF=EDEE=DCD@@BBC')
}
# filter_dna(EXAMPLE_FASTQ)
#print(length_filter(['ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA',
                    # 'ATTAGCGAGGAGGAGTGCTGAGAAGATGTCGCCTACGCCGTTGAAATTCCCTTCAATCAGGGGGTACTGGAGGATACGAGTTTGTGTG']))
#print(ord('A'))

print(quality_threshold_filter(['<<<=;@B??@<>@><48876EADEG6B<A@*;398@.=BB<7:>.BB@.?+98204<:<>@?A=@EFEFFFEEFB', '<98;<@@@:@CD@BCCDD=DBBCEBBAAA@9???@BCDBCGF=GEGDFGDBEEEEEFFFF=EDEE=DCD@@BBC','1']))