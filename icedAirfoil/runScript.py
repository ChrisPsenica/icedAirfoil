#!/usr/bin/env python
"""
DAFoam run script for iced and clean airfoil
"""

# =============================================================================
# Imports
# =============================================================================
from mpi4py import MPI
import os
import numpy as np
import openmdao.api as om
from mphys.multipoint import Multipoint
from dafoam.mphys import DAFoamBuilder, OptFuncs
from mphys.scenario_aerodynamic import ScenarioAerodynamic
from pygeo.mphys import OM_DVGEOCOMP
from pygeo import geo_utils
gcomm = MPI.COMM_WORLD

# =============================================================================
# Input Parameters
# =============================================================================
U0 = 20.0
p0 = 0.0
nuTilda0 = 4.5e-5
aoa0 = 0.0
A0 = 1e-3
rho0 = 1.0

# Input parameters for DAFoam
daOptions = {
    "solverName": "DASimpleFoam",
    "primalMinResTol": 1e-8,
    "primalMinResTolDiff": 1e8,
    "primalBC": {
        "U0": {"variable": "U", "patches": ["inout"], "value": [U0, 0.0, 0.0]},
        "p0": {"variable": "p", "patches": ["inout"], "value": [p0]},
        "nuTilda0": {"variable": "nuTilda", "patches": ["inout"], "value": [nuTilda0]},
        "useWallFunction": True,
    },
    "function": {

        "CD": {
            "type": "force",
            "source": "patchToFace",
            "patches": ["wing"],
            "directionMode": "fixedDirection",
            "direction": [1.0, 0.0, 0.0],
            "scale": 1.0 / (0.5 * U0 * U0 * A0 * rho0),
        },

        "CL": {
            "type": "force",
            "source": "patchToFace",
            "patches": ["wing"],
            "directionMode": "fixedDirection",
            "direction": [0.0, 0.0, 1.0],
            "scale": 1.0 / (0.5 * U0 * U0 * A0 * rho0),
        },

    },

}

# Mesh deformation setup
meshOptions = {
    "gridFile": os.getcwd(),
    "fileType": "OpenFOAM",
    "symmetryPlanes": [[[0.0, 0.0, 0.0], [0.0, 1.0, 0.0]], [[0.0, 0.005, 0.0], [0.0, 1.0, 0.0]]],
}

class Top(Multipoint):
    def setup(self):
        dafoam_builder = DAFoamBuilder(daOptions , scenario = "aerodynamic")
        dafoam_builder.initialize(self.comm)
        self.mphys_add_scenario("cruise" , ScenarioAerodynamic(aero_builder = dafoam_builder))

prob = om.Problem()
prob.model = Top()
prob.setup(mode = "rev")
prob.run_model()