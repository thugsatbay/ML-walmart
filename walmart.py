import numpy as np
import pandas as pd


#Load CSV File
trainD=pd.read_csv("train.tsv",sep="\t",header=0)


#Seperating Y variable per output
sepTags=trainD['tag'].apply(func=(lambda eachRow: str(eachRow).replace("[","").replace("]","").replace(" ",""))).str.split(",").apply(pd.Series,1).stack()
#testing.index=testing.index.droplevel(-1)
sepTags.reset_index(level=1,drop=True,inplace=True)
sepTags=sepTags.apply(func=(lambda val:[val]))
sepTags.name="tagNew"
del trainD['tag']
trainD=trainD.join(sepTags)



#Making Meaningful Features
#trainD.join(testing)
#trainD.join()

#print list(trainD.columns.values)

#List Of Seller Names
'''
for x in trainD.columns.values:
	if x not in ['item_id','Product Long Description', 'Product Name', 'Product Short Description','Short Description', 'Synopsis']:
		print x
		print list(trainD[x].value_counts().index)
		print list(trainD[x].value_counts())
		print sum(list(trainD[x].value_counts()))
		print len(list(trainD[x].value_counts().index))
		print "\n\n"
		
#give the count of all sellers how many times they repeat


print trainD[trainD['MPAA Rating'].notnull()]['tag'].value_counts()
print trainD[trainD['Aspect Ratio'].notnull()]['Recommended Use'].value_counts()
print trainD[trainD['Aspect Ratio'].notnull()]['tag'].value_counts()
sellerColNames=list(trainD['Seller'].value_counts().index)
#print list(trainD['Seller'].value_counts().axes)


#split into features
df=pd.get_dummies(trainD,prefix=['Seller','Actual_Color','Recommended_Use'],columns=['Seller','actual_color','Recommended Use'])
#print len(list(df[df['Seller__Walmart.com']==1]['Color']))

'''