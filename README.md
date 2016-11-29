

requirements:
IMP 


# exocyst

Tag modeling:
1 - mkdir output
1 - runIMP_exocystTags.pl 10000 0 output
#get the RMSD matrix
2 - evalbstmdl_exocyst.pl output_tags


Protein modeling:
1 - runIMP_exocyst.pl tag_matrix_from_MeV number_of_iterations
#evaluate and get best models
2 - supbestmdl_exocyst.pl  ---> needs to be fixed, modified for the COG

#to generate a superposition and get std-dev of best tag models 
analcluster.pl 
