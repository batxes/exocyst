# Exocyst and COG 3D modeling

## requirements:
IMP 


-- exocyst

Tag modeling:
create output directory
1 - mkdir output
generate 10000 models
2 - runIMP_exocystTags.pl 10000 0 output
get the RMSD matrix from the best models
3 - evalbstmdl_exocyst.pl output_tags


Protein modeling:
generate excyst models from. We need one cluster from the RMSD matrix
1 - runIMP_exocyst.pl tag_matrix_from_MeV number_of_iterations
evaluate and get best models
2 - supbestmdl_exocyst.pl  ---> needs to be fixed, modified for the COG

----
to generate a superposition and get std-dev of best tag models 
1 - analcluster.pl 
