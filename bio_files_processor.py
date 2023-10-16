def convert_multiline_fasta_to_oneline(input_fasta=input('Please, enter file path:'),
                                       output_fasta=input('Please enter name for results')):
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

convert_multiline_fasta_to_oneline()