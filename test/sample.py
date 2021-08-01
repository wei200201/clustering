from numpy import *
import pylab as plt

# Make a block diagonal matrix
N = 30
c = 5
A = zeros((N*c,N*c))
for m in range(c):
    A[m*N:(m+1)*N, m*N:(m+1)*N] = random.random((N,N))

print(A)

# Add some noise
A += random.random(A.shape) * 0.1

print(A)


# Make symmetric
A += A.T - diag(A.diagonal())

print("\n")
print(A)

# Show the original matrix
plt.subplot(131)
plt.imshow(A.copy(), interpolation='nearest')
plt.show()

'''
# Permute the matrix for effect
idx = random.permutation(N*c)
A = A[idx,:][:,idx]

# Compute eigenvalues
L = linalg.eigvalsh(A)

# Show the results
plt.subplot(132)
plt.imshow(A, interpolation='nearest')
plt.subplot(133)
plt.plot(sorted(L,reverse=True))

plt.plot([c-.5,c-.5],[0,max(L)],'r--')

plt.ylim(0,max(L))
plt.xlim(0,20)
plt.show() 
'''
