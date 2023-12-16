from util import utils_1

#Function for total session duration per user 
def table_user (datafr,usersIDcol, data) : 
    #get the list of users
    userlist = datafr[usersIDcol].unique()
    #get the total data of each user
    data1 = []
    for ID in userlist :
        row = datafr[datafr[usersIDcol]==ID].index.tolist()
        tot = 0
        for i in row : 
            row_n= i
            value_n = datafr[data][row_n]
            tot=tot+value_n
        data1 = data1 + [tot]
        
    #Create a dataframe
    df_behave = pd.DataFrame()
    df_behave[usersIDcol] = userlist
    df_behave[data] = data1
    return df_behave  
