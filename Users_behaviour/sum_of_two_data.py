from util import utils_1
from total_session import table_user


#the total download (DL) and upload (UL) data
def sumofdata (datafr,usersIDcol, data1, data2):
    #the total download (DL)
    DLT = table_user(datafr,usersIDcol,data1 )

    #the total upload (UL)
    ULT = table_user(datafr,usersIDcol,data2 )

    # sum of download (DL) and upload (UL) data
    ST = DLT[data1] + ULT[data2]

    #Create the new dataframe
    df_DL_UL = pd.DataFrame()
    df_DL_UL[usersIDcol] =DLT[usersIDcol]
    df_DL_UL['Total of '+ data1 +' and '+data2] = ST
    return df_DL_UL 
