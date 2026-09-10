######################################################################

$catwords = "";
$nonwhite = 0;

sub do_file {
  local(*INFILE, *NEWFILE);

  *INFILE = $_[0];
  foreach(<INFILE>) {
    if(/^[\s]*\#[\s]*define[\s]+[\w]+[\s]*$/) {
      chomp;
      $name = $_;
      $name =~ s/^[\s]*\#[\s]*define[\s]+([\w]+)[\s]*$/$1/g;
      $arefs{$name} = "";
      if($catwords ne "") {
	$catwords .= "|" . $name;
      }
      else {
	$catwords = $name;
      }
    }
    elsif(/^[\s]*\#[\s]*define[\s]+[\w]+[\s]+[\S]+.*$/) {
      chomp;
      $name = $_;
      $name =~ s/^[\s]*\#[\s]*define[\s]+([\w]+)[\s]+[\S]+.*$/$1/g;
      $value = $_;
      $value =~ s/^[\s]*\#[\s]*define[\s]+[\w]+[\s]+([\S]+.*)$/$1/g;
      $arefs{$name} = $value;
      if($catwords ne "") {
	$catwords .= "|" . $name;
      }
      else {
	$catwords = $name;
      }      
    }
    elsif(/^[\s]*\#[\s]*include[\s]+\"[\S]+\"[\s]*$/) {
      $file = $_;
      $file =~ s/^[\s]*\#[\s]*include[\s]+\"([\S]+)\"[\s]*$/$1/g;
      open(NEWFILE, $file);
      &do_file(*NEWFILE{IO});
    }
    else {
      $line = $_;
      if($catwords ne "") {
        while($line =~ /.*\b($catwords)\b.*/) {
	  $line =~ s/\b($catwords)\b/$arefs{$1}/egos;
        }
      }
      if (!$nonwhite && $line ne "\n") {
	  $nonwhite = 1;
      }
      if ($nonwhite) {
	  print STDOUT "$line";
      }
    }
  }

}

&do_file(STDIN);

######################################################################

