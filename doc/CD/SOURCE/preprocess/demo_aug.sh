for f in "$1"/*.jpeg; do
    echo "$f" 
done | parallel -j 2 --colsep ' ' --eta "convert {1} \( +clone -background black -rotate 15 \) \
-compose Src -composite -fuzz 15% -trim -equalize -resize 299x299! \
-set filename:base "$2"_%[base]" "./%[filename:base].jpeg"

#a done | parallel -j 3 --colsep ' ' --eta "convert {1} \( +clone -background black -rotate 15 \) \
#b done | parallel -j 3 --colsep ' ' --eta "convert {1} \( +clone -background black -rotate -15 \) \
#c done | parallel -j 3 --colsep ' ' --eta "convert {1} \( +clone -background black -page +64+0 -rotate 15 \) \
#d done | parallel -j 1 --colsep ' ' --eta "convert {1} \( +clone -background black -page +64+0 -rotate -20 \) \
#e done | parallel -j 1 --colsep ' ' --eta "convert {1} \( +clone -background black -page +64+0 -rotate 20 \) \