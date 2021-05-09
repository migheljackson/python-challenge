#Add dependencies and read in the csv
import pandas as pd
csv_path='Resources/election_data.csv'
elecdata_DF=pd.read_csv(csv_path)

#Calculate total votes cast by counting VoterID
totalvotes=elecdata_DF["Voter ID"].count()
totalvotesform="{:,}".format(totalvotes)

#Calculate the vote counts for each candidate
votedcandidates_DF=elecdata_DF["Candidate"].value_counts()

#Calculate the percentage of the vote each candidate received
percentvotes=votedcandidates_DF/totalvotes

#Convert and merge votedcandidate Series and percentvotes Series into a single DataFrame
#This will allow us to more easily call individual data values for our outputs  
totvote_df=pd.DataFrame({'Candidate':votedcandidates_DF.index, 'Total Votes':votedcandidates_DF.values})
percvote_df=pd.DataFrame({'Candidate':percentvotes.index, '% of Vote':percentvotes.values})
electresult_df=pd.merge(totvote_df,percvote_df,on='Candidate',how='inner')

#Uses argmax to find the index of the row that contains the highest % of Vote and the associated Candidate
findwindex=electresult_df["% of Vote"].argmax()
winner=electresult_df['Candidate'].iloc[findwindex]

#Calculates the number of candidates in our data set
candidatecount=len(electresult_df['Candidate'])

#Generate Terminal outputs for QA
print('Election Results\n---------------\n')
print(f'Total Votes Cast: {totalvotesform}\n---------------\n')

#For loop generates a formatted output for each candidate
for x in range(0,candidatecount): 
    name=electresult_df['Candidate'].iloc[x]
    votes=electresult_df['Total Votes'].iloc[x]
    votesform="{:,}".format(votes)
    percent=(electresult_df['% of Vote'].iloc[x])*100
    percentform="{:.2f}%".format(percent)
    print((f'{name} received {percentform} of the vote with {votesform} total votes.\n'))
    
print(f'---------------\nWinner: {winner}\n---------------')

#Generate results .txt file
results= open("election_results.txt","w+")
results.write('Election Results\n---------------\n')
results.write(f'Total Votes Cast: {totalvotesform}\n---------------\n')

for x in range(0,candidatecount): 
    name=electresult_df['Candidate'].iloc[x]
    votes=electresult_df['Total Votes'].iloc[x]
    votesform="{:,}".format(votes)
    percent=(electresult_df['% of Vote'].iloc[x])*100
    percentform="{:.2f}%".format(percent)
    results.write((f'{name} received {percentform} of the vote with {votesform} total votes.\n'))
    
results.write(f'---------------\nWinner: {winner}\n---------------')
results.close()