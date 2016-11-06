import pandas as pd 

def printFeaturesInfo(dataFrameSet,featuresToInclude=[]):
	for x in dataFrameSet.columns.values:
		if x in featuresToInclude:
			print x
			print dataFrameSet[x].value_counts()
			print list(dataFrameSet[x].value_counts().index)
			print list(dataFrameSet[x].value_counts())
			print sum(list(dataFrameSet[x].value_counts()))
			print len(list(dataFrameSet[x].value_counts().index))
			print "\n\n"

def printAllColumnNames(dataFrameSet):
	print list(dataFrameSet.columns.values)
	return list(dataFrameSet.columns.values)

def oneZero(value):
	value=str(value)
	if len(value)>0:
		return 1
	return 0