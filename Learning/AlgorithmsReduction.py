import numpy as np

def gaussian_lattice_reduction(v1, v2):
    while True:
        m_v1 = np.linalg.norm(v1)
        m_v2 = np.linalg.norm(v2)

        if m_v2 < m_v1:
            aux = v1
            v1 = v2
            v2 = aux

        m_v1 = np.linalg.norm(v1)
        m = np.dot(v1, v2) / (m_v1 ** 2)

        if m == 0:
            return v1, v2

        v2 = v2 - (m * v1)


def gram_schmidt(v_1, v_2):
    basis = []
    for v in range(2):
        w = v - np.sum( np.dot(v,b)*b  for b in basis )
        if (w > 1e-10).any():
            basis.append(w/np.linalg.norm(w))
    return np.array(basis)


def mu(v1, v2):
    return (np.dot(v1, v2)) / np.linalg.norm(v2) ** 2


def lll_lattice_reduction(basis):
    k = 1
    v = basis

    while k <= len(basis):  # k <= n, n is size of basis
        for j in range(k-1, 1):
            v[k] = v[k] - ((mu(v[k], v[j])) * v[j])

        v_o = gram_schmidt(v)

        if np.linalg.norm(v_o[k]) ** 2 >= (0.75 - (mu(v[k], v_o[k-1]))**2) * (np.linalg.norm(v_o[k-1]) ** 2):
            k = k + 1

        else:
            tmp = v[k-1]
            v[k-1] = v[k]
            v[k] = tmp

            k = max(k-1, 2)

    return v

if __name__ == '__main__':
        m = []
        n = []

        for i in range(2):
            i = float( input("Ingrese los escalares del primer vector, entrada ["+str(i+1)+"] : "))
            m.append(i)
        print("")

        for j in range(2):
            j = float( input("Ingrese los escalares del segundo vector, entrada ["+str(j+1)+"] : "))
            n.append(j)

        v_1 = np.array(m)
        v_2 = np.array(n)
        
        v_11 = int(gaussian_lattice_reduction(v_1, v_2)[0][0])
        v_12 = int(gaussian_lattice_reduction(v_1, v_2)[0][1])
        

        print())
        print("\n")
        print(gaussian_lattice_reduction(v_1, v_2)[1]))

