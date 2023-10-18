def convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta: str):
    """
        A function that makes one of several fasta sequences

        Arguments:
        - input_fasta (str): the path to fasta file
        - output_fasta (str): the path to the new output fasta file

        Return:
        - File with combined sequences
        """
    with open(input_fasta) as fasta_file, open(output_fasta + '.fasta', 'w') as output_file:
        lines_new = []
        for line in fasta_file:
            if line.startswith('>'):
                continue
            else:
                line = line.strip('')
                lines_new.append(line)
        print(lines_new)
        return output_file.write("\n".join(lines_new))


def select_genes_from_gbk_to_fasta (input_gbk: str, genes: list[str], output_fasta: str, n_before: int = 1,
                                    n_after: int = 1):
    """
    A function that searches for neighboring genes with a user-defined gene

        Arguments:
        - input_gbk (str): the path to gbk file
        - output_fasta (str): the path to the new output fasta file
        - genes (list(str)): list with users genes
        - n_before (int): number of genes up to
        - n_after (int): number of genes after

        Return:
        - A file with the genes located next to the user's genes
    """
    with open(input_gbk) as gbk_file, open (output_fasta + '.fasta', 'w') as fasta_file:
        lines = gbk_file.readlines()
        for line in range(len(lines)):
            lines[line] = lines[line][0:len(lines[line])-2]

        gene_list = []
        trans_list = []
        transgene_list = []
        for line in range(len(lines)):
            if lines[line].find('/gene=') != -1 :
                gene_list.append(line)
                transgene_list.append(line)
            if lines[line].find('/translation=') != -1:
                trans_list.append(line)
                transgene_list.append(line)

        list_res = []
        sub_res = []
        for word in genes:
            for genline in gene_list:
                if lines[genline].find(word) != -1:
                    for i in range(n_before):
                        list_res.append(''.join(lines[trans_list[gene_list.index(genline)]-n_before+1:genline-n_before]))
                    for i in range(n_after):
                        list_res.append(''.join(lines[trans_list[gene_list.index(genline)+n_after+1]:gene_list[gene_list.index(genline)+n_after+1]-1]))
