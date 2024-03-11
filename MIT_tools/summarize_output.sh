#!/bin/bash -l
#SBATCH --mail-type=END
#SBATCH -n 1 
#SBATCH --mem=8GB
#SBATCH --time=01:00:00
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err

input_path="RANCH_cluster/cache_results"
output_path="RANCH_cluster/summarized_output_EIG_adults.csv"
cmd="python -m RANCH_cluster.summarize_output $input_path $output_path"

echo $cmd 

$cmd
