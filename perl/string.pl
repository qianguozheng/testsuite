#!/usr/bin/perl

#$string = "GET xxxx.apple.com/us/xx/shit/heloo/ibmxxxsdfsdfsdfsdf.ipa?wisplost=local";
$string = "http://192.168.2.1/xxxx.apple.com/us/xx/shit/heloo/ibmxxxsdfsdfsdfsdf.ipa";
$position = index($string,".ipa");
print "$position\n";
#$position2 = index($string,".ipx");
#print "$position2\n";


#$test = $string =~/([0-9]{1,3}\.?){4}/;
#print "test = $test\n";


@all_proto = split(/\/\//, $string);
$protocal = @all_proto[0];
$new_string = @all_proto[1];

@suball = split(/\//, $new_string);
$sep = @suball[0];

@origin = split(/$sep/, $new_string);
print "origin=@origin[1]\n";
print "proto =$protocal\n";

print "New String = $protocal\/@origin[1]\n";

@all = split(/\//, $string);
$i = 0;
foreach $str (@all){
	print "$str\n";
	#if ($str=~/([0-9]{1,3}\.?){4}/)
	
	if (0 == $i)
	{
		$str = '';
		$i = 1;
	}	
	#$all2 += "$str";
}

print "\n";
print "all2=$all2\n";
if ($position > 0)
{
	print "$string\n";

	@arr = split(/\?/, $string);
	
	foreach (@arr){
		#$str2 = $_;
		#print $_,"\n";
		break;
	}
	$str2 = @arr[0];
	print "$str2\n";

	$position3 = index($str2, ".apple.com");
	if ($position3 > 0)
	{
		print "$position3\n";
		@arr2 = split(/\.apple\.com/, $str2);
		
		$str3 = @arr2[1];
		print "URI: $str3\n";	
	}

	#@arr2 = split($str2, ".apple.com");
	#print "@arr2";
	#foreach(@arr2)
	#{
		#$str2 = $_;
	#	print "$_";
	#}
	
}
