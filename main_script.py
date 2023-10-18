from internal_functions.dna_rna_tools import complement
from internal_functions.dna_rna_tools import reverse
from internal_functions.dna_rna_tools import reverse_complement
from internal_functions.dna_rna_tools import transcribe
from internal_functions.protein_analysis_tool import brutto_count
from internal_functions.protein_analysis_tool import codon_optimization
from internal_functions.protein_analysis_tool import get_amino_acid_sum
from internal_functions.protein_analysis_tool import length
from internal_functions.protein_analysis_tool import molecular_weight
from internal_functions.protein_analysis_tool import name_transform
from internal_functions.protein_analysis_tool import one_letter_to_three
from internal_functions.work_with_fastq import gc_count_filter
from internal_functions.work_with_fastq import length_filter
from internal_functions.work_with_fastq import quality_threshold_filter
import os


def run_dna_rna_tools(*args: str) -> str:
    """
    run_dna_rna_tools is a utility for working with sequences of nucleic acids

    Arguments:
    - args (str): an arbitrary number of arguments with DNA or RNA sequences,
                      as well as the name of the procedure to be performed:
                      transcribe, reverse, complement, reverse_complement
    Return:
    - the line with the result of the operation
    """
    sequences, operation = args[0:-1], args[-1].lower()
    type_of_operation = {'transcribe': transcribe(sequences),
                         'reverse': reverse(sequences),
                         'complement': complement(sequences),
                         'reverse_complement': reverse_complement(sequences)}
    for sequence in sequences:
        for nucleotide in sequence:
            if 't' == nucleotide.lower() or 'u' == nucleotide.lower():
                raise ValueError('A nonexistent sequence has been introduced')
            else:
                return type_of_operation.get(operation)
    if len(args) < 2:
        raise ValueError('Correct the input data: only 1 argument was received')
    else:
        raise ValueError('Check the function name')


def protein_analysis(*args: str, procedure: str, cell_type: str = None, letter_format: int = 1) -> list:
    """
    Function protein_analysis:
    - calculates predicted molecular weight of amino acid sequences in kDa (procedure name: molecular_weight)
    - translate aa sequences from one-letter to three-letter code (procedure name: one_letter_to_three)
    - calculates total amount of each amino acid in the sequences (procedure name: get_amino_acid_sum)
    - makes DNA based codon optimization for the introduced amino acid sequences, support 3 types of cells:
      Esherichia coli, Pichia pastoris, Mouse (procedure name: codon_optimization)
    - calculates length of amino acid sequences (procedure name: length)
    - counts the number of atoms of each type in a sequence (procedure name: brutto_count)

    Arguments:
    - one or multiple string of protein sequences written one letter or three letter code (not mixed)
    - name of procedure as string
    - cell type (required only for codon_optimization procedure)
    - letter_format of code for the protein sequences as int: 1 for one letter, 3 for three letter code

    Return:
    - molecular_weight procedure returns list of floats
    - one_letter_to_three procedure returns list of strings
    - get_amino_acid_sum procedure returns list of dictionaries
    - codon_optimization procedure returns list of strings
    - length procedure returns list of int values
    - brutto_count procedure returns list of dictionaries with counts of atoms in the sequence
    """
    amino_acid_seqs = name_transform(args, letter_format)
    procedures = {
        "molecular_weight": molecular_weight,
        "one_letter_to_three": one_letter_to_three,
        "get_amino_acid_sum": get_amino_acid_sum,
        "codon_optimization": codon_optimization,
        "length": length,
        "brutto_count": brutto_count,
    }
    if procedure not in procedures.keys():
        raise ValueError("Requested procedure is not defined")
    elif procedure == "codon_optimization":
        return procedures.get(procedure)(amino_acid_seqs, cell_type)
    else:
        return procedures.get(procedure)(amino_acid_seqs)


def filter_dna(input_path: str = input('Please, enter file path:'),
               output_filename=input('Please enter name for results'),
               gc_bounds: int = (0, 100),
               length_bounds: int = (0, 2 ** 32),
               quality_threshold: int = 0):
    """
    Filter fastq-sequences by parameters: gc_bounds, length_bounds and quality_threshold.

    Arguments:
    - gc_bounds (int): the GC interval of the composition (in percent) for filtering (by default is (0, 100)
    - length_bounds (int): length interval for filtering (default is (0, 2**32))
    - quality_threshold (int): the threshold value of the average quality of the read
                               for filtering (by default is 0)

    Return:
    - the source dictionary filtered by all parameters
    """
    seqs = read_file(input_path)
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
    return write_file(output_filename, seqs)


def read_file(input_path: str) -> dict:
    """
    A function that writes a  fastq file as a dictionary

    Arguments:
    - input_path (str): the path to fastq file

    Return:
    - seqs (dict): A dictionary where the key is the name of the sequence
                   and the value is a tuple of two strings: sequence and quality
    """
    keys = []
    values = []
    values_final = []
    with open(input_path) as fastq_file:
        lines = fastq_file.readlines()
        for line in lines:
            if line.startswith('@SRX'):
                line = line.strip()
                keys.append(line)
            elif line.startswith('+SRX'):
                continue
            else:
                line = line.strip()
                values.append(line)
                # print(values)
                if len(values) == 2:
                    # print(True)
                    values_final.append(values[0:len(values)])
                    values.clear()
        # values.append(list_line)
    # values = list(map(str.split, values))
    seqs = dict(zip(keys, values_final))
    return seqs


def write_file(output_filename: str, seqs: dict):
    """
        A function that records a dictionary filtered by parameters as a fastq file

        Arguments:
        - output_filename (str): name for the new  fastq file
        - seqs (dict): A dictionary where the key is the name of the sequence
                       and the value is a tuple of two strings: sequence and quality

        Return:
        - File with filtered sequences
        """
    keylist = list(seqs.keys())
    vallist = list(seqs.values())
    if not os.path.isdir("fastq_filtrator_resuls"):
        os.mkdir("fastq_filtrator_resuls")
    os.chdir("fastq_filtrator_resuls")
    with open(output_filename + '.fastq', 'w') as output_file:
        for key_iter in range(len(keylist)):
            output_file.write(keylist[key_iter])
            output_file.write('\n')
            for value_iter in range(len(vallist[key_iter])):
                output_file.write(vallist[key_iter][value_iter])
                output_file.write('\n')
            return output_file
