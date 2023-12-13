#!/bin/bash 
#SBATCH -p gpu 
#SBATCH -c 10
#SBATCH -t 12:00:00
#SBATCH -G 1
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err
#SBATCH --mail-type=ALL

ml python/3.9
python3 -m RANCH_cluster.stanford_tools.run_stanford_cluster RANCH_cluster/sim_info/param_info/surprisal.csv RANCH_cluster/sim_info/trial_info/trial_info.csv

