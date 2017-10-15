cd labeled_1-4/4


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+64 -rotate 8 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_aj_%[base]" "../../aug/4/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+64 -rotate -8 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_neg_ak_%[base]" "../../aug/4/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+32 -rotate 15 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_al_%[base]" "../../aug/4/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+32 -rotate -15 \) -compose Src -composite -fuzz 16% -trim -equalize -set filename:base "sleft_neg_am_%[base]" "../../aug/4/%[filename:base].jpeg""

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+32 -rotate 8 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_an_%[base]" "../../aug/4/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+32 -rotate -8 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_neg_ao_%[base]" "../../aug/4/%[filename:base].jpeg""

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +64+0 -rotate 15 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_ap_%[base]" "../../aug/4/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +64+0 -rotate -15 \) -compose Src -composite -fuzz 17% -trim -equalize -set filename:base "sleft_neg_aq_%[base]" "../../aug/4/%[filename:base].jpeg""

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +32+0 -rotate 8 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_ar_%[base]" "../../aug/4/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +32+0 -rotate -8 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_neg_as_%[base]" "../../aug/4/%[filename:base].jpeg""


cd ../..


cd labeled_1-4/3


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+64 -rotate 8 \) -compose Src -composite -fuzz 16% -trim -equalize -set filename:base "sleft_pos_aj_%[base]"   "../../aug/3/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+64 -rotate -8 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_neg_ak_%[base]"  "../../aug/3/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+32 -rotate 15 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_al_%[base]"  "../../aug/3/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+32 -rotate -15 \) -compose Src -composite -fuzz 17% -trim -equalize -set filename:base "sleft_neg_am_%[base]" "../../aug/3/%[filename:base].jpeg""

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+32 -rotate 8 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_an_%[base]"   "../../aug/3/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+32 -rotate -8 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_neg_ao_%[base]"  "../../aug/3/%[filename:base].jpeg""

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +64+0 -rotate 15 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_ap_%[base]"  "../../aug/3/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +64+0 -rotate -15 \) -compose Src -composite -fuzz 16% -trim -equalize -set filename:base "sleft_neg_aq_%[base]"  "../../aug/3/%[filename:base].jpeg""

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +32+0 -rotate 8 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_pos_ar_%[base]"   "../../aug/3/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +32+0 -rotate -8 \) -compose Src -composite -fuzz 15% -trim -equalize -set filename:base "sleft_neg_as_%[base]"  "../../aug/3/%[filename:base].jpeg""


cd ../..







