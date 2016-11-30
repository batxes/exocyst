#!/usr/bin/perl
#modify lines depending on cog or exocyst

die "USAGE:./removtag.pl dir/file [sphere radius]\n" unless (-e $ARGV[0]);

open (IN,$ARGV[0]);
@df=split/\//,$ARGV[0];
$nm=$df[1];
$nm=~s/.py/_notags.py/;

open (OUT,">$df[0]/$nm\n");
$prt=1;
while (<IN>) {
if (/mark=s\.place_marker/) {
	$l=$_;
	$l=~s/\d+\.\d+\)$/2\)/;
	print OUT $l if ($prt==1);
} else {
 $prt=0 if (/if \"\w+_\D+\" not in marker_sets:/);
 $prt=1 if (/if \"\w+_\d+\" not in marker_sets:/ && (/Cog1/ || /Cog2/ || /Cog3/ || /Cog4/ || /Cog5/ || /Cog6/ || /Cog7/ || /Cog8/));

 print OUT if ($prt==1);
}
}
