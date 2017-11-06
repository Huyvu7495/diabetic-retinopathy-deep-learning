
cd labeled_5/4

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +128+0 -rotate 8 \) -compose Src -composite -fuzz 15% -trim -equalize -resize 42% -set filename:base "ac_%[base]" "../../resize/4/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+128 -rotate -8 \) -compose Src -composite -fuzz 15% -trim -equalize -resize 42% -set filename:base "ad_%[base]" "../../resize/4/%[filename:base].jpeg""

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+128 -rotate 10 \) -compose Src -composite -fuzz 15% -trim -equalize -resize 42% -set filename:base "aa_%[base]" "../../resize/4/%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +128+0 -rotate -10 \) -compose Src -composite -fuzz 15% -trim -equalize -resize 42% -set filename:base "ab_%[base]" "../../resize/4/%[filename:base].jpeg""

cd ../..










