from liblll import * 
import numpy as np

# LLL
mat1 = LLLasMatCol()
print("Example 1 : ")
mat1 = create_matrix(mat1)
print("mat1 : ")
print_mat(mat1)
print("mat1 is lll ? ", islll(mat1))
print()

v_1 = [ float(mat1[0][0]), float(mat1[1][0]), float(mat1[2][0])]
v_2 = [ float(mat1[0][1]), float(mat1[1][1]), float(mat1[2][1])]
v_3 = [ float(mat1[0][2]), float(mat1[1][2]), float(mat1[2][2])]

print(v_1)
print(v_2)
print(v_3)
print()

# GAUSS
mat2 = GaussMatCol()
print("Example 1 : ")
mat2 = create_matrix(mat2)
print("mat2 : ")
print_mat(mat2)
print("mat2 is gauss reduced ? ", islll(mat2))
print()
u_1 = [ float(mat2[0][0]), float(mat2[1][0]) ]
u_2 = [ float(mat2[0][1]), float(mat2[1][1]) ]
print(u_1)
print(u_2)
