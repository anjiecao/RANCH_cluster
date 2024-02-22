#!/bin/bash -l

project_path="/om2/scratch/tmp/galraz/RANCH/RANCH_cluster"

param_info=$project_path/sim_info/param_info/adults/eig.csv
trial_info="RANCH_cluster/sim_info/trial_info/exposure_duration/adults/trial_info.csv"
embedding_info="RANCH_cluster/sim_info/embeddings/resnet_pa.csv"

param_dir=$project_path/MIT_tools/param_dir

# code that takes eig.csv and creates different files for each row
cmd="python $project_path/MIT_tools/populate_param_dir.py $param_info"

$cmd

param_vals=($(find $param_dir/ -type f))

len=$(expr ${#param_vals[@]} - 1) 

cmd="sbatch --array=0-$len $project_path/MIT_tools/MIT_single_job.sh $project_path $trial_info $embedding_info ${param_vals[@]}" 

$cmd

