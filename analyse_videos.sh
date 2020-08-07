#!/bin/bash
video_dir=./examples/media/basketball
data_dir=./postdata
#videos=`ls ${video_dir} -tr | grep 0712`
videos="curry_cs.mp4"
echo ${videos}
for video in ${videos}
do
    echo "processing ${video}..."
    ./build/examples/tutorial_api_cpp/my_code.bin -video_file=${video_dir}/${video} -write_video=${video_dir}/op_${video}>  ${data_dir}/${video}.data
done
