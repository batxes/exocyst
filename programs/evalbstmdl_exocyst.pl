#!/usr/bin/perl

##get the scores
open (IN,"./output/scores_final.txt");
while (<IN>) {last if (/###/);chomp;
 ($mdl,$s)=split /\t/;
 $s{$mdl}=$s;
}

#evaluate the 200 best scores for constraints satisfaction
$cnt=-1;
foreach $s (sort bys keys %s) {
 $cnt++;
 $nnurm=@nurm;
last if ($nnurm==200);
 print "$cnt $s with $s{$s}\n";
 open (SAT,"perl ./programs/evalmdl_exocyst.pl $s |");
 while (<SAT>) {print if (/should be/);
  if (/(\d+) non sat restr/) {print;
	$nsr=$1;
	push @nurm,$s if ($1==0);
  }
 }
}

#RMSD all against all the 200 best that satisfy ALL restraints only!
$nnurm=@nurm;
print "@nurm\n$nnurm models that satisfy all restraint\n";

## Matrix is symmetrical calculate only half and populate the rest
open (MTX,">mtx.txt");
for ($i=0;$i<=$#nurm;$i++) {print MTX "\toptimized_$nurm[$i].py";}print MTX "\n";
for ($i=0;$i<=$#nurm;$i++) {
 print MTX "optimized_$nurm[$i].py";
 for ($j=0;$j<=$#nurm;$j++) {#die if ($i==2 && $j==3);
	$rmsd="-";
	if ($j==$i) {print MTX "\t";next;
	} elsif (defined $rmsd{$i}{$j}) {
	print "rmsd $rmsd{$i}{$j} Angstr\n";
	print MTX "\t$rmsd{$i}{$j}";
	} else {

	 print "$nurm[$i] vs $nurm[$j]\t";
	 open (CHM,">chimeraEval_exocyst_Tags.py");
print CHM "import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\n";
print CHM "os.chdir(\"./output\")\n";
print CHM "rc(\"open optimized_$nurm[$i].py\")\n";
print CHM "rc(\"open optimized_$nurm[$j].py\")\n";
#change this number according to model panel
print CHM "rc(\"match #0-21 #22-43\")\n";

print CHM "rc(\"close all\")\nrc(\"stop now\")\n";
close CHM;
	open (CHI,"chimera --nogui chimeraEval_exocyst_Tags.py |");
	while (<CHI>) {
		print;
		if (/RMSD between \d+ atom pairs is (\S+) angstroms/) {
		 $rmsd=$1;
		}
	}
	print "rmsd $rmsd Angstr\n";
	print MTX "\t$rmsd";
	$rmsd{$j}{$i}=$rmsd;
	}
	
 }
 print MTX "\n";
}
print "$nnurm models that satisfy all restraint\n";

sub bys {$s{$a}<=>$s{$b};}
