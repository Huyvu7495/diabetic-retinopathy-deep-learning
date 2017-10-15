cd labeled_2/1

# for f in *.jpeg; do
    # echo "$f" 
# done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +128+0 -rotate 5 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sright_pos_rotate_%[base]" "../../resize/%[filename:base].jpeg""


# for f in *.jpeg; do
    # echo "$f" 
# done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +128+0 -rotate -10 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sright_neg_rotate_%[base]" "../../resize/%[filename:base].jpeg""

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+128 -rotate 10 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_rotate_%[base]" "../../resize/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+128 -rotate -5 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_neg_rotate_%[base]" "../../resize/%[filename:base].jpeg""

cd ../..










