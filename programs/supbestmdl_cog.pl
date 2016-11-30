#!/usr/bin/perl

#for the COG proteins
# remember that we need models that satisfy all restraints. All restraints = 0
$satisfaction_res = 0;
#number of random models to represent from full population
$random_models = 100; #Take 100 random models from the 200 best 
$best_models = 200;
@aux; 
##get the scores
open (IN,"./output/scores_final.txt");
while (<IN>) {last if (/###/);chomp;
    ($mdl,$s)=split /\t/;
     $s{$mdl}=$s;
}

#stop with 200 satisfied models
$cnt=-1;
foreach $s (sort bys keys %s) {
     $cnt++;
     last if ($cnt==1000); 
     print "$cnt $s with $s{$s}\n";
#    open (SAT,"./programs/evalmdl.pl $s |");
     open (SAT,"perl ./programs/evalrestrdmtr_cog.pl $s |");
     while (<SAT>) {print if (/should be/);
          if (/(\d+) non sat restr/) {
                print <SAT>;
                print;
                $nsr=$1;
                if ($1<=$satisfaction_res){ #number of restraints to fulfil
                    push @nurm,$s;
                    print "<--- Satisfied! \n";
                }
                print "nurm scalar: ";
                print scalar(@nurm);
                print "\n";

                if (scalar(@nurm) eq $best_models){
                    $cnt = 999;
                }
#   	         push @nurm,$s if ($1<=1);
          }
     }
}

#get the 100 best scores
#@nn=sort bys keys %s;
@nn=@nurm;

#####   get a percentage of array

for ($i=0; $i<$random_models;$i++){
    $random_number = int (rand(scalar@nn));
    push (@aux,$nn[$random_number]);
    splice(@nn,$random_number,1);    
}
#@nn = @aux;  

print ("perl programs/removtag_cog.pl output/optimized_$nn[0].py\n");
system ("perl programs/removtag_cog.pl output/optimized_$nn[0].py\n");

open (CHM,">chimera_bstmdlnotags.py");
print CHM "import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\nos.chdir(\"./output\")\n";
print CHM "rc(\"open optimized_$nn[0]_notags.py\")\n";

$nbrprt1=1;#cog2
$nbrprt2=5;#3
$nbrprt3=6;#4
$nbrprt4=3;#5		
$nbrprt5=6;#6
$nbrprt6=2;#7
$nbrprt7=5;#8

$b1=0;$e1=$b1+$nbrprt1;
$b2=$e1+1;$e2=$b2+$nbrprt2;
$b3=$e2+1;$e3=$b3+$nbrprt3;
$b4=$e3+1;$e4=$b4+$nbrprt4;
$b5=$e4+1;$e5=$b5+$nbrprt5;
$b6=$e5+1;$e6=$b6+$nbrprt6;
$b7=$e6+1;$e7=$b7+$nbrprt7;

$nef=$e7;
$e8=$e7;

#use the line below if less than 100 models
for ($i=1;$i<=$#nn;$i++) {
$nn=$nn[$i];
next unless (-e "output/optimized_${nn}.py");
system ("perl programs/removtag_cog.pl output/optimized_${nn}.py\n");
#	push @nurm,$s if ($1==0);

 print CHM "rc(\"open optimized_${nn}_notags.py\")\n";
 $nb1=$nef+1;$ne1=$nb1+$nbrprt1;
 $nb2=$ne1+1;$ne2=$nb2+$nbrprt2;
 $nb3=$ne2+1;$ne3=$nb3+$nbrprt3;
 $nb4=$ne3+1;$ne4=$nb4+$nbrprt4;
 $nb5=$ne4+1;$ne5=$nb5+$nbrprt5;
 $nb6=$ne5+1;$ne6=$nb6+$nbrprt6;
 $nb7=$ne6+1;$ne7=$nb7+$nbrprt7;
 #$nb8=$ne7+1;$ne8=$nb8+$nbrprt8;
 $nef=$ne7;
 $ne8=$ne7;

 #matching segments
 #	print CHM "rc(\"match #$nb1-$ne1 #$b1-$e1\")\n";
 #print CHM "rc(\"match #$nb2-$ne2 #$b2-$e2\")\n";
 #print CHM "rc(\"match #$nb3-$ne3 #$b3-$e3\")\n";
 #print CHM "rc(\"match #$nb4-$ne4 #$b4-$e4\")\n";
 #print CHM "rc(\"match #$nb5-$ne5 #$b5-$e5\")\n";

 #matching all the protein
 print CHM "rc(\"match #$nb1-$ne8 #$b1-$e8\")\n";
}
print CHM "rc(\"open optimized_$nn[0].py\")\n";
#die;
system "chimera chimera_bstmdlnotags.py";

sub bys {$s{$a}<=>$s{$b};}

