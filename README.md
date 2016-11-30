#Exocyst and COG 3D modeling
These scripts were used to model the 3D architecture of the exocyst and COG protein complexes published in:

Andrea Picco, Ibai Irastorza-Azcarate, Tanja Specht, Dominik Böke, Irene Pazos, Anne-Sophie Rivier-Cordey, Damien P. Devos, Marko Kaksonen, Oriol Gallego, The in vivo architecture of the exocyst provides structural basis for exocytosis, Cell; DOI:to be announced

This is the repository to which the Cell STAR methods points to.

##Requirements:
IMP version 2.1.1 or earlier https://integrativemodeling.org/

UCSF chimera http://www.cgl.ucsf.edu/chimera/

MeV https://sourceforge.net/projects/mev-tm4/

##Usage
###Exocyst
####Tag modeling:
1 - mkdir output #create output directory

2 - runIMP_exocystTags.pl 10000 0 output #generate 10000 models starting from model number 0 (in case we want to parallelize)

3 - evalbstmdl_exocyst.pl dir_with_tag_models #get the RMSD matrix from the best models

####Protein modeling:
1 - runIMP_exocyst.pl tag_matrix_from_MeV 10000 #generate 10000 excyst models. We need one cluster from the RMSD matrix computed before. With MeV cluster it and get a population of them.

2 - supbestmdl_exocyst.pl   #evaluate and get best models

###COG
The same as for the exocyst but with the scripts finishing in cog.

###Other scripts
to generate a superposition and get std-dev of best tag models 

1 - analcluster.pl 
