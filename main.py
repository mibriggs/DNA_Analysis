#Michael Briggs
#Mr. Sedlar
#CSII DNA Analysis
#11/17/2017

#This is the sample DNA
sample = ['GTA','GGG','CAC']


#Helps read the DNA
def read_dna(dna_file):
  dna_data = " "
  with open(dna_file) as f:
    data = f.read()
    for i in f:
      dna_data += i 
    return dna_data

#This helps us split the long string of DNA into 3 piece codons  
def dna_codons(dna):
  codons = []
  for i in range(0, len(dna), 3):
    if (i+3) < len(dna):
      codons.append(dna[i:i+3])
  return codons
  
#This helps us see if the DNA codons of the suspect matches the sample codons
def match_dna(dna):
  matches = 0
  for i in dna:
    if i in sample:
      matches += 1
  
  return matches

#This is to do the final part. To find out who the criminal is.  
def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print "You have %s matches. This means you're a suspect. The investigation must keep going" % (num_matches)
  else:
    print "You only have %s matches. You're free to go" % (num_matches)

is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")

