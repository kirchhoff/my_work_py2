#coding=utf-8
'''
max: 2 * x1 + 5 * x2
约束：
1.  2 * x1 - x2 <= 4
2.  x1 + 2 * x2 <= 9
3.  -x1 + x2 <= 3
'''
from pulp import *

prob = LpProblem('lptest', LpMaximize)

x1 = LpVariable('x1', lowBound=0)
x2 = LpVariable('x2', lowBound=0)

prob += 2 * x1 + 5 * x2

prob += 2 * x1 - x2 <= 4
prob += x1 + 2 * x2 <= 9
prob += -x1 + x2 <= 3
prob.solve(GLPK("C:/usr/glpk-4.61/w64/glpsol.exe"))

for v in prob.variables():
    print v.name, '=', v.varValue

print 'objective =', value(prob.objective)


