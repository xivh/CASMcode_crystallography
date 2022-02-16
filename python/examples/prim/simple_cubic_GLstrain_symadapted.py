import numpy as np
import casm.xtal as xtal
from math import sqrt

# Lattice vectors
lattice_column_vector_matrix = np.array([
    [1., 0., 0.], # a
    [0., 1., 0.], # a
    [0., 0., 1.]] # a
    ).transpose() # <--- note transpose
lattice = xtal.Lattice(lattice_column_vector_matrix)

# Basis sites positions, as columns of a matrix,
# in fractional coordinates with respect to the lattice vectors
coordinate_frac = np.array([
    [0., 0., 0.]]).transpose()  # coordinates of basis site, b=0

# Occupation degrees of freedom (DoF)
occ_dof = [
    ["A"]  # occupants allowed on basis site, b=0
]

# Global continuous degrees of freedom (DoF)
GLstrain_dof = xtal.DoFSetBasis(
    dofname="GLstrain",
    axis_names=["e_{1}", "e_{2}", "e_{3}", "e_{4}", "e_{5}", "e_{6}"],
    basis=np.array([
        [1./sqrt(3), 1./sqrt(3), 1./sqrt(3), 0.0, 0.0, 0.0],
        [1./sqrt(2), -1./sqrt(2), 0.0, 0.0, 0.0, 0.0],
        [-1./sqrt(6), -1./sqrt(6), 2./sqrt(6), 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]]).transpose())
global_dof = [GLstrain_dof]

# Construct the prim
prim = xtal.Prim(lattice=lattice, coordinate_frac=coordinate_frac, occ_dof=occ_dof,
                 global_dof=global_dof, title="simple_cubic_GLstrain_symadapted")

# Print the factor group
i = 1
factor_group = prim.make_factor_group()
for op in factor_group:
    syminfo = xtal.SymInfo(op, lattice)
    print(str(i) + ":", syminfo.brief_cart())
    i += 1

# Format as JSON
with open('../../doc/examples/prim/json/simple_cubic_GLstrain_symadapted.json', 'w') as f:
    f.write(prim.to_json())
