#!/bin/bash -l
#SBATCH --mail-type=END
#SBATCH -n 1 
#SBATCH --mem=8GB
#SBATCH --time=05:00:00
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err

input_path="RANCH_cluster/cache_results_new"
output_path="RANCH_cluster/runbyrun.csv"
cmd="python -m RANCH_cluster.summarize_output $input_path $output_path"

echo $cmd 

$cmd
