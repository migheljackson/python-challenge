from pandas import read_csv
csv_path='Resources/budget_data.csv'
budgetDF=read_csv(csv_path)

#print(budgetDF.columns)
#print(budgetDF.count)
monthcount=(budgetDF['Date']).count()
#print(monthcount)


netprofit=(budgetDF['Profit/Losses']).sum()
netprofitformatted="$ {:.2f}".format(netprofit)

#print("${:.2f}".format((budgetDF['Profit/Losses']).sum()))

monthdelta=(budgetDF['Profit/Losses']).diff()
budgetDF['Delta']=monthdelta
avgdelta=budgetDF.Delta.mean()
avgdeltaformatted="$ {:.2f}".format(avgdelta)

#print("${:.2f}".format(monthdelta.mean()))

#print(monthdelta.max())

index=budgetDF.Delta.argmax()
maxprofitdelta=budgetDF['Delta'].iloc[index]
maxprofitdeltaformatted="$ {:.2f}".format(maxprofitdelta)
maxprofitdate=budgetDF['Date'].iloc[index]
#print(maxprofitdeltaformatted)
#print(maxprofitdate)

mindex=budgetDF.Delta.argmin()
minprofitdelta=budgetDF['Delta'].iloc[mindex]
minprofitdeltaformatted="$ {:.2f}".format(minprofitdelta)
minprofitdate=budgetDF['Date'].iloc[mindex]


#print(budgetDF['Date'].iloc[index])

#maxprofit=budgetDF[budgetDF.Delta == budgetDF.Delta.max()]


#minprofit=budgetDF[budgetDF.Delta == budgetDF.Delta.min()]
#print(minprofit)
results= open("analysis_result.txt","w+")
results.write('Financial Analysis\n----------------------\n')
results.write(f'Total Months: {monthcount}\nTotal Profit: {netprofitformatted}\nAverage Monthly Change: {avgdeltaformatted}\n')
results.write(f'The greatest increase in profits was {maxprofitdate}, with an increase of {maxprofitdeltaformatted}.\n')
results.write(f'The greatest decrease in profits was {minprofitdate}, with a decrease of {minprofitdeltaformatted}.')
results.close()

