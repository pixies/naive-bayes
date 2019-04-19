from srcbase.nbayes import *
import sys

param = sys.argv[1:][0]

#r'databasedir/pima-indians-diabetes.data.csv'
def main():
	testSet = loadCsv(param)
	#splitRatio = 0.67
	dataset = loadCsv("tmp/test.csv")
	trainingSet = dataset
	#trainingSet, testSet = splitDataset(dataset, splitRatio)
	#testSet = loadCsv("testeSet.csv")
	print('Split {0} rows into train={1} and test={2} rows').format(len(dataset), len(trainingSet), len(testSet))
	# prepare model
	

	summaries = summarizeByClass(trainingSet)
	# test model
	#print(len(summaries[1.0]))
	##print(len(summaries[2.0]))
	#print(len(summaries[3.0]))
	#print(len(summaries[4.0]))

	#print(summaries)

	predictions = getPredictions(summaries, testSet)
	#print(predictions)
	accuracy = getAccuracy(testSet, predictions)
	print('Accuracy: {0}%').format(accuracy)

main()
