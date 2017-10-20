import numpy as np
from Data import db
from Methodes import methodes as mt

# Data
data = db.data
n = len(data['peopels'])
m = len(data['subjects'])

# Calculate Col's {moy, equart, sigma}
print(mt)
bars = mt.get_bars(data, n, m)
variances = mt.get_equartypes(data, bars, n, m)
sigmas = mt.get_sigmas(variances)


## Center
mat_centered = mt.matrix_centre(data, bars, n ,m)

print('\nMatrix')
print( '        ', ' |'.join(map(str, data['subjects'])) )
for i in range(0, n) :
    print( data['peopels'][i], data['matrix'][i])

print('\nBars')
print (bars)

print ('\nVariances')
print (variances)

print ('\nSigmas')
print (sigmas)

print ('\nCentered')
print ('         ', '     | '.join(map(str, data['subjects'])))
for i in range(0, n):
    print (data['peopels'][i], mat_centered[i] )



## Reduce
mat_reduced = mt.matrix_reduce(mat_centered, sigmas, n ,m)

print ('\nReduced')
print ('         ', '     | '.join(map(str, data['subjects'])))
for i in range(0, n):
    print (data['peopels'][i], mat_reduced[i] )


## Corelation matrix
mat_corelation = ( float(1)/float(n) ) * np.dot(np.transpose(mat_reduced), mat_reduced)

print ('\nCorealation')
print ('         ', '   | '.join(map(str, data['subjects'])))
for i in range(0, m):
    print (data['subjects'][i], mat_corelation[i] )

## eigen values & eigen vectors
eigen = np.linalg.eigh(mat_corelation)
eigen_vals = eigen[0] 
eigen_vects = eigen[1]

## eigen vectors
print ('\nEigen valuse')
print (eigen_vals )

print ('\nEigen vectors')
for i in range(0, m):
    print ('Vect{0}: '.format(i), eigen_vects[i])