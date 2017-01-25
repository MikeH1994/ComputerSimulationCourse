import numpy as np
import matplotlib.pyplot as plt

basisVectors = [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]
minVectorComponent = 1.0
maxVectorComponent = 1.0

def getNIonsInRadius(radius,sieve):
	nIons = 0
	k = int (radius+1)
	for index1 in range(-k,k+1):
		for index2 in range(-k,k+1):
			for index3 in range(-k,k+1):
				x,y,z = getCoordFromBasis(index1,index2,index3)
				if getDistanceFromOrigin(x,y,z)<radius:
					nIons+=1
	return nIons - 1
	
def getRadiusIncrement(shell):
	return (shell**2 + minVectorComponent**2)**0.5 - shell
	
def getDistanceFromOrigin(x,y,z):
	return np.sqrt(x**2 + y**2 + z**2)
	
def getCoordFromBasis(i,j,k):
	x = basisVectors[0][0]*i + basisVectors[1][0]*j + basisVectors[2][0]*k
	y = basisVectors[0][1]*i + basisVectors[1][1]*j + basisVectors[2][1]*k
	z = basisVectors[0][2]*i + basisVectors[1][2]*j + basisVectors[2][2]*k
	return x,y,z

def getMadelungConstants(endShell, printVal = True):
	sieve = []
	for i in range(3):
		subArray = []
		for j in range(2*endShell+1):
			subArray.append(False)
		sieve.append(subArray)
	nIonsInShell = []
	nShell = 1
	radius = 0
	nIonsCurr = 0
	nIonsLast = 0
	x = []
	y = []
	while nShell<=endShell:
		radius+=getRadiusIncrement(nShell)
		nIonsCurr = getNIonsInRadius(radius,sieve)
		if nIonsCurr>nIonsLast:
			nIonsInShell.append(nIonsCurr-nIonsLast)
			madelungConstant = 0
			for i in range (len(nIonsInShell)):
				madelungConstant+=pow(-1,i+1)*nIonsInShell[i]/pow(i+1,0.5)
			x.append(nShell)
			y.append(madelungConstant)
			if printVal:
				print ('Shell: {} Number of Ions: {} Radius: {} Madelung Constant: {}'.format(nShell,(nIonsCurr-nIonsLast),radius,madelungConstant))
			nShell+=1
			nIonsLast = nIonsCurr
			nIonsCurr = 0

	return x,y
	
if __name__ == "__main__":
	x,y = getMadelungConstants(20)
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(x,y)
	plt.title('Madelung Constant as a Function of Number of Shells') 
	plt.xlabel('Number of Shells')
	plt.ylabel('Madelung Constant')
	plt.show()
