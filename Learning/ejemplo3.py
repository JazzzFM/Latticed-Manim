from liblll import * 
import numpy as np

# LLL
mat1 = LLLasMatCol()

v_1 = mat1[0]
v_2 = mat1[1]
v_3 = mat1[2]

print("Example 1 : ")
print("mat1 : ")
mat1 = create_matrix(mat1)
mat1 = lll_reduction(mat1)
print_mat(mat1)

print("mat1 is lll ? ", islll(mat1))
print()

print(v_1)
print(v_2)
print(v_3)
print()

# GAUSS
mat2 = GaussMatCol()

u_1 = mat2[0]
u_2 = mat2[1]

print("Example 1 : ")
print("mat2 : ")
mat2 = create_matrix(mat2)
print_mat(mat2)
print("mat2 is gauss reduced ? ", islll(mat2))
print()

print(u_1)
print(u_2)
