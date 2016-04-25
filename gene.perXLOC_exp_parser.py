# This code was written to work with self-generated gene.perXLOC_exp files (in /home/msxakk/Desktop/day5_analysis1_cuffnorm_work filder). It reads the gene names in the second column and does the following: splits genes into seperate rows if they happen to occur in the same raw sepearated by (,) and assigns the same expression values per each sepearated gene (as the same XLOC ids) while the rest of raws are just outputed. The programme ignores newly discovered genes. This code does NOT identify genes that occur multiple times.

fname = raw_input("Enter input file name (if in local dir) or path:"'\n')

try:
    fh = open(fname)
except:
    print 'The input file ' + fname + ' does not exist DONE'
    exit()

output = raw_input("Enter output file name (if in local dir) or path" + '\n' + "WARNING:Any existing data will be erased: "'\n')
try:
    oh = open(output, "w")
except:
    'The output file ' + output + 'does not exist. DONE'
 
for line in fh:
    line = line.rstrip()
    line = line.split()
    if line[1].startswith('gene'):
        oh.write('NAME' + '       ' + line[2] + '       ' + line[3] + '       ' + line[4] + '\n')
        continue
    elif line[1].startswith('"'):
        line[1] = line[1].lstrip('"')
        line[1] = line[1].rstrip('"')
        genes = line[1].split(',')
        for gene in genes:
            #print gene+ '       ' + line[2]+ '       ' + line[3]+ '       ' + line[4] + '\n'
            oh.write(gene+ '       ' + line[2]+ '       ' + line[3]+ '       ' + line[4] + '\n') 
    elif line[1].startswith('-'):  
        continue 
    else:
        #print line[1] + '       ' + line[2] + '       ' + line[3] + '       ' + line[4]
        oh.write(line[1] + '       ' + line[2] + '       ' + line[3] + '       ' + line[4] + '\n')
print 'DONE'

