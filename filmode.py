#fill the missing and N/A value with mode
def filmode (datafr) :
    
    for col in datafr.columns :
        datafr[col] = datafr[col].fillna(datafr[col].mode()[0])
    return datafr

