#!/usr/bin/perl

srand;
#score limit variable
$scrlmt=3450;
die "USAGE: ./runIMP.pl cluster_matrix_file nbr_iterat \n" unless ($ARGV[0]=~/\d/);

@df=split/\//,$ARGV[0];
$iterat=$ARGV[1];

die "USAGE: ./runIMP.pl cluster_matrix_file nbr_iterat\n" unless (-e "$df[0]/$df[1]");

open (IN,"$ARGV[0]");
while (<IN>) {
 if (/\d+\t(\S+)/) {
	@l=split /\t/;
	$cl{$l[1]}++;
 }
}
$ncl=@cl=keys %cl;
#print "@cl $ncl in $df[0] $df[1] for $iterat\n";

open (SCR,">output/scores_final.txt");

for ($i=0;$i<=$iterat-1;$i++) {
#print "Iteration: $i\n";
#1) copy tags location
#2) generate random starting point for proteins

#randomly select the starting file
$rndfil=int(rand($#cl));
open (RPR,"$df[0]/$cl[$rndfil]");

#print "$rndfil with file $df[0]/$cl[$rndfil]\n";

open (OUT,">input/repr_exocyst_rdm.xml");
print OUT "<Representation>\n";

#copy the starting location
open (IN,"$df[0]/$cl[$rndfil]");
while (<IN>) {
 if (/if \"(\w+)\" not in marker_sets/) {$prt=$1;
 } elsif (/mark=s\.place_marker\(\((.\d.+?)\),/) {
	@crd=split/, /,$1;

print OUT "<Fragment id=\"$prt\">\n\t<GeometricShapeRep total_residue=\"150\">\n\t\t<Sphere><InitialPosition x=\"$crd[0]\" y=\"$crd[1]\" z=\"$crd[2]\" optimize=\"1\"/></Sphere>\n\t</GeometricShapeRep>\n</Fragment>\n";
 }
}

#get the starting location for the protein
open (RPR,"input/repr_exocyst.xml");
while (<RPR>) {
 if (/InitialPosition/) {

		$x=int(rand(1000));
		$y=int(rand(1000));
		$z=int(rand(1000));
 print OUT "<Sphere><InitialPosition  x=\"$x\" y=\"$y\" z=\"$z\" optimize=\"1\"/></Sphere>\n"
 } else {print OUT;}
}

print OUT "</Representation>\n";
close OUT;

#run IMP, save the scores
open (IMP,"python exocyst.py |");
open (OUT,">output/log_scr.txt");

while (<IMP>) {
 print OUT if (/score/);
 $scr=$1 if (/Final score: (\S+)/);
}
print SCR "$i\t$scr\n";
$sc=int($scr/10);
$sc{$sc}++;

print "Protein score: $scr. Limit: $scrlmt\n\n";
if ($scr<$scrlmt) {
print "rc(\"open $df[0]/$cl[$rndfil]\") __model:$i\n";
system "mv output/initial.py output/initial_$i.py";
system "mv output/optimized.py output/optimized_$i.py";
system "mv output/log_scr.txt output/log_scr_$i.txt";
}
}

print SCR "####dstr of scores\nscore\t# of models\n";
foreach $c (sort byc keys %sc) {
 print "$c\t$sc{$c}\n";
 print SCR "$c\t$sc{$c}\n";
}
system "rm output/log_scr.txt output/initial.py output/optimized.py" if (-e "output/log_scr.txt");
sub byc {
 $a<=>$b;
}
