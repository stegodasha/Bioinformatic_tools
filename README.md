# Bioinformatic_tools
> *This is the repo for the fifth homework of the BI Python 2023 course.
> It is a set of previously implemented programs. 
> There are only 3 functions in the main repository script: 
> the main function HW_3, the main function HW_4 and the main function HW_5.
> All other functions are imported in the main script, 
> they are  defined in the internal_functions folder.*
# HW_3. Functions 
> *This is the repo for the third homework of the BI Python 2023 course.*
> *Improvements have been added according to the comments*

### Program dna_rna_tools

dna_rna_tools is a utility for working with sequences of nucleic acids.

#### Basic functionality

Function `run_dna_rna_tools` accepts an arbitrary
number of arguments with DNA or RNA sequences (*str*) as input,
as well as the name of the procedure to be performed 
(for the correct operation of the program, always specify the desired procedure
with the last argument, *str*, see the usage example). 
After that, the command performs the specified action on all
the transmitted sequences. 
If one sequence is submitted, a string with the result is returned. 
If several are submitted, a list of strings is returned. 

**List of implemented functions:**

- `transcribe` — print the transcribed sequence
- `reverse` — print an inverted sequence
- `complement` — print a complementary sequence
- `reverse_complement` — print the reverse complementary sequence

**Usage example**

```python
run_dna_rna_tools('ATG', 'transcribe') # 'AUG'
run_dna_rna_tools('ATG', 'reverse') # 'GTA'
run_dna_rna_tools('AtG', 'complement') # 'TaC'
run_dna_rna_tools('ATg', 'reverse_complement') # 'cAT'
run_dna_rna_tools('ATG', 'aT', 'reverse') # ['GTA', 'Ta']
```

**Additional features**

- The program saves the case of characters (for example **complement AtGc** is **TaCg**)
- The program works  **only** with sequences of nucleic acids and checks the correctness of the entered sequence 
(for example, the sequence AUTGC cannot exist because it contains T and U).
- The program checks the input sequence and commands to it:
```python
run_dna_rna_tools('ATG') # 'Correct the input data: only 1 argument was received'
```
- Программа проверяет корректность ввода команды:
```python
run_dna_rna_tools('ATG','compliment') # 'Check the function name'
```


### Team

The task was individual, so I was the only member of the team: Daria Sokolova.
My contacts for communication: kalabanova_dasha@mail.ru


Thank you for your interest in my first program! ✨✨
# HW_4.Protein Info
> *This is the repo for the forth homework of the BI Python 2023 course.*
> *Improvements have been added according to the comments*
> 
This tool supports standard 20 amino acids. Any modifications of amino acids are not supported. You can write amino acids in any case (lower, upper or mixed). 
This project consists of one function "protein_analysis" that helps user to:
- predict molecular weight of amino acid (aa) sequences
- translate aa sequences from one-letter to three-letter code
- calculate total amount of each amino acid in the sequences
- make DNA based codon optimization for the introduced amino acid sequences with the support for 3 cell types: Esherichia coli, Pichia pastoris, Mouse
- calculate length of amino acid sequences
- count the number of atoms of each type in a sequence (brutto formula)  <br/>

Tool is coded with Python.

## How to use:
**protein_analysis**(**args, procedure, cell_type=None, letter_format=1*) <br/>
**Parametrs:**
> ***args** : **sequence of str** <br/>
> &nbsp;&nbsp;&nbsp;&nbsp;Any number of lines with amino acid sequences <br/>
    **procedure** : ***str*** <br/>
> &nbsp;&nbsp;&nbsp;&nbsp;The name of the operation you want to perform. The following types of procedures are supported: <br/>
>>  
>> - ***molecular_weight***: calculates predicted molecular weight of amino acid sequences in kDa
>> - ***one_letter_to_three***: translate aa sequences from one-letter to three-letter code
>> - ***get_amino_acid_sum***: calculates total amount of each amino acid in the sequences
>> - ***codon_optimization***: makes DNA based codon optimization for the introduced amino acid sequences, support 3 types of cells. Can only be used in conjunction with **cell_type**: `Esherichia coli`, `Pichia pastoris`, `Mouse`
>> - ***length***: calculates length of amino acid sequences 
>> - ***brutto_count***: counts the number of atoms of each type in a sequence
>> 
>    **cell_type** : ***str, defalut None*** <br/>
> &nbsp;&nbsp;&nbsp;&nbsp;The type of cells for which optimization is applied. Cell types supported:<br/>
>>
>> - `Esherichia coli` *or* `E.coli`
>> - `Pichia pastoris` *or* `P.pastoris`
>> - `Mouse` *or* `mouse`
>> 
>    **letter_format** : ***int, defalut 1*** <br/>
> &nbsp;&nbsp;&nbsp;&nbsp;Specifies the format for receiving amino acid sequences. Either one-letter (**letter_format** = 1) or three-letter sequences (**letter_format** = 3) <br/>
>

Call the "protein_analysis" funcion with following arguments.
Requred arguments:
- tuple of protein sequences written one letter or three letter code without stop codos. Please do not use sequences in different formats in the same function call!
- name of procedure as string (see list of precedures)
- format of code for the protein sequences as int: 1 for one letter, 3 for three letter code
Optional argument:
- cell type (required only for codon_optimization procedure). Accepted cell types Esherichia coli, Pichia pastoris, Mouse

## List of procedures:

- `molecular_weight` — returns list of float values, that indicate predicted molecular weights of given aa sequences (in kDa)
- `one_letter_to_three` — will return list of strings, containing the same sequences written in three-letter code
- `get_amino_acid_sum` — сounts the amount of each amino acid in the injected protein sequences
- `codon_optimization` — makes codon-optimized DNA based on the introduced amino acid sequences for 3 types of cells: Esherichia coli, Pichia pastoris, Mouse
- `length` — calculates length of amino acid sequences 
- `brutto_count` — counts the number of atoms of each type in a sequence
## Example of use:

```python
protein_analysis("ACD", "AD", procedure="one_letter_to_three", letter_format=1) # ['AlaCysAsp', 'AlaAsp']
protein_analysis("AlaAspLys", "AlaAsp", procedure="molecular_weight", letter_format=3) # [0.37, 0.22]
protein_analysis("ACD", "AD", procedure="get_amino_acid_sum") # [{'A': 1, 'C': 1, 'D': 1, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0, 'Y': 0},
                                                                        # {'A': 1, 'C': 0, 'D': 1, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0, 'Y': 0}]
protein_analysis("ACD", "AD", procedure="codon_optimization", cell_type = 'E.coli', letter_format=1) # ['GCGTGCGAT', 'GCGGAT']
protein_analysis("acDEFGHIKLMNPQRSTVwy", "ad", procedure="length", letter_format=1) # [20, 2]
protein_analysis("FGHIKLMNPQ", "PQRSTVwy", "adN", procedure="brutto_count", letter_format=1)
# [{'C': 54, 'H': 103, 'N': 15, 'O': 22, 'S': 1}, {'C': 48, 'H': 83, 'N': 23, 'O': 18, 'S': 3}, {'C': 11, 'H': 22, 'N': 4, 'O': 9, 'S': 0}]
```


## Input requirements and possible errors:
 - **It is important to indicate the type of operation. An error occurs when you enter an incorrect operation type**
```python
protein_analysis("FGHIKLMNPQ", "PQRSTVwy", "adN", procedure="brutto", letter_format=1)
# ValueError: Requested procedure is not defined
```
- **To perform the coden_optimization operation, you must enter cell_type (None by default). Otherwise an error message is displayed**
```python
protein_analysis('AlaCysAsp', 'AlaAsp', procedure="codon_optimization", cell_type='Rat', letter_format=3) 
# ValueError: Type Rat is not supported. The following types of organisms are available for codon optimization: Esherichia coli, Pichia pastoris, Mouse
```
 - **By default, entering amino acid sequences in a single-letter format in any case is supported. To enter in three-letter format in any case, you need to specify letter_format = 3. <br/> If an unknown format is entered, an error message is displayed.**
```python
protein_analysis("ACD", "AD", procedure="one_letter_to_three", cell_type='E.coli', letter_format=2)
# ValueError: Error unsupported letter_format. Only letter_formats 1 and 3 are supported
```
 - **If letter_format = 1 is specified, but all sequences are similar to the three-letter amino slot encoding, a notification will be displayed warning**
```python
protein_analysis("LYSlys", "HishisHis", procedure="get_amino_acid_sum", letter_format=1)
# Warning: all your sequences are similar to three-letter ones. Check the letter_format value
```
 - **If a single-letter amino acid input format is specified, but at least one amino acid slot is not standard or is written incorrectly, an error message is displayed**
```python
protein_analysis("BBB", procedure="get_amino_acid_sum", letter_format=1)
# ValueError: Error B is not an amino acid. Correct your input.
```
- **If a three-letter amino acid input format is specified, but at least one amino acid slot is not standard or is written incorrectly, an error message is displayed**
```python
protein_analysis("Al", procedure="get_amino_acid_sum", letter_format=3)
# ValueError: Error al is incorrect form of amino acid notation. Correct your input
protein_analysis("AluLysArg", procedure="get_amino_acid_sum", letter_format=3)
# ValueError: Error alu is not an amino acid. Correct your input
```

## Private policy and contacts
This tool can be freely distributed and used.
<br/>
If you have any suggestions for improving the tool or if you find a bug, please contact us by email.
<br/>
This tool was developed by the "workaholics" team:
<br/>
Yulia Volkova volkova.yulia.leonidovna@gmail.com
<br/>
Dasha Sokolova kalabanova_dasha@mail.ru
<br/>
Team leader: Ivan Kozin ivan.d.kozin@gmail.com
<br/>
Team photo:
![Снимок экрана 2023-09-29 210559_2](https://github.com/ivandkoz/HW4_Functions2_Kozin/assets/63678919/ad1302a1-d139-4c82-b7eb-d5b9ac1897e8)
## Personal contribution
`Ivan Kozin` (team leader) worte functions:
- length
- brutto_count
- is_amino_acid
- name_transform
- is_length_divisible_by_3
- is_amino_acid_three_letter
- managed work with guthub repository

`Dasha Sokolova` (co-leader) wrote functions: 
- get_amino_acid_sum
- codon_optimization functions
  
`Yulia Volkova` (co-leader) wrote functions:
- main (protein_analysis)
- molecular_weight
- one_letter_to_three functions
  
Writting README, debugging code and testing it has been done by the efforts of all team.
# HW_5. Work with fastq
> *This is the repo for the fifth homework of the BI Python 2023 course.*


### Program work_with_fastq

Work_with_fastq is a utility for filtering fastq-sequences 
by parameters: gc_bounds, length_bounds and quality_threshold.

**Basic functionality**

The main function `filter_dna`accepts 4 arguments as input: seqs, gc_bounds, length_bounds, quality_threshold:

- `seqs (dict)`: A dictionary where the key is the name of the sequence
                 and the value is a tuple of two strings: sequence and quality
- `gc_bounds (int)`: the GC interval of the composition (in percent) for filtering (by default is (0, 100)
- `length_bounds (int)`: length interval for filtering (default is (0, 2**32))
- `quality_threshold (int)`: the threshold value of the average quality of the read
                               for filtering (by default is 0)

**List of implemented functions:**

- `gc_count_filter` — filter sequences by parameter gc_bounds
- `length_filter` — filter sequences by parameter length_bounds
- `quality_threshold_filter` — filter qualities by parameter quality_threshold
- `read_file` — write a  fastq file as a dictionary
- `write_file` — record a dictionary filtered by parameters as a fastq file

**Usage example**

```python
EXAMPLE_FASTQ = {
    # 'name' : ('sequence', 'quality')
    '@SRX079804:1:SRR292678:1:1101:21885:21885': 
    ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA', 
     'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'),
    '@SRX079804:1:SRR292678:1:1101:24563:24563': 
    ('ATTAGCGAGGAGGAGTGCTGAGAAGATGTCGCCTACGCCGTTGAAATTCCCTTCAATCAGGGGGTACTGGAGGATACGAGTTTGTGTG', 
     'BFFFFFFFB@B@A<@D>BDDACDDDEBEDEFFFBFFFEFFDFFF=CC@DDFD8FFFFFFF8/+.2,@7<<:?B/:<><-><@.A*C>D')}

print(filter_dna(EXAMPLE_FASTQ, gc_bounds=60, length_bounds=100, quality_threshold=35))
filter_dna(EXAMPLE_FASTQ, gc_bounds=60, length_bounds=100, quality_threshold=35) 
# {'@SRX079804:1:SRR292678:1:1101:21885:21885': 
# ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA', 
# 'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD')}


```


### Team

The task was individual, so I was the only member of the team: Daria Sokolova.
My contacts for communication: kalabanova_dasha@mail.ru


Thank you for your interest in my program! ✨✨
# HW_6.Bio_files_processor
> *This is the repo for the sixth homework of the BI Python 2023 course.*

### Program work with fasta and gbk files

Bio_files_processor is a utility for the work with bioinformatics files 

**Basic functionality**

The function `convert_multiline_fasta_to_oneline`accepts 2 arguments as input: input_fasta, output_fasta:

- `input_fasta (str)`: the path to fasta file
- `output_fasta (str)`: the path to the new output fasta file

The function `select_genes_from_gbk_to_fasta`accepts 5 arguments as input: input_gbk, output_fasta, 
                                              genes, n_before, n_after:
- `input_gbk (str)`: the path to gbk file
- `output_fasta (str)`: the path to the new output fasta file
- `genes (list(str))`: list with users genes
- `n_before (int)`: number of genes up to
- `n_after (int)`: number of genes after

**List of implemented functions:**

- `convert_multiline_fasta_to_oneline` — makes one of several fasta sequences
- `select_genes_from_gbk_to_fasta` — searches for neighboring genes with a user-defined gene