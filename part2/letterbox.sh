#!/bin/bash 

if [ ! -f aspect43.mp4 ]; then
    echo "Input not found, downloading:"
    curl "https://imgcdn.sports.aparentmedia.com/test/aspect43.mp4" -o aspect43.mp4
fi


ffmpeg -i aspect43.mp4 \
-vf pad="width=in_h*16/9:height=in_h:x=(out_w-in_w)/2:y=(out_h-in_h)/2:color=black" \
-c:a copy \
aspect169.mp4




