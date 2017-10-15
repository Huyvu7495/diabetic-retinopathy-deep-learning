cd labeled_1-4/1

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +128+0 -rotate 12 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sright_pos_aa_%[base]" "../../aug/1/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +128+0 -rotate -12 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sright_neg_ab_%[base]" "../../aug/1/%[filename:base].jpeg""

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+128 -rotate 5 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_ac_%[base]" "../../aug/1/%[filename:base].jpeg""


cd ../..







