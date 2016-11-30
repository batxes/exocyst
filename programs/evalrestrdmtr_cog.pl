#!/usr/bin/perl

#check out line 188 with the double std_dev

#Only works when y2h interactions are in pairs and have no subnumber of beads
$y2h_cut_off_distance = 35; #35 its the minimum distance
$y2h_number = 1; #quantity of y2h interactions in restraints

die "USAGE:	evalmdl.pl number_mdl2eval\n" unless (-e "output/optimized_$ARGV[0].py");

open (DSP,"./input/displ_cog.xml");
$id=-1;
while (<DSP>) {next if (/--/);
	if (/<Fragment id="(\S+)"><Color/) {$id++;$id{$1}=$id;$di{$id}=$1;}
}

open (RES,"./input/restraint_cog.xml");
$y2h = 0;
$ny2h = 0;
$exVol = 0;
@y2h;
while (<RES>) {
 if ($y2h == 0 and $exVol == 0){
     if (/Restraint name="\S+\d+" max_diameter="(\S+)" std_dev="(\S+)"/) {$res=$1;$std=$2;}
     if (/Restraint name="\S+\d+" distance="(\S+)" std_dev="(\S+)"/) {$dis=$1;$std=$2;}
     if (/<Particle id="(\S+)"\/>/) {push @prt,$1;}
     if (/<\/Restraint>/) {
        $res{"$prt[0]-$prt[1]"}=$res if (defined $res);
        $dis{"$prt[0]-$prt[1]"}=$dis if (defined $dis);
        $std{"$prt[0]-$prt[1]"}=$std;
        $nres++;
        print "1 Diam $nres $prt[0] $prt[1] $res $std\n" if (defined $res);
        print "1 Dist $nres $prt[0] $prt[1] $dis $std\n" if (defined $dis);
        undef @prt;
        undef $res;
        undef $dis;
     }
 }
 if (/<Y2H>/){
        $y2h = 1;
    }
  
 if (/<\/Y2H>/){
        $y2h = 0;
    }
 if ($y2h == 1){
        #save the y2h pairs in an array
        if (/<Particle id="(\S+)"\/>/) {
            push @y2h,$1;
        }
        if (/<\/Restraint>/) {
           print "y2h interaction $ny2h: @y2h \n";
           $ny2h++;
           $y2h_list {$ny2h} = [@y2h];
           @y2h = ();
        }
    }
    
 if (/<ExcludedVolume>/){
        $exVol = 1;
    }
 if (/<\/ExcludedVolume>/){
        $exVol = 0;
    }
 #read from excluded volume the quantity of beads of each protein and store them in a hash
 if ($exVol == 1){
    if (/<Particle id="(\S+)"\/>/) {
        $prt_aux = $1;
        @prt_aux = split ("_",$prt_aux);
        $prt_id{"$prt_aux[0]"} = $prt_aux[1];
        
    }
 }
                
}
#use Data::Dumper;
#print Dumper(\%y2h_list);

#print the hash to see its content
#while (($k,$v)=each %prt_id){print "$k $v\n"};

#we generate 2 python file evaluators, one for distance and diameters and another one for y2h
#since some distances are already evaluated
open (CHM,">chimeraEvaldmtr_cog.py");
print CHM "import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\n";
print CHM "os.chdir(\"./output\")\n";
print CHM "rc(\"open optimized_$ARGV[0].py\")\n";

open (CHMY2H,">chimeraEvaldmtrY2H_cog.py");
print CHMY2H "import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\n";
print CHMY2H "os.chdir(\"./output\")\n";
print CHMY2H "rc(\"open optimized_$ARGV[0].py\")\n";

foreach $pr (keys %res) {
	@pr=split /-/,$pr;
	print "Diam $res{$pr} with std $std{$pr} btw $pr -$id{$pr[0]} $id{$pr[1]}=\n";
	print CHM "rc(\"distance \#$id{$pr[0]} \#$id{$pr[1]}\")\n";
}
foreach $pr (keys %dis) {
	@pr=split /-/,$pr;
	#print "Dist $dis{$pr} with std $std{$pr} btw $pr -$id{$pr[0]} $id{$pr[1]}=\n";
	print CHM "rc(\"distance \#$id{$pr[0]} \#$id{$pr[1]}\")\n";
}
#write the code to check y2h interactions
# only works if the y2h interactions are with all the sub beads: sec3_0 Sec4_2 ...
for ($i=1; $i<=$y2h_number;$i++){
    print " Vuelta $i: ";
    print $y2h_list{"$i"}[0];
    print "\n";
    print $y2h_list{"$i"}[1];
    print "\n";
    $n_of_y2h_per_pair = 0;
    @list1=();
    @list2=();
    if ($y2h_list{"$i"}[0] !~ m/_/){
        @list1 = Add_all_beads_y2h($y2h_list{"$i"}[0]);
        if ($y2h_list{"$i"}[1] !~ m/_/){
            @list2 = Add_all_beads_y2h($y2h_list{"$i"}[1]);
        } else{
            for($j=1;$j<scalar@{$y2h_list{"$i"}};$j++){
                push(@list2,$y2h_list{"$i"}[$j]);
            }
        }
    } else{
        @prefijo = split("_",$y2h_list{"$i"}[0]);
        push(@list1,$y2h_list{"$i"}[0]);
        for($j=1;$j<scalar@{$y2h_list{"$i"}};$j++){
            if ($y2h_list{"$i"}[$j] =~ /_/){
                @pre = split("_",$y2h_list{"$i"}[$j]);
                print "\npre = $pre[0]. prefijo = $prefijo[0]\n";
                if( $pre[0] eq $prefijo[0]){
                    push(@list1,$y2h_list{"$i"}[$j]);
                    print "valor metido en lista1: "; 
                    print $y2h_list{"$i"}[$j];
                }else{
                    push(@list2,$y2h_list{"$i"}[$j]);
                    print "valor metido en lista2: "; 
                    print $y2h_list{"$i"}[$j];
                }
            } else {
                @list2 = Add_all_beads_y2h($y2h_list{"$i"}[$j]);
            }
    
        }
        
    }
    #print "list1: ";
    #print @list1;
    #print "\nlist2: ";
    #print @list2;
    #print "Pres INTRO\n";
    #$userinput =  <STDIN>;
    for ($j=0; $j < scalar@list1;$j++){
        for ($k=0; $k < scalar@list2;$k++){
            $bead_1 = $list1[$j];
            $bead_2 = $list2[$k];
            print "Y2h dist btw $bead_1 and $bead_2 must be less than $y2h_cut_off_distance\n";
            print CHMY2H "rc(\"distance \#$id{$bead_1} \#$id{$bead_2}\")\n";
            $n_of_y2h_per_pair++;
        }
    }
    push (@number_of_distances_in_y2h,$n_of_y2h_per_pair);
}



#print "$nres restrn\n";
print CHM "rc(\"close all\")\nrc(\"stop now\")\n";
print CHMY2H "rc(\"close all\")\nrc(\"stop now\")\n";

$nsr=0;
open (CHI,"chimera --nogui chimeraEvaldmtr_cog.py |");
while (<CHI>) {
	if (/Distance between #(\d+):1@ and #(\d+):1@:.+?(\d+)/) {
	  if (defined $res{"$di{$1}-$di{$2}"}) {
        
          #print "\n############  EL ERROR DIO CON: $1 y $2";
		$do=$3;$dr=$res{"$di{$1}-$di{$2}"};$stdr=$std{"$di{$1}-$di{$2}"};
#		print "distance $1 $di{$1} $2 $di{$2} is $3 should be $dr+-$stdr\n";
		if ($do<$dr+($stdr)) {#print "OK\n";
		} else {$nsr++;print "distance $1 $di{$1} $2 $di{$2} is $3 should be $dr+-$stdr\n";
		}
	  }
	  if (defined $dis{"$di{$1}-$di{$2}"}) {
          #print "\n############  EL ERROR DIO CON: $1 y $2";
		$do=$3;$dr=$dis{"$di{$1}-$di{$2}"};$stdr=$std{"$di{$1}-$di{$2}"};
#		print "distance $1 $di{$1} $2 $di{$2} is $3 should be $dr+-$stdr\n";
		if ($do>=$dr-($stdr*1) && $do<=$dr+($stdr*1)) {#print "OK\n";
		} else {$nsr++;print "distance $1 $di{$1} $2 $di{$2} is $3 should be $dr+-$stdr\n";
		}
	  }
	}
}
$y2h_quantity = scalar@number_of_distances_in_y2h;
$interaction_ok = 0;
$j= 0;
    open (CHI_Y2H,"chimera --nogui chimeraEvaldmtrY2H_cog.py |");
    for ($i = 0; $i<$y2h_quantity; $i++){
        while (<CHI_Y2H>){
            #print "\n j = $j. number of distances in y2h[i] = $number_of_distances_in_y2h[$i]";
            if ($j == $number_of_distances_in_y2h[$i]){last;}
            if (/Distance between #(\d+):1@ and #(\d+):1@:.+?(\d+)/) {
                $j++;
                print "\n$1 and $2 = Distance $3";
                if ($3<$y2h_cut_off_distance) { 
                    $interaction_ok = 1;
                }         
                
            }
        }
        #print "\n\nLAST?\n\n";
        $j = 0;
        if ($interaction_ok == 0){
            $nsr++;
            print "\ndistance y2h number $i not fulfilled";
        }
    }
#close CHI_Y2H;
$nres_total = $nres + $ny2h;
print "\n$nsr non sat restr on $nres_total restrn\n";

sub Add_all_beads_y2h(){
    $residue = $_[0];
    @list = ();
    if ($residue =~ /Cog2/){
        $beads = 2;
    } else {
        if ($residue =~ /Cog7/){
            $beads = 3;
        } else {
            if ($residue =~/Cog5/){
                $beads = 4;
            } else {
                if ($residue =~/Cog4/){
                    $beads = 7;
                } else {
                    if ($residue =~/Cog3/){ 
                        $beads = 6;    
                    }else{
                        if ($residue =~/Cog8/){
                            $beads = 6;
                    }else{ 
                        if ($residue =~/Cog6/){
                            $beads = 7;
                        }
                        else{$beads = 4}
                }
                
                }
            }
            }        
        }
     }
    for ($l = 0; $l < $beads; $l++){
        $value = "$residue\_$l";
        push @list, $value;
    }
    return @list;
}
