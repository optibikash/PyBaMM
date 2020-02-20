#
# Example showing how to load and solve the SPMe
#

import pybamm
import numpy as np

pybamm.set_logging_level("DEBUG")

# load model
model = pybamm.lithium_ion.SPMe()
model.convert_to_format = "python"

# create geometry
geometry = model.default_geometry

# load parameter values and process model and geometry
param = model.default_parameter_values
param.process_model(model)
param.process_geometry(geometry)

# set mesh
mesh = pybamm.Mesh(geometry, model.default_submesh_types, model.default_var_pts)

# discretise model
disc = pybamm.Discretisation(mesh, model.default_spatial_methods)
disc.process_model(model)

# solve model for 1 hour
t_eval = np.linspace(0, 3600, 100)
solution = model.default_solver.solve(model, t_eval)

# plot
overpotentials = [
        "X-averaged reaction overpotential [V]",
        "X-averaged concentration overpotential [V]",
        "X-averaged electrolyte ohmic losses [V]",
        "X-averaged solid phase ohmic losses [V]",
        "Change in measured open circuit voltage [V]",
        "Local ECM resistance [Ohm]"
    ]
plot = pybamm.QuickPlot(solution, output_variables=overpotentials)
plot.dynamic_plot()
