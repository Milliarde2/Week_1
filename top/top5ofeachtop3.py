#Top 5 handsets per top 3 handsets manufacturers

from util import utils_1
from top import top3


#Find the top 5 handsets of one manufacturer

def findtop5 (datafr,manufcol,handsetcol,manuf):  
    
    #get the manufacturer handset list and number
    row =datafr[datafr[manufcol]==manuf].index.tolist() #list of the row where we find the manuf
    handset_list =[]
    for index in row :
        handset = datafr[handsetcol][index]
        handset_list = handset_list + [handset]
        handset_list =handset_list
    df_handset_and_manuf = pd.DataFrame()
    df_handset_and_manuf['Handset'] = handset_list
    handset_list = df_handset_and_manuf['Handset'].unique()  #list
    nb_hs_type = len( handset_list)
    
    # top 5 of the handset 
    # Number of users of each handset
    numb_use_hs=[]
    for hs in handset_list : 
        numb = len(df_handset_and_manuf[df_handset_and_manuf['Handset']==hs].index.tolist())
        numb_use_hs = numb_use_hs +[numb]
        
        #creating a dataframe for users numbers and handset type
    df_hs = pd.DataFrame()
    df_hs['Handset Type'] = handset_list
    df_hs['Number of users'] = numb_use_hs
    
    # Get the top5 number of use
    num_top_hs = sorted(df_hs['Number of users'], reverse=True)[:5]

    #Get the top 5 handset types
    top_hs =[]
    for num in num_top_hs : 
        row = df_hs[df_hs['Number of users']== num].index.tolist()
        row = row[0] #assume that no number of uses are same
        top = df_hs['Handset Type'][row]
        top_hs=top_hs+[top]
    
    #number of handset type
    n=len(handset_list)
    
    print("There are ", n , "handset type of ", manuf , " and the top 5 handset types are : ", top_hs)   
    return(top_hs)

#Get now the top 5 handsets per top 3 handsets manufacturers
def top5ofeach(datafr,IDcol,manufcol,handsetcol) :
    top_manu = top3(datafr,IDcol,manufcol)
    for manuf in top_manu :
        a = findtop5(datafr,manufcol,handsetcol,manuf)
    return(a)
