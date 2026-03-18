#Source: Statistics Netherlands, statline.cbs.nl 
#House prices, quarterly percentage changes
#For new and existing dwellings 
#in period: 2017 1st quarter - 2018 2nd quarter (6 quarters)
import numpy as np

newHomes = np.array([6.1, 6.3, 6.2, 10.2, 11.5, 12.6])
existingHomes = np.array([6.8, 7.7, 7.6, 8.2, 9.0, 8.8])


#In which quarters was the percent of change for existing dwellings higher than
#the percent of change for new dwellings? Display only the percentages which
#apply to this rule.

n = 0
higher = []
for percent in existingHomes:
    if percent > newHomes[n]:
       higher.append(percent)
    
    n += 1
    

print(np.array(higher))

#what is the mean percent of change for new dwellings in 2017

mean = np.sum(newHomes[0:4]) / 4
print(mean)

#for the existing dwellings change the percentages with a value between
# 7 and 8 to 7.5

n = 0
for percent in existingHomes:
    if percent > 7 and percent < 8:
       existingHomes[n] = 7.5
    
    n += 1

print(existingHomes)