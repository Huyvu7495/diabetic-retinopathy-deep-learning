cd labeled_2/1

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +0+256 \) -compose Src -composite -fuzz 15% -trim -set filename:base "../ab/ab_%[base]" "./%[filename:base].jpeg""


for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta "convert {1} \( +clone -background black -page +256+0 \) -compose Src -composite -fuzz 15% -trim -set filename:base "../aa/aa_%[base]" "./%[filename:base].jpeg""

cd ../..







