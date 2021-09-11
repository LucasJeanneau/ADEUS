## Importation des modules 

import pymongo
from statistics import mean, median
from openpyxl import load_workbook
import pandas as pd
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME,'')
import matplotlib.pyplot as plt 
import re


## Connexion à la base au Serveur MongoDB et à la base de données ADEUS
 
client= pymongo.MongoClient('localhost', 27017)
mydb= client["ADEUS"]
collections = mydb.list_collection_names()

## Importation des dates de début/fin des vacances scolaires

wb = load_workbook('C:\\Users\jeanneau\Desktop\calendriers\\vacances_scolaires.xlsx')
ws = wb.active
df = pd.DataFrame(ws.values)


liste_debut = []

i=0
while i< len(df):
    timestamp = datetime.timestamp(df.at[i,0])
    liste_debut.append(timestamp)
    i+=1

liste_fin = []

i=0
while i< len(df):
    timestamp = datetime.timestamp(df.at[i,1])
    liste_fin.append(timestamp)
    i+=1
    
## Création de la liste qui va contenir les dictionnaires qui vont contenir tous les indicateurs pour chaque trajet

list_dicts =[]


    
for v in range(len(collections)):
    collection = mydb[collections[v]]
    nb = collection.count()
    
    ## collection années : 
    
    ############################## 2019 ##############################################
    
        ## collection Vacances scolaires VS
            
    list_of_collection = []
    
    for i in range(len(liste_fin)):
        x = collection.find({'$and':
                                    [{"unix": {'$gte': liste_debut[i]}},
                                     {"unix": {'$lte': liste_fin[i]}},{"year":2019}]}
                                    ) 
     
        list_of_collection.append(pd.DataFrame(list(x)))
        
    colls = pd.concat(list_of_collection)
    colls.index = list(range(0,len(colls)))
    
    jour_vacances_2019=[]
    for i in range(len(colls)):
        z= colls.loc[i,'speed']
        jour_vacances_2019.append(z)
    
    
    ## collection samedi hors VS
    
    b= colls.iloc[:,5]
    
    b= b.astype(float)
    
    c= [b[0],b[1]]
    
    x = collection.find({"$and":
                        [{"unix": {"$nin": c}},
                         {"day": {"$eq" :"samedi"}},
                         {"year":2019}]}) 
        
    liste_samedi_HVS = pd.DataFrame(x)
    
    samedi_hors_vacances_2019=[]
    
    for i in range(len(liste_samedi_HVS)):
        z= liste_samedi_HVS.at[i,'speed']
        samedi_hors_vacances_2019.append(z)
    
    
    
    ## collection mardi jeudi hors VS
    
    day=["mardi","jeudi"]
        
    x = collection.find({"$and":
                        [{"unix": {"$nin": c}},
                         {"day": {"$in" : day}},
                         {"year":2019}]}) 
    
    
    liste_mardi_jeudi_HVS = pd.DataFrame(x)
    
    mar_jeu_hors_vacances_2019=[]
    
    for i in range(len(liste_mardi_jeudi_HVS)):
        z= liste_mardi_jeudi_HVS.at[i,'speed']
        mar_jeu_hors_vacances_2019.append(z)
        
        
    if 600<nb:
        
############################## 2018 ##############################################Y  



        ## collection VS 
            
        list_of_collection = []
        
        for i in range(len(liste_fin)):
            x = collection.find({'$and':
                                        [{"unix": {'$gte': liste_debut[i]}},
                                         {"unix": {'$lte': liste_fin[i]}},{"year":2018}]}
                                        ) 
         
            list_of_collection.append(pd.DataFrame(list(x)))
            
        colls = pd.concat(list_of_collection) 
        colls.index = list(range(0,len(colls)))
        
        jour_vacances_2018=[]
        for i in range(len(colls)):
            z= colls.at[i,'speed']
            jour_vacances_2018.append(z)
        
        
        ## collection samedi hors VS
        
        b= colls.iloc[:,5]
        
        b= b.astype(float)
        
        c= [b[0],b[1]]
        
        x = collection.find({"$and":
                            [{"unix": {"$nin": c}},
                             {"day": {"$eq" :"samedi"}},
                             {"year":2018}]}) 
            
        liste_samedi_HVS = pd.DataFrame(x)
        
        samedi_hors_vacances_2018=[]
        
        for i in range(len(liste_samedi_HVS)):
            z= liste_samedi_HVS.at[i,'speed']
            samedi_hors_vacances_2018.append(z)
        
        
        
        ## collection mardi jeudi hors VS
        
        day=["mardi","jeudi"]
            
        x = collection.find({"$and":
                            [{"unix": {"$nin": c}},
                             {"day": {"$in" : day}},
                             {"year":2018}]}) 
        
        
        liste_mardi_jeudi_HVS = pd.DataFrame(x)
        
        mar_jeu_hors_vacances_2018=[]
        
        for i in range(len(liste_mardi_jeudi_HVS)):
            z= liste_mardi_jeudi_HVS.at[i,'speed']
            mar_jeu_hors_vacances_2018.append(z)
            
            
    if nb>900:
        
    ############################## 2017 ##############################################  
    
    
    
        ## collection VS 
            
        list_of_collection = []
        
        for i in range(len(liste_debut)):
            x = collection.find({'$and':
                                        [{"unix": {'$gte': liste_debut[i]}},
                                         {"unix": {'$lte': liste_fin[i]}},
                                         {"year":2017}]}
                                        ) 
            list_of_collection.append(pd.DataFrame(list(x)))
            
        colls = pd.concat(list_of_collection) 
        colls.index = list(range(0,len(colls)))
        
        jour_vacances_2017=[]
        for i in range(len(colls)):
            z= colls.at[i,'speed']
            jour_vacances_2017.append(z)
        
        
        ## collection samedi hors VS
        
        b= colls.iloc[:,5]
        
        b= b.astype(float)
        
        c= [b[0],b[1]]
        
        x = collection.find({"$and":
                            [{"unix": {"$nin": c}},
                             {"day": {"$eq" :"samedi"}},
                             {"year":2017}]}) 
            
        liste_samedi_HVS = pd.DataFrame(x)
        
        samedi_hors_vacances_2017=[]
        
        for i in range(len(liste_samedi_HVS)):
            z= liste_samedi_HVS.at[i,'speed']
            samedi_hors_vacances_2017.append(z)
        
        
        
        ## collection mardi jeudi hors VS
        
        day=["mardi","jeudi"]
            
        x = collection.find({"$and":
                            [{"unix": {"$nin": c}},
                             {"day": {"$in" : day}},
                             {"year":2017}]}) 
        
        
        liste_mardi_jeudi_HVS = pd.DataFrame(x)
        
        mar_jeu_hors_vacances_2017=[]
        
        for i in range(len(liste_mardi_jeudi_HVS)):
            z= liste_mardi_jeudi_HVS.at[i,'speed']
            mar_jeu_hors_vacances_2017.append(z)

 
######### Creation des boxplots ###############

    if nb>900:
        
        ####  2017   #####
                  
          # HPM mardi/jeudi hors VS
           
          hpm = []
          for j in mar_jeu_hors_vacances_2017:
                  hpm.append(j[7:9])
          
          flat=[]
          for i in hpm:
              for j in i:
                 flat.append(j)
          
          median_mar_jeu_hvs_hpm_2017=[]
          
          for item in flat:
              for i in item:
                  median_mar_jeu_hvs_hpm_2017.append(i)
                  
                # HPS mardi/jeudi hors VS
          
          hps = []
          for j in mar_jeu_hors_vacances_2017:
                  hps.append(j[17:19])
          
          flat=[]
          for i in hps:
              for j in i:
                 flat.append(j)
          
          median_mar_jeu_hvs_hps_2017=[]
          
          for item in flat:
              for i in item:
                  median_mar_jeu_hvs_hps_2017.append(i)
                  
                  
          
          # HC mardi/jeudi hors VS
          
          hc = []
          for j in mar_jeu_hors_vacances_2017:
                  hc.append(j[10:13])
          
          flat=[]
          for i in hc:
              for j in i:
                 flat.append(j)
          
          median_mar_jeu_hvs_hc_2017=[]
          
          for item in flat:
              for i in item:
                  median_mar_jeu_hvs_hc_2017.append(i)
                  
          
        
          
          plt.boxplot([median_mar_jeu_hvs_hpm_2017, median_mar_jeu_hvs_hc_2017,median_mar_jeu_hvs_hps_2017])
          a = str(collection[v])
          o= re.findall(r", '(.*?')",a)
          o[1]
          plt.title("2017"+o[1])
          plt.xticks([1,2,3], ['HPM','HC','HPS'])
          plt.show()
          plt.close()
          
            
       ########## 2018#####
                
    if nb>600:
         
        # HPM mardi/jeudi hors VS
        
        
        hpm = []
        for j in mar_jeu_hors_vacances_2018:
                hpm.append(j[7:9])
        
        flat=[]
        for i in hpm:
            for j in i:
               flat.append(j)
        
        median_mar_jeu_hvs_hpm_2018=[]
        
        for item in flat:
            for i in item:
                median_mar_jeu_hvs_hpm_2018.append(i)
                
        
        
        # HPS mardi/jeudi hors VS
        
        hps = []
        for j in mar_jeu_hors_vacances_2018:
                hps.append(j[17:19])
        
        flat=[]
        for i in hps:
            for j in i:
               flat.append(j)
        
        median_mar_jeu_hvs_hps_2018=[]
        
        for item in flat:
            for i in item:
                median_mar_jeu_hvs_hps_2018.append(i)
                
        
        
        # HC mardi/jeudi hors VS
        
        hc = []
        for j in mar_jeu_hors_vacances_2018:
                hc.append(j[10:13])
        
        flat=[]
        for i in hc:
            for j in i:
               flat.append(j)
        
        median_mar_jeu_hvs_hc_2018=[]
        
        for item in flat:
            for i in item:
                median_mar_jeu_hvs_hc_2018.append(i)
                
        
        plt.boxplot([median_mar_jeu_hvs_hpm_2018, median_mar_jeu_hvs_hc_2018, median_mar_jeu_hvs_hps_2018])
        a = str(collection[v])
        o= re.findall(r", '(.*?')",a)
        o[1]
        plt.title("2018"+o[1])
        plt.xticks([1,2,3], ['HPM','HC','HPS'])
        plt.show()
        plt.close()
                
        
                
    ######## 2019 ##########

    
    # HPM mardi/jeudi hors VS
    
    
    hpm = []
    for j in mar_jeu_hors_vacances_2019:
            hpm.append(j[7:9])
    
    flat=[]
    for i in hpm:
        for j in i:
           flat.append(j)
    
    median_mar_jeu_hvs_hpm_2019=[]
    
    for item in flat:
        for i in item:
            median_mar_jeu_hvs_hpm_2019.append(i)
            
    median(median_mar_jeu_hvs_hpm_2019)
    
    
    # HPS mardi/jeudi hors VS
    
    hps = []
    for j in mar_jeu_hors_vacances_2019:
            hps.append(j[17:19])
    
    flat=[]
    for i in hps:
        for j in i:
           flat.append(j)
    
    median_mar_jeu_hvs_hps_2019=[]
    
    for item in flat:
        for i in item:
            median_mar_jeu_hvs_hps_2019.append(i)
            
    median(median_mar_jeu_hvs_hps_2019)
    
    
    # HC mardi/jeudi hors VS
    
    hc = []
    for j in mar_jeu_hors_vacances_2019:
            hc.append(j[10:13])
    
    flat=[]
    for i in hc:
        for j in i:
           flat.append(j)
    
    median_mar_jeu_hvs_hc_2019=[]
    
    for item in flat:
        for i in item:
            median_mar_jeu_hvs_hc_2019.append(i)
            
    median(median_mar_jeu_hvs_hc_2019)
    
    
    plt.boxplot([median_mar_jeu_hvs_hpm_2019, median_mar_jeu_hvs_hc_2019,median_mar_jeu_hvs_hps_2019])
    a = str(collection[v])
    o= re.findall(r", '(.*?')",a)
    o[1]
    plt.title("2019"+o[1])
    plt.xticks([1,2,3], ['HPM','HC','HPS'])
    plt.show()
    plt.close()
    
    