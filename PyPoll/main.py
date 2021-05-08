import pandas as pd
csv_path='Resources/election_data.csv'
elecdata_DF=pd.read_csv(csv_path)

#print(elecdata_DF.head())

#print(len(elecdata_DF["Voter ID"]))

totalvotes=elecdata_DF["Voter ID"].count()
#print(totalvotes)

votedcandidates_DF=elecdata_DF["Candidate"].value_counts()

percentvotes=votedcandidates_DF/totalvotes

new=pd.DataFrame({'email':votedcandidates_DF.index, 'list':votedcandidates_DF.values})
new2=pd.DataFrame({'email':percentvotes.index, 'list':percentvotes.values})

print(elecdata_DF)
#print(votedcandidates_DF)

#newlist=[]

#for x in votedcandidates_DF:
    #newlist.append(x)
    