for f in *.jpeg; do
    echo "$f" 
done | parallel -j 4 --colsep ' ' --eta convert {1} -fuzz 15% -trim -equalize -resize 299x299! -set filename:base "%[base]" "../../resize/"$1"/%[filename:base].jpeg"



