cd working

for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta convert {1} -equalize -fuzz 25% -trim -resize "1024x1024!" -set filename:base "%[base]" "../resize/%[filename:base].jpeg"

cd ..


