#!/usr/bin/perl

##get the scores
open (IN,"./output/scores_final.txt");
while (<IN>) {last if (/###/);chomp;
 ($mdl,$s)=split /\t/;
 $s{$mdl}=$s;
}

$cnt=-1;
foreach $s (sort bys keys %s) {
 $cnt++;
 last if ($cnt==100);
 print "$cnt $s with $s{$s}\n";
 open (SAT,"./programs/evalrestrdmtr_exocyst.pl $s |");
 while (<SAT>) {print if (/should be/);
  if (/(\d+) non sat restr/) {print;
	$nsr=$1;
	push @nurm,$s if ($1==0);
  }
 }
}

@nn=@nurm;

system ("./programs/removtag.pl output/optimized_$nn[0].py\n");
open (CHM,">chimera_bstmdlnotags.py");
print CHM "import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\"./output\")\n";
print CHM "rc(\"open optimized_$nn[0]_notags.py\")\n";

#$nbrprt1=5;
#$nbrprt=25;
$nbrprt1=6;#Sec3
$nbrprt2=5;#Sec5
$nbrprt3=4;#Sec6
$nbrprt4=5;#Sec10
$nbrprt5=5;#Sec15
$nbrprt6=1;#Exo70
$nbrprt7=1;#Exo84

$b1=0;$e1=$b1+$nbrprt1;
$b2=$e1+1;$e2=$b2+$nbrprt2;
$b3=$e2+1;$e3=$b3+$nbrprt3;
$b4=$e3+1;$e4=$b4+$nbrprt4;
$b5=$e4+1;$e5=$b5+$nbrprt4;
#$b6=$e5+1;$e6=$b6+$nbrprt5;
#$b7=$e6+1;$e7=$b7+$nbrprt6;

#$nef=$e5;
$nef=$e5+2;
#$nef=$e7;

for ($i=1;$i<=99;$i++) {
$nn=$nn[$i];
next unless (-e "output/optimized_${nn}.py");
system ("./programs/removtag.pl output/optimized_${nn}.py\n");

 print CHM "rc(\"open optimized_${nn}_notags.py\")\n";
 $nb1=$nef+1;$ne1=$nb1+$nbrprt1;
 $nb2=$ne1+1;$ne2=$nb2+$nbrprt2;
 $nb3=$ne2+1;$ne3=$nb3+$nbrprt3;
 $nb4=$ne3+1;$ne4=$nb4+$nbrprt4;
 $nb5=$ne4+1;$ne5=$nb5+$nbrprt5;
 $nef=$ne5+2;
 print CHM "rc(\"match #$nb1-$ne1 #$b1-$e1\")\n";
 print CHM "rc(\"match #$nb2-$ne2 #$b2-$e2\")\n";
 print CHM "rc(\"match #$nb3-$ne3 #$b3-$e3\")\n";
 print CHM "rc(\"match #$nb4-$ne4 #$b4-$e4\")\n";
 print CHM "rc(\"match #$nb5-$ne5 #$b5-$e5\")\n";
 
}
print CHM "rc(\"open optimized_$nn[0].py\")\n";
#die;
system "chimera chimera_bstmdlnotags.py";

sub bys {$s{$a}<=>$s{$b};}

