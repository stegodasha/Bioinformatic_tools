def filter_dna(seqs: dict, gc_bounds: int = (0, 100), length_bounds: int = (0, 2**32),
               quality_threshold: int = 0) -> dict:
    """
    Filter fastq-sequences by parameters: gc_bounds, length_bounds and quality_threshold.

    Arguments:
    - seqs (dict): A dictionary where the key is the name of the sequence
                   and the value is a tuple of two strings: sequence and quality
    - gc_bounds (int): the GC interval of the composition (in percent) for filtering (by default is (0, 100)
    - length_bounds (int): length interval for filtering (default is (0, 2**32))
    - quality_threshold (int): the threshold value of the average quality of the read
                               for filtering (by default is 0)

    Return:
    - the source dictionary filtered by all parameters
    """
    seqs_qualities = list(seqs.values())
    seqs_keys = list(seqs.keys())

    sequences = []
    qualities = []

    for sequence in range(len(seqs_qualities)):
        sequences.append(seqs_qualities[sequence][0])
    for quality in range(len(seqs_qualities)):
        qualities.append(seqs_qualities[quality][1])

    gcf = gc_count_filter(sequences, gc_bounds)
    lf = length_filter(sequences, length_bounds)
    qtf = quality_threshold_filter(qualities, quality_threshold)

    for seq_counter in range(len(gcf)):
        if gcf[seq_counter] is False or lf[seq_counter] is False or qtf[seq_counter] is False:
            del seqs[seqs_keys[seq_counter]]

    return seqs


def gc_count_filter(sequences: list[str], gc_bounds: int) -> list[bool]:
    """
    Filter sequences by parameter gc_bounds.

    Arguments:
    - sequences (list[str]): list of sequences
    - gc_bounds (int): the GC interval of the composition (in percent) for filtering (by default is (0, 100)


    Return:
    - a list of boolean values, where true corresponds to the passage of the filtering element
      by parameter gc_bounds
    """
    gc = []
    gc_answer = []
    for sequence in range(len(sequences)):
        gc.append((sequences[sequence].upper().count('G') + sequences[sequence].upper().count('C')) / len(
            sequences[sequence]) * 100)

    for gc_content in gc:

        if type(gc_bounds) == int:
            if gc_content < gc_bounds:
                gc_answer.append(True)
            else:
                gc_answer.append(False)

        else:

            if gc_bounds[0] < gc_content < gc_bounds[1]:
                gc_answer.append(True)
            else:
                gc_answer.append(False)

    return gc_answer


def length_filter(sequences: list[str], length_bounds: int) -> list[bool]:
    """
        Filter sequences by parameter length_bounds

        Arguments:
        - sequences (list[str]): list of sequences
        - length_bounds (int): length interval for filtering (default is (0, 2**32))

        Return:
        - a list of boolean values, where true corresponds to the passage of the filtering element
          by parameter length_bounds
        """
    length_sequences = []
    length_sequences_answer = []

    for sequence in range(len(sequences)):
        length_sequences.append(len(sequences[sequence]))

    for length in length_sequences:
        if type(length_bounds) == int:

            if length < length_bounds:
                length_sequences_answer.append(True)
            else:
                length_sequences_answer.append(False)

        else:

            if length_bounds[0] < length < length_bounds[1]:
                length_sequences_answer.append(True)
            else:
                length_sequences_answer.append(False)

    return length_sequences_answer


def quality_threshold_filter(qualities: list[str], quality_threshold: int = 0) -> list[bool]:
    """
            Filter qualities by parameter quality_threshold

            Arguments:
            - qualities(list[str]): list of qualities
            - quality_threshold (int): the threshold value of the average quality of the read
                                       for filtering (by default is 0)

            Return:
            - a list of boolean values, where true corresponds to the passage of the filtering element
              by parameter quality_threshold
            """
    quality_answers = []

    for quality in qualities:
        summ_qualities = 0

        for symbol in range(len(quality)):
            letter = ord(quality[symbol]) - 33
            summ_qualities += letter
        avg_quality = summ_qualities / len(quality)
        if avg_quality > quality_threshold:
            quality_answers.append(True)
        else:
            quality_answers.append(False)

    return quality_answers
