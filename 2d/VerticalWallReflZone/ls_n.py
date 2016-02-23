from proteus.default_n import *
import ls_p as physics
from proteus import (StepControl,
                     TimeIntegration,
                     NonlinearSolvers,
                     LinearSolvers,
                     LinearAlgebraTools)
from proteus.mprans import NCLS
from proteus import Context
ct = Context.get()

runCFL = ct.runCFL
nLevels = ct.nLevels
parallelPartitioningType = ct.parallelPartitioningType
nLayersOfOverlapForParallel = ct.nLayersOfOverlapForParallel
restrictFineSolutionToAllMeshes = ct.restrictFineSolutionToAllMeshes
triangleOptions = ct.triangleOptions

timeIntegration = TimeIntegration.BackwardEuler_cfl
stepController  = StepControl.Min_dt_controller

femSpaces = {0: ct.basis}
elementQuadrature = ct.elementQuadrature
elementBoundaryQuadrature = ct.elementBoundaryQuadrature

massLumping       = False
conservativeFlux  = None # {0:'pwl-bdm-opt'} 
numericalFluxType = NCLS.NumericalFlux
subgridError      = NCLS.SubgridError(coefficients=physics.coefficients,
                                      nd=ct.domain.nd)
shockCapturing    = NCLS.ShockCapturing(physics.coefficients,
                                        ct.domain.nd,
                                        shockCapturingFactor=ct.ls_shockCapturingFactor,
                                        lag=ct.ls_lag_shockCapturing)

fullNewtonFlag  = True
multilevelNonlinearSolver = NonlinearSolvers.Newton
levelNonlinearSolver      = NonlinearSolvers.Newton

nonlinearSmoother = None
linearSmoother    = None

matrix = LinearAlgebraTools.SparseMatrix

if ct.useOldPETSc:
    multilevelLinearSolver = LinearSolvers.PETSc
    levelLinearSolver      = LinearSolvers.PETSc
else:
    multilevelLinearSolver = LinearSolvers.KSP_petsc4py
    levelLinearSolver      = LinearSolvers.KSP_petsc4py
if ct.useSuperlu:
    multilevelLinearSolver = LinearSolvers.LU
    levelLinearSolver      = LinearSolvers.LU

linear_solver_options_prefix = 'ncls_'
levelNonlinearSolverConvergenceTest = 'r'
linearSolverConvergenceTest         = 'r-true'

tolFac = 0.0
linTolFac = 0.001
l_atol_res = 0.001*ct.ls_nl_atol_res
nl_atol_res = ct.ls_nl_atol_res
useEisenstatWalker = False#True

maxNonlinearIts = 50
maxLineSearches = 0
