import pandas as pd
csv_path='Resources/election_data.csv'
elecdata_DF=pd.read_csv(csv_path)

#print(elecdata_DF.head())

#print(len(elecdata_DF["Voter ID"]))

totalvotes=elecdata_DF["Voter ID"].count()
#print(totalvotes)

votedcandidates_DF=elecdata_DF["Candidate"].value_counts()

percentvotes=votedcandidates_DF/totalvotes

new=pd.DataFrame({'Candidate':votedcandidates_DF.index, 'Total Votes':votedcandidates_DF.values})
new2=pd.DataFrame({'Candidate':percentvotes.index, '% of Vote':percentvotes.values})
merge_df=pd.merge(new,new2,on='Candidate',how='inner')



#print(elecdata_DF)
#print(votedcandidates_DF)

#newlist=[]
index2=len(merge_df['Candidate'])


for x in range(0,index2): 
    name=merge_df['Candidate'].iloc[x]
    votes=merge_df['Total Votes'].iloc[x]
    votesformatted="{:,}".format(votes)
    percent=(merge_df['% of Vote'].iloc[x])*100
    percentformatted="{:.2f}%".format(percent)
    print((f'{name} received {percentformatted} of the vote with {votesformatted} total votes.'))
    
findwindex=merge_df["% of Vote"].argmax()
winner=merge_df['Candidate'].iloc[findwindex]
print(winner)