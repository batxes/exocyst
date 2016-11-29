#!/usr/bin/perl

die "USAGE:	evalmdl.pl number_mdl2eval\n" unless (-e "output/optimized_$ARGV[0].py");

open (DSP,"./input/displ_exocyst.xml");
$id=-1;
while (<DSP>) {next if (/--/);
	if (/<Fragment id="(\S+)"><Color/) {$id++;$id{$1}=$id;$di{$id}=$1;}
}

open (RES,"./input/restraint_exocyst.xml");
while (<RES>) {
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

open (CHM,">chimeraEvaldmtr_exocyst.py");
print CHM "import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\n";
print CHM "os.chdir(\"./output\")\n";
print CHM "rc(\"open optimized_$ARGV[0].py\")\n";

foreach $pr (keys %res) {
	@pr=split /-/,$pr;
	print "Diam $res{$pr} with std $std{$pr} btw $pr -$id{$pr[0]} $id{$pr[1]}=\n";
	print CHM "rc(\"distance \#$id{$pr[0]} \#$id{$pr[1]}\")\n";
}
foreach $pr (keys %dis) {
	@pr=split /-/,$pr;
	print "Dist $dis{$pr} with std $std{$pr} btw $pr -$id{$pr[0]} $id{$pr[1]}=\n";
	print CHM "rc(\"distance \#$id{$pr[0]} \#$id{$pr[1]}\")\n";
}
#print "$nres restrn\n";

print CHM "rc(\"close all\")\nrc(\"stop now\")\n";

$nsr=0;
open (CHI,"chimera --nogui chimeraEvaldmtr_exocyst.py |");
while (<CHI>) {
	if (/Distance between #(\d+):1@ and #(\d+):1@:.+?(\d+)/) {
	  if (defined $res{"$di{$1}-$di{$2}"}) {
		$do=$3;$dr=$res{"$di{$1}-$di{$2}"};$stdr=$std{"$di{$1}-$di{$2}"};
		if ($do<$dr+($stdr*2)) {#print "OK\n";
		} else {$nsr++;print "distance $1 $di{$1} $2 $di{$2} is $3 should be $dr+-$stdr\n";
		}
	  }
	  if (defined $dis{"$di{$1}-$di{$2}"}) {
		$do=$3;$dr=$dis{"$di{$1}-$di{$2}"};$stdr=$std{"$di{$1}-$di{$2}"};
		if ($do>=$dr-($stdr*2) && $do<=$dr+($stdr*2)) {#print "OK\n";
		} else {$nsr++;print "distance $1 $di{$1} $2 $di{$2} is $3 should be $dr+-$stdr\n";
		}
	  }
	}
}
print "$nsr non sat restr on $nres restrn\n";
