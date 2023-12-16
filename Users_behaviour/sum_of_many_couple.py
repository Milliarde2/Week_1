#The total data volume (in bytes) during this session for each application

from util import utils_1
from sum_of_two_data import sumofdata
#List of applications

# Applist should be kind of list of couple, for example, Applist = Applications =[['Social Media DL (Bytes)','Social Media UL (Bytes)'],['Youtube DL (Bytes)','Youtube UL (Bytes)'],['Netflix DL (Bytes)','Netflix UL (Bytes)'],['Google DL (Bytes)','Google UL (Bytes)'],['Email UL (Bytes)','Email DL (Bytes)'],['Gaming UL (Bytes)','Gaming DL (Bytes)'],['Total UL (Bytes)','Total DL (Bytes)']]

def tot_per_app (datafr,usersIDcol, Applist):
    
    #create a dataframe where we can save all result
    dt_appli = pd.DataFrame()
    userlist = datafr[usersIDcol].unique()
    dt_appli[usersIDcol]= userlist
    for appli in Applist :
        tot_vol_ap = sumofdata(datafr,usersIDcol, appli[0], appli[1])
        #create a combined dataframe
        dt_appli = pd.merge(dt_appli, tot_vol_ap)
    return dt_appli
