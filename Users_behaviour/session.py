
from util import utils_1
#number of xDR sessions
def session_num(datafr,usersIDcol, data) :
    
    #get the list of users
    userlist = datafr[usersIDcol].unique()
    
    #get the number of session of each user
    Ss_num_ls = []
    for ID in userlist :
        row = datafr[datafr[usersIDcol]==ID].index.tolist()
        numb=len(row)
        Ss_num_ls = Ss_num_ls + [numb]
    
    #Create a dataframe
    df_Ss_num = pd.DataFrame()
    df_Ss_num[usersIDcol] = userlist
    df_Ss_num[data] = Ss_num_ls
    return df_Ss_num   
