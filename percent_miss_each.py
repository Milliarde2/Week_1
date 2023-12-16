#Percentage of missing value for each element
def percent_miss_each (datafr):
    a = (datafr.isna().sum() / len(df) )*100
    return a
