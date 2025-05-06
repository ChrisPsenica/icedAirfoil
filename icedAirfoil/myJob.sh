#!/bin/bash

#SBATCH --time=001:00:00                    # walltime limit (HH:MM:SS)
#SBATCH --nodes=2                           # number of nodes
#SBATCH --ntasks-per-node=36                # 36 processor core(s) per node 
#SBATCH --job-name="icedAF"                 # job name
#SBATCH --output="log-%j.txt"               # job standard output file (%j replaced by job id)
#SBATCH --constraint=intel                  # use intel cores to avoid bad termination on HPC
#SBATCH --mail-user=cpsenica@iastate.edu    # who to email when the job is done
#SBATCH --mail-type=ALL                     # mail type

# =============================================================================
# Load Modules
# =============================================================================
. /work/phe/ChrisPsenica/DAFoam/cpsenica/loadDAFoam.sh

# Check if the OpenFOAM enviroments are loaded
if [ -z "$WM_PROJECT" ]; then
  echo "OpenFOAM environment not found, forgot to source the OpenFOAM bashrc?"
  exit
fi

# =============================================================================
# Run Codes
# =============================================================================
#---------- Preprocessing ----------
cp -r 0.orig 0
#fluent3DMeshToFoam icedAirfoilMesh4.msh
#createPatch -overwrite
renumberMesh -overwrite

#---------- runScript.py ----------
mpirun -np 72 python runScript.py -optimizer=SNOPT

#---------- Reconstruct ----------
reconstructPar  && rm -rf processor*