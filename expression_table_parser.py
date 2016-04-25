# This program does the following:

# 1. It reads the file and creats a dictionary where gene_name is key while value is list. The lst[0] of the list is the gene count while subsequent items are expression values for genes in following order UT1 UT1 UT3 NC1 NC2 NC3 A1 A2 A3 C1 C2 C3 (if lst[0] is 1)
# 2. If gene occured 2 or more times (per single sample) in expression dataset, the programe is capable of creating sublists which are elements of the data list above. Each sublist contains the FPKMs per gene PER SAMPLE(!) and in the same order as above.
# 3. Sums the FPKMs within each substring to yield final single per gene FPKM per sample.
  
# Therefore the gene expression that will be laveraged for GSEA is the sum of all XLOC FPKMs values that belong to a gene. The decision was made to do the analysis this way since averaging would significantly skew the data, while picking up the maximum only may result in loss of significant data (depends on relative contributions of XLOCs for the gene expression). The shortcoming of doing analysis this way is that genes that had multiple XLOCs assigned may be overreprested due to that fact that the same reads are being counted additional times as the reads may contribute to the FPKMs of different XLOCs of the same id (depends if there is overlap). However this bias is going to be introduced in all the samples so hopefully it will be canceled out during GSEA.

# This output of this program has the following column format:
# gene_name UT1 UT1 UT3 NC1 NC2 NC3 A1 A2 A3 C1 C2 C3

def str_to_float(lst): #Function to convert a list of strings into floats if possible or else the original string returned. If '0' encountered it is converted to integer rather than float.
    for x in lst:
        try:
            if x == '0':
                x = int(x)
            else:
                x = float(x)
            yield x
        except ValueError:
            yield x    
#Split a list into roughly equal-sized pieces (Python recipe) 
#From http://code.activestate.com/recipes/425397/ 
def split_seq(seq, size):
    newseq = []
    splitsize = 1.0/size*len(seq)
    for i in range(size):
        newseq.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])
    return newseq
#Function to identify the sum of num within the splitted chunks (lists) generated from orginal lst.
def block_of_num_sum_returner(lst,chunk_num):
    lst = split_seq(lst,chunk_num)
    sumed_num_lst = list()
    for s in lst:
        sumed_num_lst.append(sum(s))
    return sumed_num_lst
         

fname = raw_input("Enter input file name (if in local dir) or path:"'\n')

try:
    fh = open(fname)
except:
    print 'The input file ' + fname + ' does not exist DONE'
    exit()

dct_map = dict()

for line in fh:
    if line.startswith('NAME'):
        continue
    line = line.rstrip()
    line = line.split()
    gene = line[0]
    if gene not in dct_map: #creats the dictionary where key is gene_name while value is list containing expression data. Redundant genes have multiple FPKMs nested together within the sample.
		dct_map[gene] = [1, line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12]] 
    else:
        dct_map[gene][0] = dct_map[gene][0] + 1
        dct_map[gene][1] = str(dct_map[gene][1]) + ' ' + line[1] 
        dct_map[gene][2] = str(dct_map[gene][2]) + ' ' +  line[2] 
        dct_map[gene][3] = str(dct_map[gene][3]) + ' ' +  line[3] 
        dct_map[gene][4] = str(dct_map[gene][4]) + ' ' +  line[4] 
        dct_map[gene][5] = str(dct_map[gene][5]) + ' ' +  line[5] 
        dct_map[gene][6] = str(dct_map[gene][6]) + ' ' +  line[6] 
        dct_map[gene][7] = str(dct_map[gene][7]) + ' ' +  line[7] 
        dct_map[gene][8] = str(dct_map[gene][8]) + ' ' +  line[8] 
        dct_map[gene][9] = str(dct_map[gene][9]) + ' ' +  line[9] 
        dct_map[gene][10] = str(dct_map[gene][10]) + ' ' +  line[10] 
        dct_map[gene][11] = str(dct_map[gene][11]) + ' ' +  line[11] 
        dct_map[gene][12] = str(dct_map[gene][12]) + ' ' +  line[12] 
    
    #print line[0], dct_map.get(line[0])

print 'FINISHED GENERATING DICTIONARY '


output = raw_input("ENTER initial output file name" + '\n' + "The file will be created in local dir. If the file exists then it will be overwitten!" + '\n')
oh = open(output, "w")



for gene,data in dct_map.items():	
    if data[0] == 1:
         oh.write(gene + ' ' + str(dct_map[gene][0]) + ' ' + dct_map[gene][1] + ' ' + dct_map[gene][2] + ' ' + dct_map[gene][3] + ' ' + dct_map[gene][4] + ' ' + dct_map[gene][5] + ' ' + dct_map[gene][6] + ' ' + dct_map[gene][7] + ' ' + dct_map[gene][8] + ' ' + dct_map[gene][9] + ' ' + dct_map[gene][10] + ' ' + dct_map[gene][11] + ' ' + dct_map[gene][12] + '\n')         
    else:
        #print type(gene)
        #print type(dct_map[gene][0])
        #print type(dct_map[gene][1]) 
        oh.write(gene + ' ' + str(dct_map[gene][0]) + ' ' + dct_map[gene][1] + ' ' + dct_map[gene][2] + ' ' + dct_map[gene][3] + ' ' + dct_map[gene][4] + ' ' + dct_map[gene][5] + ' ' + dct_map[gene][6] + ' ' + dct_map[gene][7] + ' ' + dct_map[gene][8] + ' ' + dct_map[gene][9] + ' ' + dct_map[gene][10] + ' ' + dct_map[gene][11] + ' ' + dct_map[gene][12] + '\n') 

print 'FINIFHED WRITING INITIAL OUTPUT FILE'

fh.close() #closing file handles
oh.close()

fh2 = open(output)

output2 = raw_input("ENTER FINAL OUTPUT file name" + '\n' + "The file will be created in local dir. If the file exists then it will be overwitten!" + '\n')
oh2 = open(output2, "w") #makes file handle in writing mode for final file output           
      
oh2.write('gene_name UT1 UT2 UT3 NC1 NC2 NC3 A1 A2 A3 C1 C2 C3''\n')



for generaw in fh2:
    generaw = generaw.rstrip()
    generaw = generaw.split()
    generaw = list(str_to_float(generaw)) #converts numeric strings into floats if possible
    if generaw[1] == 1:
        oh2.write(str(generaw[0]) + ' ' + str(generaw[2])+ ' ' +str(generaw[3])+ ' ' +str(generaw[4])+ ' ' +str(generaw[5])+ ' ' +str(generaw[6])+ ' ' +str(generaw[7])+ ' ' +str(generaw[8])+ ' ' +str(generaw[9])+ ' ' +str(generaw[10])+ ' ' +str(generaw[11])+ ' ' +str(generaw[12])+ ' ' +str(generaw[13])+ '\n')
    if generaw[1] > 1:
       generaw[2:] = block_of_num_sum_returner(generaw[2:],12)
       oh2.write(str(generaw[0]) + ' ' + str(generaw[2])+ ' ' +str(generaw[3])+ ' ' +str(generaw[4])+ ' ' +str(generaw[5])+ ' ' +str(generaw[6])+ ' ' +str(generaw[7])+ ' ' +str(generaw[8])+ ' ' +str(generaw[9])+ ' ' +str(generaw[10])+ ' ' +str(generaw[11])+ ' ' +str(generaw[12])+ ' ' +str(generaw[13])+ '\n')
