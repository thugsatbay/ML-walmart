import numpy as np
import pandas as pd
from functions import printFeaturesInfo
from functions import printAllColumnNames
from functions import oneZero

#Load CSV File
trainD=pd.read_csv("train.tsv",sep="\t",header=0)


#Seperating Y variable per output
sepTags=trainD['tag'].apply(func=(lambda eachRow: str(eachRow).replace("[","").replace("]","").replace(" ",""))).str.split(",").apply(pd.Series,1).stack()
#testing.index=testing.index.droplevel(-1)
sepTags.reset_index(level=1,drop=True,inplace=True)
sepTags=sepTags.apply(func=(lambda val:str(val)))
sepTags.name="tagNew"
del trainD['tag']
trainD=trainD.join(sepTags)
#Reset Index
trainD = trainD.reset_index(drop=True)


#List Of Features
printAllColumnNames(trainD)
#printFeaturesInfo(trainD,['Actors'])
'''
for x in trainD.columns.values:
	if x not in ['Actors','item_id','Product Long Description', 'Product Name', 'Product Short Description','Short Description', 'Synopsis']:
		printFeaturesInfo(trainD,[x])
'''



'''
print trainD[trainD['MPAA Rating'].notnull()]['tag'].value_counts()
print trainD[trainD['Aspect Ratio'].notnull()]['Recommended Use'].value_counts()
print trainD[trainD['Aspect Ratio'].notnull()]['tag'].value_counts()
sellerColNames=list(trainD['Seller'].value_counts().index)
#print list(trainD['Seller'].value_counts().axes)
'''

#Seperate y Output
yD=trainD['tagNew']
del trainD['tagNew']


#split Seller Binay Feature Seperation
trainD=pd.get_dummies(trainD,prefix=['Seller'],columns=['Seller'],dummy_na=True)



#Updating Actor Feature
'''
#Actors Data 1 Or 0
trainD.loc[trainD['Actors'].notnull(),'Actors']=1
trainD.loc[trainD['Actors'].isnull(),'Actors']=0
'''
#Actors By How Many
allActors=trainD['Actors'].apply(func=lambda eachRow: len(list(str(eachRow).replace(", ",",").split(","))) if str(eachRow)!="nan" else 0)
allActors.name="NumActors"
del trainD['Actors']
trainD=trainD.join(allActors,how="inner")
'''
#Actors By Name
allActors=trainD['Actors'].str.replace(", ",",").str.split(",").apply(pd.Series,1).stack()
allActors.reset_index(level=1,drop=True,inplace=True)
allActors.reset_index(drop=True,inplace=True)
#925 Actors where they appear 1432 times
'''