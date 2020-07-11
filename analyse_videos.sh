#!/bin/bash
video_dir=./examples/media/basketball
videos=`ls ${video_dir} -tr | grep 0711`
echo ${videos}
for video in ${videos}
do
    echo "processing ${video}..."
    ./build/examples/tutorial_api_cpp/my_code.bin -video_file=${video_dir}/${video} >  ${video}.data
done
