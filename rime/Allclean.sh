#!/bin/bash

echo "Cleaning..."

rm -rf 0
rm -rf report*
rm -rf log-*
rm -rf postProcessing
rm -rf constant/extendedFeatureEdgeMesh
rm -rf constant/triSurface
rm -rf *.bin *.info *.dat *.xyz *.stl
rm -rf processor* 0.0*
rm -rf {1..9}*

echo "Done!"