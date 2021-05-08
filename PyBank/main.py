#Import dependencies
from pandas import read_csv

#Load in csv from resources into a dataframe
csv_path='Resources/budget_data.csv'
budgetDF=read_csv(csv_path)

#Find number of entries in the date column
#Use count() to return number of rows in the Date column
monthcount=(budgetDF['Date']).count()

#Find net profit for the entire dataset
#Use sum() to return the sum of all the data in the Profit/Losses column
#Format the sum to show as dollars 
netprofit=(budgetDF['Profit/Losses']).sum()
netprofitformatted="$ {:.2f}".format(netprofit)

#Find the average change in profit from month-to-month
#Use diff() to calulate the difference between a row and the previous row
#Add Delta as a column to the dataframe and calculate the mean
monthdelta=(budgetDF['Profit/Losses']).diff()
budgetDF['Delta']=monthdelta
avgdelta=budgetDF.Delta.mean()
avgdeltaformatted="$ {:.2f}".format(avgdelta)

#Find the maximum month-to-month profit increase
#Use argmax() to return the index of the maximum delta
#Use the iloc[index] to locate the corresponding values in the dataframe for max profit increase
index=budgetDF.Delta.argmax()
maxprofitdelta=budgetDF['Delta'].iloc[index]
maxprofitdeltaformatted="$ {:.2f}".format(maxprofitdelta)
maxprofitdate=budgetDF['Date'].iloc[index]

#Find thw lowest month-to-month profit increase
#Use argmin() to return the index of the minimum delta
mindex=budgetDF.Delta.argmin()
minprofitdelta=budgetDF['Delta'].iloc[mindex]
minprofitdeltaformatted="$ {:.2f}".format(minprofitdelta)
minprofitdate=budgetDF['Date'].iloc[mindex]

#Write results to a txt file report
results= open("analysis_result.txt","w+")
results.write('Financial Analysis\n----------------------\n')
results.write(f'Total Months: {monthcount}\nTotal Profit: {netprofitformatted}\nAverage Monthly Change: {avgdeltaformatted}\n')
results.write(f'The greatest increase in profits was {maxprofitdate}, with an increase of {maxprofitdeltaformatted}.\n')
results.write(f'The greatest decrease in profits was {minprofitdate}, with a decrease of {minprofitdeltaformatted}.')
results.close()

