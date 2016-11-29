#!/usr/bin/perl

die "USAGE:	evalmdl.pl number_mdl2eval\n" unless (-e "output/optimized_$ARGV[0].py");

open (DSP,"./input/displ_cog_Tags.xml");
$id=-1;
while (<DSP>) {next if (/--/);
	if (/<Chain><Fragment id="(\S+)"><Color/) {$id++;$id{$1}=$id;$di{$id}=$1;}
}

open (RES,"./input/restraint_cog_Tags.xml");
while (<RES>) {
 last if (/<!--/);
last if (/Diameter/);
 if (/Restraint name="dst\d+" distance="(\S+)" std_dev="(\S+)"/) {$res=$1;$std=$2;}
 if (/<Particle id="(\S+)"\/>/) {push @prt,$1;}
 if (/<\/Restraint>/ && defined $res) {
	$res{"$prt[0]-$prt[1]"}=$res;
	$std{"$prt[0]-$prt[1]"}=$std;
	$nres++;
	undef @prt;
	undef $res;
 }
}

open (CHM,">chimeraEval_cog_Tags.py");
print CHM "import os\nfrom chimera import runCommand as rc\nfrom chimera import replyobj\n";
print CHM "os.chdir(\"./output\")\n";
print CHM "rc(\"open optimized_$ARGV[0].py\")\n";

foreach $pr (keys %res) {
	@pr=split /-/,$pr;
	print CHM "rc(\"distance \#$id{$pr[0]} \#$id{$pr[1]}\")\n";
}
#print "$nres restrn\n";

print CHM "rc(\"close all\")\nrc(\"stop now\")\n";

$nsr=0;
open (CHI,"chimera --nogui chimeraEval_cog_Tags.py |");
while (<CHI>) {
	if (/Distance between #(\d+):1@ and #(\d+):1@:.+?(\d+)/) {
		$do=$3;$dr=$res{"$di{$1}-$di{$2}"};$stdr=$std{"$di{$1}-$di{$2}"};
		if ($do>$dr-($stdr*1) && $do<$dr+($stdr*1)) {#print "OK\n";
		} else {$nsr++;print "distance $1 $di{$1} $2 $di{$2} is $3 should be $dr+-$stdr\n";
		}
	}
}
print "$nsr non sat restr on $nres restrn\n";
