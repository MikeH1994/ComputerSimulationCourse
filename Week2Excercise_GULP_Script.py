import os
import numpy as np
import matplotlib.pyplot as plt

structures = ["Mg_O","Ca_O","Sr_O","Cs_Cl"]
argsLine1 = "single prop"
argsLine2 = "cell"
argsLine3_part = "90.000000  90.000000  90.000000 1 0 0 0 0 0"
argsLine4 = "fractional    3"
argsLine5_part = "core  0.000000   0.000000   0.000000    2.000000 1.0000 0.00000 0 0 0"
argsLine6_part = "shel  0.000000   0.000000   0.000000    2.000000 1.0000 0.00000 0 0 0"
argsLine7_part = "core  0.500000   0.500000   0.500000    0.800000 1.0000 0.00000 0 0 0"
argsLine8_part = "shel  0.500000   0.500000   0.500000   -2.800000 1.0000 1.12468 0 0 0"
argsLine9 = "space"
argsLine10 = "225"
argsLine11 = "library bush.lib"


resultsStringToSearchFor = "kJ"

inputFilename = "Week2Excercise.gin"
outputFilename = "Results.gout"

def getLatticeEnergy(structureType = "Mg_O",x1 = 4.212000, y1 = 4.212000, z1 = 4.212000):
	structureType = structureType.split("_")
	element1 = structureType[0]
	element2 = structureType[1]
	print(('Structure: {}{}; Basis Vectors [{},{},{}])\n').format(element1,element2,x1,y1,z1))
	
	f = open(inputFilename,'w')
	f.write(('{}\n').format(argsLine1))
	f.write(('{}\n').format(argsLine2))
	f.write(('\t{}\t{}\t{}\t{}\n').format(x1,y1,z1,argsLine3_part))
	f.write(('{}\n').format(argsLine4))
	f.write(('{}\t{}\n').format(element1,argsLine5_part))
	f.write(('{}\t{}\n').format(element1,argsLine6_part))
	f.write(('{}\t{}\n').format(element2,argsLine7_part))
	f.write(('{}\t{}\n').format(element2,argsLine8_part))
	f.write(('{}\n').format(argsLine9))
	f.write(('{}\n').format(argsLine10))
	f.write(('{}\n').format(argsLine11))
	f.close()
	os.system(('../gulp-linux <{}> {}').format(inputFilename,outputFilename))
	
	resultsFile = open(outputFilename)
	#Primitive unit cell  kJ/(mole unit cells)
	resultsFileContent = resultsFile.read().split(resultsStringToSearchFor)[1].split("\\s")[-1].split("=")[1].strip()
	resultsFile.close()
	print(('Structure: {}{}; Basis Vectors [{},{},{}]; energy: {} kJ/(mole unit cells)\n').format(element1,element2,x1,y1,z1,resultsFileContent))
	return float(resultsFileContent)
	
if __name__ == "__main__":
	fig = plt.figure()
	colors = ["red","green","blue","black"]
	for i in range(len(structures)-1):
		xData = []
		yData = []
		for x in np.arange(3,5,0.2):
			xData.append(x*x*x)
			yData.append(getLatticeEnergy(structures[i],x,x,x))
		plt.plot(xData,yData,color = colors[i],label = structures[i])
	plt.title("Lattice Energy as a f'n of volume") 
	plt.xlabel('Volume')
	plt.ylabel('Lattice energy (kJ/mole unit cells)')
	plt.legend(loc = 0)
	plt.show()
