cd labeled_2/1

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 3 --colsep ' ' --eta convert {1} -background black -rotate 10 -fuzz 15% -trim -equalize -set filename:base "pos_rotate_%[base]" "../../resize/%[filename:base].jpeg"


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 3 --colsep ' ' --eta convert {1} -background black -rotate -10 -fuzz 15% -trim -equalize -set filename:base "neg_rotate_%[base]" "../../resize/%[filename:base].jpeg"

cd ../..




