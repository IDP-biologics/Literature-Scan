offset=$1
start=${offset}
end=$(( offset + 5 ))

NOUGAT_PATH=/rbscratch/brettin/DepMap-Experiments/tool_collection/pull_papers

echo "$(date) START"

for n in $(seq $start $end) ; do 
	device=$(( n % 8 ))
	echo "CUDA_VISIBLE_DEVICES=$device python $NOUGAT_PATH//nougat_pdf.py ./chunks/$n/"
	#CUDA_VISIBLE_DEVICES=$device python -u $NOUGAT_PATH/nougat_pdf.py ./chunks/$n/ > ./chunks/$n/log &
done

wait

echo "$(date) FINISH"
