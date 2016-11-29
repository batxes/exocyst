#!/usr/bin/perl

srand;

die "USAGE: ./runIMP.pl nbr_iterat starting_iteration output_folder_number\n" unless ($ARGV[0]=~/\d/);
$output = $ARGV[2];
$file = "$output/scores_final.txt";
open (SCR,">",$file);
$iterat=$ARGV[0];
$starting_iteration=$ARGV[1];

for ($i=$starting_iteration;$i<=$iterat+$starting_iteration-1;$i++) {
# generate random starting point
    open (RPR,"input/repr_exocyst_Tags.xml");
    open (OUT,">input/repr_exocyst_Tags_rdm_$output.xml");
    while (<RPR>) {
     if (/InitialPosition/) {

            $x=int(rand(1000));
            $y=int(rand(1000));
            $z=int(rand(1000));
     print OUT "<Sphere><InitialPosition  x=\"$x\" y=\"$y\" z=\"$z\" optimize=\"1\"/></Sphere>\n"
     } else {print OUT;}
    }
    close OUT;

#run IMP, save the scores

    open (IMP,"python exocyst_Tags.py $output |");
    open (OUT,">$output/log_scr.txt");

    while (<IMP>) {
     print OUT if (/score/);
     $scr=$1 if (/Final score: (\S+)/);
    }
    print SCR "$i\t$scr\n";
    $sc=int($scr/10);
    $sc{$sc}++;
    print "\nIteration $i";
    print "\nSCORE is = $scr ";
    if ($scr<6) {
    print "------------> Satisfied!\n";
        system "mv $output/initial.py $output/initial_$i.py";
        system "mv $output/optimized.py $output/optimized_$i.py";
        system "mv $output/log_scr.txt $output/log_scr_$i.txt";

        open (SAT,"perl ./programs/evalmdl_exocyst.pl $i |");
        while (<SAT>) {print if (/should be/);
            if (/(\d+) non sat restr/) {print;
                $nsr=$1;
                if ($1!=0){
                    print "\t Deleting model number $i\n";
                    system "rm $output/initial_$i.py";
                    system "rm $output/optimized_$i.py";
                    system "rm $output/log_scr_$i.txt";
                }
                system "rm $output/optimized_$i.pyc";
            }
        }
    }

}

print SCR "####dstr of scores\nscore\t# of models\n";
foreach $c (sort byc keys %sc) {
 print "$c\t$sc{$c}\n";
 print SCR "$c\t$sc{$c}\n";
}
system "rm $output/log_scr.txt $output/initial.py $output/optimized.py" if (-e "$output/log_scr.txt");
sub byc {
 $a<=>$b;
}

close(MYLOG);
