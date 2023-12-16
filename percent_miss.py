import numpy as np
#Percentage of missing values

def percent_miss (data):
    
    #total number of cells in df
    T = np.product(data.shape)
    
    #total number of missing values
    M = data.isna().sum().sum()
    
    #percentage of missing values
    P = round((M/T)*100,2)
    
    print ("The dataframe telecom has ", P , "%" , " missing values.")
    return P
