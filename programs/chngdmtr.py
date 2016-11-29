#!/usr/bin/perl

open (IN,$ARGV[0]);
$chg=$ARGV[0];
$chg=~s/.py/_sml.py/;
open (OUT,">$chg");
while (<IN>) {
 if (/mark=s\.place_marker/) {
	$l=$_;
	$l=~s/\d+\.\d+\)$/2\)/;
	print OUT $l;
 } else {print OUT;}

}
