from hashlib import new


def read_matrix(filename):
    file = open(filename, 'r')
    mat = []
    m = 0
    for line in file:
        m = m + 1
        n = 0
        cells = line.strip()
        row = []
        for cell in cells:
            if cell != ' ':
                row.append(int(cell))
                n = n + 1
        mat.append(row)
    return mat, m, n


I, m, n = read_matrix("small_planets.txt")

print(str(m) + " " + str(n))
#for i in range(m):
#    print(mat[i])
#print(mat[1][1])

r_new = 0

A = []
B = []
for i in range(13):
    A.append([])
    B.append([])
A[0] = [i for i in range(0,m)]
B[0] = []
#print(A[0])

def IsCanonical(r, y):
    global r_new, I, A, B, m, n
    for k in range(len(B[r])-1, 0, -1):
        for j in range(y, B[r][k] + 1, -1):
            h = 0
            while h < len(A[r_new]):
                if I[A[r_new][h]][j] == 0:
                    break
                h = h + 1
            if h == len(A[r_new]):
                return False
        y = B[r][k] - 1 
    
    for j in range(y, 0, -1):
        h = 0
        while h < len(A[r_new]):
            if not I[A[r_new][h]][j]:
                break
            h = h + 1
        if h == len(A[r_new]):
            return False
    return True


r_new = 0
def InClose(r, y):
    global r_new, A, B, I, m, n
    r_new = r_new + 1
    for j in range(y, n):
        A[r_new] = []
        for i in A[r]:
            if I[i][j] == 1:
                A[r_new].append(i)
        if len(A[r_new]) > 0:
            if len(A[r_new]) == len(A[r]):
                B[r].append(j)
            else:
                #print(B[r])
                if IsCanonical(r, j-1):
                    for atr in B[r]:
                        B[r_new].append(atr)
                    B[r_new].append(j)
                    InClose(r_new, j+1)
                    
InClose(0, 0)

dict_obj = {0:"Jupiter",
            1:"Mars",
            2:"Mercury",
            3:"Neptune",
            4:"Pluto",
            5:"Saturn",
            6:"Earth",
            7:"Uranus",
            8:"Venus"}

dict_atr = {0:"small",
            1:"medium",
            2:"large",
            3:"near",
            4:"far",
            5:"yes",
            6:"no"}

for r in range(12):
    print("------------------")
    print("A=")
    print([dict_obj[A[r][i]] for i in range(len(A[r]))])
    print("B=")
    print([dict_atr[B[r][i]] for i in range(len(B[r]))])
    print("------------------")
    
