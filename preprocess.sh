input=$1"*"
output=$2
for f in $input; do
    for f1 in f; do
        fname=$(basename "$f")    
        echo $f $output$fname
        ./lib/imgtxtenh -d 118.100 $f | convert png:- -deskew 40% -bordercolor white -border 5 -trim -strip $output$fname
    done
done    
