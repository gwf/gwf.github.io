
rm -rf imageinfo.txt

for f in *.gif; do
  echo -n src='"graphics/'$f'" ' >> imageinfo.txt
  giftext $f | grep Screen | head -1 \
    | sed 's/.*Width = \([0-9]*\), Height = \([0-9]*\).*/width="\1" height="\2"/g' \
    >> imageinfo.txt
done

for f in *.jpg; do
  echo -n src='"graphics/'$f'" ' >> imageinfo.txt
  ( jpegtran -v $f > /dev/null ) 2>&1 | grep width \
    | sed 's/.*width=\([0-9]*\), height=\([0-9]*\).*/width="\1" height="\2"/g' \
    >> imageinfo.txt
done

sed 's/"/\\"/g' imageinfo.txt \
  | awk '{OFS=""; print "(tags-query-replace \"", $1, "\" \"", $1, " ", $2, " ", $3, "\" nil)"}' \
  > imagestuff.el
