from util import utils_1

#Top 3 handset manufacturers
def top3(datafr,IDcol,col):  #datafr : is a dataframe ; IDcol : is a string(name of the ID column) ; col : is a string (name of the column)

    #Number and list of manufacturers
    UnManuf = datafr[col].unique() #list
    numb_manu = len(UnManuf)                            # number

    # Number of users ID for each manufacturer
    numb_use_manu=[]
    for manu in UnManuf : 
        numb = len(datafr[datafr[col]==manu].index.tolist())
        numb_use_manu = numb_use_manu +[numb]

    #creating a dataframe for users numbers and manufacturers
    df_manuf = pd.DataFrame()
    df_manuf['Handset Manufacturer'] = UnManuf
    df_manuf['Number of customers'] = numb_use_manu
    #df_manuf.head(5)

    # Get the top 3 number of use of customers
    num_top_use = sorted(df_manuf['Number of customers'], reverse=True)[:3]
    #print (num_top_use)

    #Get the top 3 handset manufacturers using their respective number of customers
    top_manu =[]
    for num in num_top_use : 
        row = df_manuf[df_manuf['Number of customers']== num].index.tolist()
        row = row[0] #assume that no number of customers are same
        top = df_manuf['Handset Manufacturer'][row]
        top_manu=top_manu+[top]
    print("The top 3 manufacturers are :")
    return(top_manu)
