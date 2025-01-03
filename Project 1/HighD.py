from math import *
import random
from numpy import *
import matplotlib.pyplot as plt
import datasets

waitForEnter=False

def generateUniformExample(numDim):
    return [random.random() for d in range(numDim)]

def generateUniformDataset(numDim, numEx):
    return [generateUniformExample(numDim) for n in range(numEx)]

def computeExampleDistance(x1, x2):
    dist = 0.0
    for d in range(len(x1)):
        dist += (x1[d] - x2[d]) * (x1[d] - x2[d])
    return sqrt(dist)

def computeDistances(data):
    N = len(data)
    D = len(data[0])
    dist = []
    for n in range(N):
        for m in range(n):
            dist.append( computeExampleDistance(data[n],data[m])  / sqrt(D))
    return dist

# N    = 200                   # number of examples
# Dims = [2, 8, 32, 128, 512]   # dimensionalities to try
# Cols = ['#FF0000', '#880000', '#000000', '#000088', '#0000FF']
Bins = arange(0, 1, 0.02)
Cols = ['#FF0000']

# plt.xlabel('distance / sqrt(dimensionality)')
# plt.ylabel('# of pairs of points at that distance')
# plt.title('dimensionality versus uniform point distances')

# for i,d in enumerate(Dims):
#     distances = computeDistances(generateUniformDataset(d, N))
#     print("D=%d, average distance=%g" % (d, mean(distances) * sqrt(d)))
#     plt.hist(distances,
#              Bins,
#              histtype='step',
#              color=Cols[i])
#     if waitForEnter:
#         plt.legend(['%d dims' % d for d in Dims])
#         plt.show(False)
#         x = input('Press enter to continue...')


# plt.legend(['%d dims' % d for d in Dims])
# plt.savefig('fig.pdf')
# plt.show()

### WU5 - PART A
plt.xlabel('distance / sqrt(dimensionality)')
plt.ylabel('# of pairs of points at that distance')
plt.title('distribution of distances with d=784')

distances = computeDistances(datasets.DigitData.X)
print("D=784, average distance=%g" % (mean(distances) * sqrt(784)))
plt.hist(distances,
             Bins,
             histtype='step',
             color=Cols[0])

plt.legend(['784 dims'])
plt.show()

def computeExampleDistanceSubdims(x1, x2, dims):
    dist = 0.0
    for d in dims:
        dist += (x1[d] - x2[d]) * (x1[d] - x2[d])
    return sqrt(dist)

def computeDistancesSubdims(data, d):
    N = len(data)
    D = len(data[0])
    dist = []

    dims = random.permutation(D)[:d]

    for n in range(N):
        for m in range(n):
            dist.append(computeExampleDistanceSubdims(data[n],data[m], dims)  / sqrt(d))
    return dist

### WU5 - PART C
# Dims = [2, 8, 32, 128, 512]   # dimensionalities to try
# Cols = ['#FF0000', '#880000', '#000000', '#000088', '#0000FF']

# plt.xlabel('distance / sqrt(dimensionality)')
# plt.ylabel('# of pairs of points at that distance')
# plt.title('dimensionality versus distances in natually occuring data')

# for i,d in enumerate(Dims):
#     distances = computeDistancesSubdims(datasets.DigitData.X, d)
#     print("D=%d, average distance=%g" % (d, mean(distances) * sqrt(d)))
#     plt.hist(distances,
#              Bins,
#              histtype='step',
#              color=Cols[i])
#     if waitForEnter:
#         plt.legend(['%d dims' % d for d in Dims])
#         plt.show(False)
#         x = input('Press enter to continue...')


# plt.legend(['%d dims' % d for d in Dims])
# plt.show()
