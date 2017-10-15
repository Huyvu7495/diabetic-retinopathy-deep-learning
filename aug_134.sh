cd labeled_1-4/4

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +128+0 -rotate 10 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sright_pos_aa_%[base]" "../../aug/4/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +128+0 -rotate -5 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sright_neg_ab_%[base]" "../../aug/4/%[filename:base].jpeg""

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+128 -rotate 5 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_ac_%[base]" "../../aug/4/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+128 -rotate -10 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_neg_ad_%[base]" "../../aug/4/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +64+0 -rotate 12 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sright_pos_ae_%[base]" "../../aug/4/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +64+0 -rotate -12 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sright_neg_af_%[base]" "../../aug/4/%[filename:base].jpeg""

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+64 -rotate 8 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_ag_%[base]" "../../aug/4/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+64 -rotate -8 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_neg_ah_%[base]" "../../aug/4/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+64 -rotate 12 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_ag_%[base]" "../../aug/4/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+64 -rotate -12 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_neg_ah_%[base]" "../../aug/4/%[filename:base].jpeg""


cd ../..


cd labeled_1-4/3

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +128+0 -rotate 10 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sright_pos_aa_%[base]" "../../aug/3/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +128+0 -rotate -5 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sright_neg_ab_%[base]" "../../aug/3/%[filename:base].jpeg""

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+128 -rotate 5 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_ac_%[base]" "../../aug/3/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+128 -rotate -10 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_neg_ad_%[base]" "../../aug/3/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +64+0 -rotate 12 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sright_pos_ae_%[base]" "../../aug/3/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +64+0 -rotate -12 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sright_neg_af_%[base]" "../../aug/3/%[filename:base].jpeg""

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+64 -rotate 8 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_ag_%[base]" "../../aug/3/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+64 -rotate -8 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_neg_ah_%[base]" "../../aug/3/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+64 -rotate 12 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_ag_%[base]" "../../aug/3/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+64 -rotate -12 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_neg_ah_%[base]" "../../aug/3/%[filename:base].jpeg""

cd ../..







