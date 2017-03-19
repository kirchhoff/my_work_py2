#coding=utf-8

from pulp import *

prob = LpProblem('lptest', LpMaximize)

x1 = LpVariable('x1', lowBound=0)
x2 = LpVariable('x2', lowBound=0)
y1 = LpVariable('y1', lowBound=0)
y2 = LpVariable('y2', lowBound=0)

prob += x1+x2+y1+y2, "problem description"

prob += 1*x1 + 3*y1 <= 1, ""
prob += 1*x1 + 2*y1 <= 2,""
prob += 1*x2 + 3*y2 <= 4,""
prob += 1*x2 + 2*y2 <= 3,""
#for DRF
prob += (x1+x2)-3*(y1+y2) == 0 ,""#DRFH

'''
#per-server partitioning
prob += x1*1 <= 0.5
prob += y1*3 <=0.5
prob += x1*1 <= 1
prob += y1*2 <= 1
prob += x2*1 <=2
prob += y2*3 <=2
prob += x2*1 <= 1.5
prob += y2*2 <= 1.5
'''
#prob.solve(GLPK("C:/usr/glpk-4.61/w64/glpsol.exe"))
prob.solve()

print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print v.name, '=', v.varValue

print 'objective =', value(prob.objective)


