#!/bin/sh
#SBATCH --partition=CPUQ
#SBATCH --account=share-ie-imf
#SBATCH --time=6-12:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --mem=12000
#SBATCH --job-name="9to12opp"
#SBATCH --output=9to12opp.out
#SBATCH --mail-user=emilamy@stud.ntnu.no
#SBATCH --mail-type=ALL

module load GCCcore/.9.3.0
module load Python/3.8.2

source ../../datasci/bin/activate

python3 Noisebias3.py
