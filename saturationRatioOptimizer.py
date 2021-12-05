# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cvxpy as cp
F = cp.Variable(31, boolean=True)

obj_func = (0.6*F[0] + 1.2*F[1] + 1.2*F[2]  
          + 1.2*F[3] + 1.2*F[4]  + 0.2*F[5]
          + 1.2*F[6] + 0.6*F[7] + 1.2*F[8]  
          + 1.6*F[9] + 1.6*F[10] + 1.2*F[11] 
          + 1.6*F[12] + 0.2*F[13] + 0.6*F[14] 
          + 0.2*F[15] + 0.6*F[16] + 1.2*F[17]
          + 0.6*F[18] + 0.6*F[19] + 0.2*F[20]
          + 0.6*F[21] + 1.2*F[22] + 0.6*F[23] 
          + 0.6*F[24] + 0.6*F[25] + 0.6*F[26] 
          + 0.6*F[27] + 0.2*F[28] + 0.2*F[29]
          + 1.6*F[30])

constraints = []
constraints.append(F[0]  + F[1]  + F[2]  + F[3]  + F[4]  + F[5]  
                 + F[6]  + F[7]  + F[8]  + F[9]  + F[10] + F[11] 
                 + F[12] + F[13] + F[14] + F[15] + F[16] + F[17] 
                 + F[18] + F[19] + F[20] + F[21] + F[22] + F[23] 
                 + F[24] + F[25] + F[26] + F[27] + F[28] + F[29] 
                 + F[30]  == 5)

constraints.append(F[1] + F[8] + F[9] + F[10] + F[11] + F[12] <= 2)

constraints.append(F[0] + F[2] + F[6] + F[7] + F[16] + F[19] <= 1)
    
problem = cp.Problem(cp.Maximize(obj_func), constraints)

problem.solve(solver=cp.GUROBI, verbose = True)

print("obj_func =")
print(obj_func.value)
print("F =")
print(F.value)

