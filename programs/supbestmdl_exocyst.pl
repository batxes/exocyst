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
 last if ($cnt==200);
 print "$cnt $s with $s{$s}\n";
 open (SAT,"perl programs/evalrestrdmtr_exocyst.pl $s |");
 while (<SAT>) {print if (/should be/);
  if (/(\d+) non sat restr/) {print;
	$nsr=$1;
	push @nurm,$s if ($1==0);
    print "Added model.\n" if ($1==0);
  }
 }
}

@nn=@nurm;

system ("perl programs/removtag_exocyst.pl output/optimized_$nn[0].py\n");
open (CHM,">chimera_bstmdlnotags_exocyst.py");
print CHM "import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\"./output\")\n";
print CHM "rc(\"open optimized_$nn[0]_notags.py\")\n";

$nbrprt1=6;#Sec3
$nbrprt2=5;#Sec5
$nbrprt3=5;#Sec6
$nbrprt4=5;#Sec8
$nbrprt5=5;#Sec10
$nbrprt6=5;#Sec15
$nbrprt7=4;#Exo70
$nbrprt8=3;#Exo84

$b1=0;$e1=$b1+$nbrprt1;
$b2=$e1+1;$e2=$b2+$nbrprt2;
$b3=$e2+1;$e3=$b3+$nbrprt3;
$b4=$e3+1;$e4=$b4+$nbrprt4;
$b5=$e4+1;$e5=$b5+$nbrprt5;
$b6=$e5+1;$e6=$b6+$nbrprt6;
$b7=$e6+1;$e7=$b7+$nbrprt7;
$b8=$e7+1;$e8=$b8+$nbrprt8;

$nef=$e8;

for ($i=1;$i<=99;$i++) {
$nn=$nn[$i];
next unless (-e "output/optimized_${nn}.py");
system ("perl programs/removtag_exocyst.pl output/optimized_${nn}.py\n");

 print CHM "rc(\"open optimized_${nn}_notags.py\")\n";
 $nb1=$nef+1;$ne1=$nb1+$nbrprt1;
 $nb2=$ne1+1;$ne2=$nb2+$nbrprt2;
 $nb3=$ne2+1;$ne3=$nb3+$nbrprt3;
 $nb4=$ne3+1;$ne4=$nb4+$nbrprt4;
 $nb5=$ne4+1;$ne5=$nb5+$nbrprt5;
 $nb6=$ne5+1;$ne6=$nb6+$nbrprt6;
 $nb7=$ne6+1;$ne7=$nb7+$nbrprt7;
 $nb8=$ne7+1;$ne8=$nb8+$nbrprt8;
 $nef=$ne8;
 print CHM "rc(\"match #$nb1-$ne1 #$b1-$e1\")\n";
 print CHM "rc(\"match #$nb2-$ne2 #$b2-$e2\")\n";
 print CHM "rc(\"match #$nb3-$ne3 #$b3-$e3\")\n";
 print CHM "rc(\"match #$nb4-$ne4 #$b4-$e4\")\n";
 print CHM "rc(\"match #$nb5-$ne5 #$b5-$e5\")\n";
 print CHM "rc(\"match #$nb6-$ne6 #$b6-$e6\")\n";
 print CHM "rc(\"match #$nb7-$ne7 #$b7-$e7\")\n";
 print CHM "rc(\"match #$nb8-$ne8 #$b8-$e8\")\n";
 
}
print CHM "rc(\"open optimized_$nn[0].py\")\n";
#die;
system "chimera chimera_bstmdlnotags_exocyst.py";

sub bys {$s{$a}<=>$s{$b};}

