def convert_multiline_fasta_to_oneline(input_fasta,output_fasta):
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

#C:\Users\Ярослав\Downloads\example_multiline_fasta.fasta

def select_genes_from_gbk_to_fasta (input_gbk, genes, output_fasta: object, n_before = 1, n_after = 1):
    """
    :type output_fasta: object
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









select_genes_from_gbk_to_fasta("C:\\Users\Ярослав\Downloads\example_gbk.gbk", genes=["pxpB"], output_fasta= 'sdfa')
# "C:\Users\Ярослав\Downloads\example_gbk.gbk"