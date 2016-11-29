#!/usr/bin/perl

die "USAGE:./analcluster.pl cluster_file_from_MeV\n" unless (-e $ARGV[0]);

###change the output folder!!
###change the number of beads!!

open (IN,"$ARGV[0]");
while (<IN>) {
 if (/\d+\t(\S+)/) {
	@l=split /\t/;
	$cl{$l[1]}++;
 }
}
$ncl=@cl=keys %cl;

# calculate the sum of RMSD for each belonging to cluster
open (MTX,"output_cog_10000_no_cog1_def1/mtx.txt"); #output dir of tag models/matrix.txt
@id=split /\t/,<MTX>;
print @id;
while (<MTX>) {
	@l=split /\t/;
	if (defined $cl{$l[0]}) {
#	 print "$l[0] ok @l\n";
	 for ($i=0;$i<=$#l;$i++) {
		if (defined $cl{$id[$i]}) {
		 $sum{$l[0]}+=$l[$i];
#		 print "$l[0] vs $i $id[$i] $cl{$id[$i]} with $l[$i] sum $sum{$l[0]}\n";
		}
	 }
	 print "$l[0] with $sum{$l[0]}\n";
	}
}

#get the 80% representative and change their diameter
$lim=int($ncl*1);  #por the 80% put .8 instead of 1
$n = 0;
foreach $mdl (sort bys keys %sum) {
    print "$n\n";
	last if ($n==$lim);
	print "$n $mdl with $sum{$mdl}\n";$nn=$mdl;$nn=~s/.py/_sml.py/;push @nn,$nn;
	system "perl ./programs/chngdmtr.py output_cog_10000_no_cog1_def1/$mdl\n" unless (-e "output_cog_10000_no_cog1_def1/$nn");
	push @mdl,$mdl;
	$n++;
}

$fff=$ARGV[0];
$fff=~s/\W+//;

open (CHM,">chimeracluster_$fff.py");
print CHM "import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\"./output_cog_10000_no_cog1_def1\")\n";
print CHM "rc(\"open $nn[0]\")\n";
$f=shift @nn;
$nbrprt=20;# this value to be changed according to spheres number
 $b=0;$e=$nbrprt;
foreach $nn (@nn) {
 print CHM "rc(\"open $nn\")\n";
 $b=$e+1;$e=$b+$nbrprt;
 print CHM "rc(\"match #$b-$e #0-$nbrprt iterate 10000\")\n";
}

system "chimera chimeracluster_$fff.py";

print "\nUSE:chimera chimeracluster_$fff.py\n";

sub bys {$sum{$a}<=>$sum{$b};}
