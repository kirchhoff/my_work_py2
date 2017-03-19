# coding=utf-8
"""
The Simplified Whiskas Model Python Formulation for the PuLP Modeller

Authors: wdtang@smail.nju.edu.cn 汤闻达
"""
from pulp import *

prob = LpProblem("test_problem", LpMinimize)  # 问题的名字，最大还是最小,LpMaximize
# The problem variables x1 and x2 are created using the LpVariable class. It has four parameters, the first is the
# arbitrary name of what this variable represents, the second is the lower bound on this variable, the third is the
# upper bound, and the fourth is essentially the type of data (discrete or continuous). The options for the fourth
# parameter are LpContinuous or LpInteger, with the default as LpContinuous. If we were modelling the number of cans to
# produce, we would need to input LpInteger since it is discrete data. The bounds can be entered directly as a number,
# or None to represent no bound (i.e. positive or negative infinity), with None as the default.

# The 2 variables Beef and Chicken are created with a lower limit of zero
# 变量的名字，下界，上届，离散还是连续 LpContinuous
x1 = LpVariable("ChickenPercent", 0, None, LpInteger)
x2 = LpVariable("BeefPercent", 0)
# The objective function is added to 'prob' first
prob += 0.013 * x1 + 0.008 * x2, "Total Cost of Ingredients per can"

# The five constraints are entered
prob += x1 + x2 == 100, "PercentagesSum"
prob += 0.100 * x1 + 0.200 * x2 >= 8.0, "ProteinRequirement"
prob += 0.080 * x1 + 0.100 * x2 >= 6.0, "FatRequirement"
prob += 0.001 * x1 + 0.005 * x2 <= 2.0, "FibreRequirement"
prob += 0.002 * x1 + 0.005 * x2 <= 0.4, "SaltRequirement"

# The problem data is written to an .lp file
prob.writeLP("WhiskasModel.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()
# “Not Solved”, “Infeasible”, “Unbounded”, “Undefined” or “Optimal”.
# The status of the solution is printed to the screen
print "Status:", LpStatus[prob.status]

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print v.name, "=", v.varValue

# The optimised objective function value is printed to the screen
print "Total Cost of Ingredients per can = ", value(prob.objective)

