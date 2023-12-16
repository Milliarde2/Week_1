from util import utils_1
#The top 10 handsets used by customers

def top10(datafr,IDcol,col):  #datafr : is a dataframe ; IDcol : is a string(name of the ID column) ; col : is a string (name of the column)
    # Find the unique bearer Ids = list of customers
    UnId = datafr[IDcol].unique()
    
    
    #Find the unique Handset Type = list of Handset type
    UnHandset = datafr[col].unique()
    
    #Number of Id using 'a specific handset', by refering to their position (row index) 
    numb_use=[]
    for handset in UnHandset : 
        numb = len(datafr[datafr[col]==handset].index.tolist())
        numb_use = numb_use +[numb]

    df_handset = pd.DataFrame()
    df_handset['Handset type'] = UnHandset
    df_handset['number of users'] = numb_use 
 
    # Get the 10 maximum number of use
    maxi_use = sorted(df_handset['number of users'], reverse = True)[:11]
   
    #get the corresponding handset type of the top 10 number of use
    tops =[]
    for i in maxi_use : 
        row = df_handset[df_handset['number of users']== i].index.tolist()
        row = row[0]
        top = df_handset['Handset type'][row]
        tops=tops+[top]
    print("The top 10 of handset type are : ")
    return(tops)

    
