## Importation des modules 

import pymongo
from statistics import mean, median
from openpyxl import load_workbook
import pandas as pd
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME,'')
import itertools
import numpy as np


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
  
    
####indicateurs#####


    if nb>900:
            
    ########## 2017 #####################################################
    
    ## Vitesse moyenne 
        
        
        ## vacances 24h
        
        moyenne_vacances_2017=[]
        
        for i in range(len(jour_vacances_2017)):
            for j in range(len(jour_vacances_2017[i])):
                moyenne_vacances_2017.append(mean(jour_vacances_2017[i][j]))
        
        
        ## samedi 24h
        
        moyenne_samedi_24_2017=[]
        
        for i in range(len(samedi_hors_vacances_2017)):
            for j in range(len(samedi_hors_vacances_2017[i])):
                moyenne_samedi_24_2017.append(mean(samedi_hors_vacances_2017[i][j]))
        
        
        ## m/j hors VS sur 24h
        
        mardi_jeudi_24_2017=[]
        
        for i in range(len(mar_jeu_hors_vacances_2017)):
            for j in range(len(mar_jeu_hors_vacances_2017[i])):
                mardi_jeudi_24_2017.append(mean(mar_jeu_hors_vacances_2017[i][j]))
        
        
        ## HPM m/j hors VS 
        
        moyenne_hpm_mj_2017 = []
        
        for i in range(len(mar_jeu_hors_vacances_2017)):
            moyenne_hpm_mj_2017.append((mean(mar_jeu_hors_vacances_2017[i][7]) + mean(mar_jeu_hors_vacances_2017[i][8]))/2)
            
        
        ## HPS m/j hors VS 
        
        
        moyenne_hps_mj_2017 = []
        
        for i in range(len(mar_jeu_hors_vacances_2017)):
            moyenne_hps_mj_2017.append((mean(mar_jeu_hors_vacances_2017[i][17]) + mean(mar_jeu_hors_vacances_2017[i][18]))/2)
            
        
        ## HC m/j hors VS 
        
        moyenne_hc_mj_2017 = []
        
        for i in range(len(mar_jeu_hors_vacances_2017)):
            moyenne_hc_mj_2017.append((mean(mar_jeu_hors_vacances_2017[i][10]) + mean(mar_jeu_hors_vacances_2017[i][11]))/2)
            
        
        
        ## Vitesse médiane
        
        # mardi/jeudi hors VS sur 24h
        
        
        flat_list = []
        for sublist in mar_jeu_hors_vacances_2017:
            for item in sublist:
                flat_list.append(item)
        
        median_mar_jeu_hvs_2017=[]
        
        for sublist in flat_list:
            for item in sublist:
                median_mar_jeu_hvs_2017.append(item)
                
        
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
                        
        
        # samedi hors VS 24h
        
        
        flat_list = []
        for sublist in samedi_hors_vacances_2017:
            for item in sublist:
                flat_list.append(item)
        
        median_samedi_hvs_2017=[]
        
        for sublist in flat_list:
            for item in sublist:
                median_samedi_hvs_2017.append(item)
                
        
        # samedi HC HVS
        
        hc = []
        for j in samedi_hors_vacances_2017:
                hc.append(j[10:13])
        
        flat_list = []
        for sublist in hc:
            for item in sublist:
                flat_list.append(item)
        
        median_samedi_hvs_hc_2017=[]
        
        for sublist in flat_list:
            for item in sublist:
                median_samedi_hvs_hc_2017.append(item)
                
        
     
        
        # samedi HPS HVS
        
        hps= []
        for j in samedi_hors_vacances_2017:
                hps.append(j[17:19])
        
        flat_list = []
        for sublist in hps:
            for item in sublist:
                flat_list.append(item)
        
        median_samedi_hvs_hps_2017=[]
        
        for sublist in flat_list:
            for item in sublist:
                median_samedi_hvs_hps_2017.append(item)
                
        
        # VS 24H
        
        flat_list = []
        for sublist in jour_vacances_2017:
            for item in sublist:
                flat_list.append(item)
        
        median_vs_2017=[]
        
        for sublist in flat_list:
            for item in sublist:
                median_vs_2017.append(item)
                
        
        ## durée de congestion 
        
        
        ## jours de vacances scolaires sur 24h
        
        nuit = []
        
        for j in mar_jeu_hors_vacances_2017:
            nuit.append(j[0:2])
        
        flat_list = []
        for sublist in nuit:
            for item in sublist:
                flat_list.append(item)
    
        nuit_seuil = []        
        for sublist in flat_list:
            for item in sublist:
                nuit_seuil.append(item)
                
        seuil_1 = mean(nuit_seuil)*0.75
        seuil_2 = mean(nuit_seuil)*0.5
        seuil_3 = mean(nuit_seuil)*0.25
    
        
        U=[]
        for i in range(len(jour_vacances_2017)):
            for j in range(len(jour_vacances_2017[i])):
                U.append(jour_vacances_2017[i][j])
                
        df= pd.DataFrame(U)
        
        congestion_niv1=0
        congestion_niv2=0
        congestion_niv3=0
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
              if 0<i<seuil_1:
                congestion_niv1+=3
                
        nb_heures_congestion_niv1_vacances_24h_2017 = (congestion_niv1/60)/(len(df)/24)
        
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
              if 0<i<seuil_2:
                 congestion_niv2+=3
                
        nb_heures_congestion_niv2_vacances_24h_2017 = (congestion_niv2/60)/(len(df)/24)
        
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
              if 0<i<seuil_3:
                 congestion_niv3+=3
                
        nb_heures_congestion_niv3_vacances_24h_2017 = (congestion_niv3/60)/(len(df)/24)
        
                
        
        ## samedi hors VS 24h
        
        
        U=[]
        for i in range(len(samedi_hors_vacances_2017)):
            for j in range(len(samedi_hors_vacances_2017[i])):
                U.append(samedi_hors_vacances_2017[i][j])
                
        df= pd.DataFrame(U)
        
        congestion_niv1=0
        congestion_niv2=0
        congestion_niv3=0
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
              if 0<i<seuil_1:
                congestion_niv1+=3
                
        nb_heures_congestion_niv1_samedi_24h_2017 = (congestion_niv1/60)/(len(df)/24)
        
             
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
              if 0<i<seuil_2:
                congestion_niv2+=3
                
        nb_heures_congestion_niv2_samedi_24h_2017 = (congestion_niv2/60)/(len(df)/24)
        
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
              if 0<i<seuil_3:
                congestion_niv3+=3
                
        nb_heures_congestion_niv3_samedi_24h_2017 = (congestion_niv3/60)/(len(df)/24)
        
        
        
        ## mardi/jeudi hors vacances scolaires 24h
        
                
        U=[]
        for i in range(len(mar_jeu_hors_vacances_2017 )):
            for j in range(len(mar_jeu_hors_vacances_2017[i])):
                U.append(mar_jeu_hors_vacances_2017[i][j])
                
        df= pd.DataFrame(U)
        
        congestion_niv1=0
        congestion_niv2=0
        congestion_niv3=0
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
               if 0<i<seuil_1:
                congestion_niv1+=3
                
        nb_heures_congestion_niv1_marjeu_24h_2017 = (congestion_niv1/60)/(len(df)/24)
        
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
               if 0<i<seuil_2:
                congestion_niv2+=3
                
        nb_heures_congestion_niv2_marjeu_24h_2017 = (congestion_niv2/60)/(len(df)/24)
        
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
               if 0<i<seuil_3:
                congestion_niv3+=3
                
        nb_heures_congestion_niv3_marjeu_24h_2017 = (congestion_niv3/60)/(len(df)/24)
        
        
        #### nombre de jours congestion niv 3 #########
      
        jour_congestion_2017_15min = []
        
        flat_list = []
        
        for sublist in mar_jeu_hors_vacances_2017:
            flat_list.append(list(itertools.chain.from_iterable(sublist)))
    
      
        for jour in flat_list:
            for elem in jour[3:-3]:
                if  0<elem<seuil_3 and ((elem +jour[jour.index(elem)-2]+ jour[jour.index(elem)-1] +jour[jour.index(elem)+1] +jour[jour.index(elem)+2])/5)<seuil_3:
                    jour_congestion_2017_15min.append(flat_list.index(jour))
                    
        jour_congestion_2017_30min = []
    
      
        for jour in flat_list:
            for elem in jour[10:-10]:
                if  0<elem<seuil_3 and (elem +jour[jour.index(elem)-5]+jour[jour.index(elem)-4]+jour[jour.index(elem)-3] +jour[jour.index(elem)-2]+ jour[jour.index(elem)-1] +jour[jour.index(elem)+1] +jour[jour.index(elem)+2] + jour[jour.index(elem)+3] + jour[jour.index(elem)+4])/10<seuil_3:
                    jour_congestion_2017_30min.append(flat_list.index(jour))
                    
                
        jour_congestion_2017_60min = []
    
      
        for jour in flat_list:
            for elem in jour[20:-20]:
                if  0<elem<seuil_3 and (elem +jour[jour.index(elem)-10] + jour[jour.index(elem)-9] + jour[jour.index(elem)-8] + jour[jour.index(elem)-7]+ jour[jour.index(elem)-6] +jour[jour.index(elem)-5]+jour[jour.index(elem)-4]+jour[jour.index(elem)-3] +jour[jour.index(elem)-2]+ jour[jour.index(elem)-1] +jour[jour.index(elem)+1] +jour[jour.index(elem)+2] + jour[jour.index(elem)+3] + jour[jour.index(elem)+4] + jour[jour.index(elem)+5] +jour[jour.index(elem)+6] + jour[jour.index(elem)+7] + jour[jour.index(elem)+8]+jour[jour.index(elem)+9])/20<seuil_3:
                    jour_congestion_2017_60min.append(flat_list.index(jour))
                    
    if 400<nb:
            
            
        
    ########## 2018 #####################################################
    
    ## Vitesse moyenne 
        
        
        ## vacances 24h
        
        moyenne_vacances_2018=[]
        
        for i in range(len(jour_vacances_2018)):
            for j in range(len(jour_vacances_2018[i])):
                moyenne_vacances_2018.append(mean(jour_vacances_2018[i][j]))
        
        
        ## samedi 24h
        
        moyenne_samedi_24_2018=[]
        
        for i in range(len(samedi_hors_vacances_2018)):
            for j in range(len(samedi_hors_vacances_2018[i])):
                moyenne_samedi_24_2018.append(mean(samedi_hors_vacances_2018[i][j]))
        
        
        ## m/j hors VS sur 24h
        
        mardi_jeudi_24_2018=[]
        
        for i in range(len(mar_jeu_hors_vacances_2018)):
            for j in range(len(mar_jeu_hors_vacances_2018[i])):
                mardi_jeudi_24_2018.append(mean(mar_jeu_hors_vacances_2018[i][j]))
        
        
        
        ## HPM m/j hors VS 
        
        moyenne_hpm_mj_2018 = []
        
        for i in range(len(mar_jeu_hors_vacances_2018)):
            moyenne_hpm_mj_2018.append((mean(mar_jeu_hors_vacances_2018[i][7]) + mean(mar_jeu_hors_vacances_2018[i][8]))/2)
            
        
        ## HPS m/j hors VS 
        
        
        moyenne_hps_mj_2018 = []
        
        for i in range(len(mar_jeu_hors_vacances_2018)):
            moyenne_hps_mj_2018.append((mean(mar_jeu_hors_vacances_2018[i][17]) + mean(mar_jeu_hors_vacances_2018[i][18]))/2)
            
        
        ## HC m/j hors VS 
        
        moyenne_hc_mj_2018 = []
        
        for i in range(len(mar_jeu_hors_vacances_2018)):
            moyenne_hc_mj_2018.append((mean(mar_jeu_hors_vacances_2018[i][10]) + mean(mar_jeu_hors_vacances_2018[i][11]))/2)
            
        
        
        ## Vitesse médiane
        
        # mardi/jeudi hors VS sur 24h
        
        
        flat_list = []
        for sublist in mar_jeu_hors_vacances_2018:
            for item in sublist:
                flat_list.append(item)
        
        median_mar_jeu_hvs_2018=[]
        
        for sublist in flat_list:
            for item in sublist:
                median_mar_jeu_hvs_2018.append(item)
                
        
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
                
        
        
        # samedi hors VS 24h
        
        
        flat_list = []
        for sublist in samedi_hors_vacances_2018:
            for item in sublist:
                flat_list.append(item)
        
        median_samedi_hvs_2018=[]
        
        for sublist in flat_list:
            for item in sublist:
                median_samedi_hvs_2018.append(item)
                
        
        # samedi HC HVS
        
        hc = []
        for j in samedi_hors_vacances_2018:
                hc.append(j[10:13])
        
        flat_list = []
        for sublist in hc:
            for item in sublist:
                flat_list.append(item)
        
        median_samedi_hvs_hc_2018=[]
        
        for sublist in flat_list:
            for item in sublist:
                median_samedi_hvs_hc_2018.append(item)
                
        
        # samedi HPS HVS
        
        hps= []
        for j in samedi_hors_vacances_2018:
                hps.append(j[17:19])
        
        flat_list = []
        for sublist in hps:
            for item in sublist:
                flat_list.append(item)
        
        median_samedi_hvs_hps_2018=[]
        
        for sublist in flat_list:
            for item in sublist:
                median_samedi_hvs_hps_2018.append(item)
                
        
        # VS 24H
        
        flat_list = []
        for sublist in jour_vacances_2018:
            for item in sublist:
                flat_list.append(item)
        
        median_vs_2018=[]
        
        for sublist in flat_list:
            for item in sublist:
                median_vs_2018.append(item)
                
        
        ## durée de congestion 
        
        
        ## jours de vacances scolaires sur 24h
        
        nuit = []
        
        for j in mar_jeu_hors_vacances_2018:
            nuit.append(j[0:2])
        
        flat_list = []
        for sublist in nuit:
            for item in sublist:
                flat_list.append(item)
    
        nuit_seuil = []        
        for sublist in flat_list:
            for item in sublist:
                nuit_seuil.append(item)
        
        seuil_1 = mean(nuit_seuil)*0.75
        seuil_2 = mean(nuit_seuil)*0.5
        seuil_3 = mean(nuit_seuil)*0.25
    
        
        U=[]
        for i in range(len(jour_vacances_2018)):
            for j in range(len(jour_vacances_2018[i])):
                U.append(jour_vacances_2018[i][j])
                
        df= pd.DataFrame(U)
        
        congestion_niv1=0
        congestion_niv2=0
        congestion_niv3=0
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
              if 0<i<seuil_1:
                congestion_niv1+=3
                
        nb_heures_congestion_niv1_vacances_24h_2018 = (congestion_niv1/60)/(len(df)/24)
        
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
              if 0<i<seuil_2:
                 congestion_niv2+=3
                
        nb_heures_congestion_niv2_vacances_24h_2018 = (congestion_niv2/60)/(len(df)/24)
        
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
              if 0<i<seuil_3:
                 congestion_niv3+=3
                
        nb_heures_congestion_niv3_vacances_24h_2018 = (congestion_niv3/60)/(len(df)/24)
        
                
        
        ## samedi hors VS 24h
        
        
        U=[]
        for i in range(len(samedi_hors_vacances_2018)):
            for j in range(len(samedi_hors_vacances_2018[i])):
                U.append(samedi_hors_vacances_2018[i][j])
                
        df= pd.DataFrame(U)
        
        congestion_niv1=0
        congestion_niv2=0
        congestion_niv3=0
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
              if 0<i<seuil_1:
                congestion_niv1+=3
                
        nb_heures_congestion_niv1_samedi_24h_2018 = (congestion_niv1/60)/(len(df)/24)
        
             
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
              if 0<i<seuil_2:
                congestion_niv2+=3
                
        nb_heures_congestion_niv2_samedi_24h_2018 = (congestion_niv2/60)/(len(df)/24)
        
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
              if 0<i<seuil_3:
                congestion_niv3+=3
                
        nb_heures_congestion_niv3_samedi_24h_2018 = (congestion_niv3/60)/(len(df)/24)
        
        
        
        ## mardi/jeudi hors vacances scolaires 24h
        
                
        U=[]
        for i in range(len(mar_jeu_hors_vacances_2018 )):
            for j in range(len(mar_jeu_hors_vacances_2018[i])):
                U.append(mar_jeu_hors_vacances_2018[i][j])
                
        df= pd.DataFrame(U)
        
        congestion_niv1=0
        congestion_niv2=0
        congestion_niv3=0
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
               if 0<i<seuil_1:
                congestion_niv1+=3
                
        nb_heures_congestion_niv1_marjeu_24h_2018 = (congestion_niv1/60)/(len(df)/24)
        
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
               if 0<i<seuil_2:
                congestion_niv2+=3
                
        nb_heures_congestion_niv2_marjeu_24h_2018 = (congestion_niv2/60)/(len(df)/24)
        
        
        for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
               if 0<i<seuil_3:
                congestion_niv3+=3
                
        nb_heures_congestion_niv3_marjeu_24h_2018 = (congestion_niv3/60)/(len(df)/24)
        
        jour_congestion_2018_15min = []
        
        flat_list = []
        
        for sublist in mar_jeu_hors_vacances_2018:
            flat_list.append(list(itertools.chain.from_iterable(sublist)))
    
      
        for jour in flat_list:
            for elem in jour[3:-3]:
                if  0<elem<seuil_3 and ((elem +jour[jour.index(elem)-2]+ jour[jour.index(elem)-1] +jour[jour.index(elem)+1] +jour[jour.index(elem)+2])/5)<seuil_3:
                    jour_congestion_2018_15min.append(flat_list.index(jour))
                    
        jour_congestion_2018_30min = []
    
      
        for jour in flat_list:
            for elem in jour[10:-10]:
                if  0<elem<seuil_3 and (elem +jour[jour.index(elem)-5]+jour[jour.index(elem)-4]+jour[jour.index(elem)-3] +jour[jour.index(elem)-2]+ jour[jour.index(elem)-1] +jour[jour.index(elem)+1] +jour[jour.index(elem)+2] + jour[jour.index(elem)+3] + jour[jour.index(elem)+4])/10<seuil_3:
                    jour_congestion_2018_30min.append(flat_list.index(jour))
                    
                
        jour_congestion_2018_60min = []
    
      
        for jour in flat_list:
            for elem in jour[20:-20]:
                if  0<elem<seuil_3 and (elem +jour[jour.index(elem)-10] + jour[jour.index(elem)-9] + jour[jour.index(elem)-8] + jour[jour.index(elem)-7]+ jour[jour.index(elem)-6] +jour[jour.index(elem)-5]+jour[jour.index(elem)-4]+jour[jour.index(elem)-3] +jour[jour.index(elem)-2]+ jour[jour.index(elem)-1] +jour[jour.index(elem)+1] +jour[jour.index(elem)+2] + jour[jour.index(elem)+3] + jour[jour.index(elem)+4] + jour[jour.index(elem)+5] +jour[jour.index(elem)+6] + jour[jour.index(elem)+7] + jour[jour.index(elem)+8]+jour[jour.index(elem)+9])/20<seuil_3:
                    jour_congestion_2018_60min.append(flat_list.index(jour))
                    
########## 2019 #####################################################

## Vitesse moyenne 
    
    
    ## vacances 24h
    
    moyenne_vacances_2019=[]
    
    for i in range(len(jour_vacances_2019)):
        for j in range(len(jour_vacances_2019[i])):
            moyenne_vacances_2019.append(mean(jour_vacances_2019[i][j]))
    
    
    ## samedi 24h
    
    moyenne_samedi_24_2019=[]
    
    for i in range(len(samedi_hors_vacances_2019)):
        for j in range(len(samedi_hors_vacances_2019[i])):
            moyenne_samedi_24_2019.append(mean(samedi_hors_vacances_2019[i][j]))
    
    
    ## m/j hors VS sur 24h
    
    mardi_jeudi_24_2019=[]
    
    for i in range(len(mar_jeu_hors_vacances_2019)):
        for j in range(len(mar_jeu_hors_vacances_2019[i])):
            mardi_jeudi_24_2019.append(mean(mar_jeu_hors_vacances_2019[i][j]))
    
    
    
    ## HPM m/j hors VS 
    
    moyenne_hpm_mj_2019 = []
    
    for i in range(len(mar_jeu_hors_vacances_2019)):
        moyenne_hpm_mj_2019.append((mean(mar_jeu_hors_vacances_2019[i][7]) + mean(mar_jeu_hors_vacances_2019[i][8]))/2)
        
    
    ## HPS m/j hors VS 
    
    
    moyenne_hps_mj_2019= []
    
    for i in range(len(mar_jeu_hors_vacances_2019)):
        moyenne_hps_mj_2019.append((mean(mar_jeu_hors_vacances_2019[i][17]) + mean(mar_jeu_hors_vacances_2019[i][18]))/2)
        
    
    ## HC m/j hors VS 
    
    moyenne_hc_mj_2019 = []
    
    for i in range(len(mar_jeu_hors_vacances_2019)):
        moyenne_hc_mj_2019.append((mean(mar_jeu_hors_vacances_2019[i][10]) + mean(mar_jeu_hors_vacances_2019[i][11]))/2)
        
    
    
    ## Vitesse médiane
    
    # mardi/jeudi hors VS sur 24h
    
    
    flat_list = []
    for sublist in mar_jeu_hors_vacances_2019:
        for item in sublist:
            flat_list.append(item)
    
    median_mar_jeu_hvs_2019=[]
    
    for sublist in flat_list:
        for item in sublist:
            median_mar_jeu_hvs_2019.append(item)
            
    
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
            
    
    
    # samedi hors VS 24h
    
    
    flat_list = []
    for sublist in samedi_hors_vacances_2019:
        for item in sublist:
            flat_list.append(item)
    
    median_samedi_hvs_2019=[]
    
    for sublist in flat_list:
        for item in sublist:
            median_samedi_hvs_2019.append(item)
            
    
    # samedi HC HVS
    
    hc = []
    for j in samedi_hors_vacances_2019:
            hc.append(j[10:13])
    
    flat_list = []
    for sublist in hc:
        for item in sublist:
            flat_list.append(item)
    
    median_samedi_hvs_hc_2019=[]
    
    for sublist in flat_list:
        for item in sublist:
            median_samedi_hvs_hc_2019.append(item)
            
    
    # samedi HPS HVS
    
    hps= []
    for j in samedi_hors_vacances_2019:
            hps.append(j[17:19])
    
    flat_list = []
    for sublist in hps:
        for item in sublist:
            flat_list.append(item)
    
    median_samedi_hvs_hps_2019=[]
    
    for sublist in flat_list:
        for item in sublist:
            median_samedi_hvs_hps_2019.append(item)
            
    
    # VS 24H
    
    flat_list = []
    for sublist in jour_vacances_2019:
        for item in sublist:
            flat_list.append(item)
    
    median_vs_2019=[]
    
    for sublist in flat_list:
        for item in sublist:
            median_vs_2019.append(item)
            
    
    ##  durée de congestion 
    
    
    ## jours de vacances scolaires sur 24h
    
    nuit = []
    
    for j in mar_jeu_hors_vacances_2019:
        nuit.append(j[0:2])
    
    flat_list = []
    for sublist in nuit:
        for item in sublist:
            flat_list.append(item)

    nuit_seuil = []        
    for sublist in flat_list:
        for item in sublist:
            nuit_seuil.append(item)   
            
    seuil_1 = mean(nuit_seuil)*0.75
    seuil_2 = mean(nuit_seuil)*0.5
    seuil_3 = mean(nuit_seuil)*0.25

            
    U=[]
    for i in range(len(jour_vacances_2019)):
        for j in range(len(jour_vacances_2019[i])):
            U.append(jour_vacances_2019[i][j])
            
    df= pd.DataFrame(U)
    
    congestion_niv1=0
    congestion_niv2=0
    congestion_niv3=0
    
    for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
          if 0<i<seuil_1:
            congestion_niv1+=3
            
    nb_heures_congestion_niv1_vacances_24h_2019 = (congestion_niv1/60)/(len(df)/24)
    
    
    for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
          if 0<i<seuil_2:
             congestion_niv2+=3
            
    nb_heures_congestion_niv2_vacances_24h_2019 = (congestion_niv2/60)/(len(df)/24)
    
    
    for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
          if 0<i<seuil_3:
             congestion_niv3+=3
            
    nb_heures_congestion_niv3_vacances_24h_2019 = (congestion_niv3/60)/(len(df)/24)
    
            
    
    ## samedi hors VS 24h
    
    
    U=[]
    for i in range(len(samedi_hors_vacances_2019)):
        for j in range(len(samedi_hors_vacances_2019[i])):
            U.append(samedi_hors_vacances_2019[i][j])
            
    df= pd.DataFrame(U)
    
    congestion_niv1=0
    congestion_niv2=0
    congestion_niv3=0
    
    for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
          if 0<i<seuil_1:
            congestion_niv1+=3
            
    nb_heures_congestion_niv1_samedi_24h_2019 = (congestion_niv1/60)/(len(df)/24)
    
         
    for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
          if 0<i<seuil_2:
            congestion_niv2+=3
            
    nb_heures_congestion_niv2_samedi_24h_2019 = (congestion_niv2/60)/(len(df)/24)
    
    
    for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
          if 0<i<seuil_3:
            congestion_niv3+=3
            
    nb_heures_congestion_niv3_samedi_24h_2019 = (congestion_niv3/60)/(len(df)/24)
    
    
    
    ## mardi/jeudi hors vacances scolaires 24h
    
            
    U=[]
    for i in range(len(mar_jeu_hors_vacances_2019 )):
        for j in range(len(mar_jeu_hors_vacances_2019[i])):
            U.append(mar_jeu_hors_vacances_2019[i][j])
            
    df= pd.DataFrame(U)
    
    congestion_niv1=0
    congestion_niv2=0
    congestion_niv3=0
    
    for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
           if 0<i<seuil_1:
            congestion_niv1+=3
            
    nb_heures_congestion_niv1_marjeu_24h_2019 = (congestion_niv1/60)/(len(df)/24)
    
    
    for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
           if 0<i<seuil_2:
            congestion_niv2+=3
            
    nb_heures_congestion_niv2_marjeu_24h_2019 = (congestion_niv2/60)/(len(df)/24)
    
    
    for i in [df[j][k] for k in range(0,len(df)) for j in df.columns]:
           if 0<i<seuil_3:
            congestion_niv3+=3
            
    nb_heures_congestion_niv3_marjeu_24h_2019 = (congestion_niv3/60)/(len(df)/24)
    
    jour_congestion_2019_15min = []
        
    flat_list = []
        
    for sublist in mar_jeu_hors_vacances_2019:
            flat_list.append(list(itertools.chain.from_iterable(sublist)))
    
      
    for jour in flat_list:
        for elem in jour[3:-3]:
                if  0<elem<seuil_3 and ((elem +jour[jour.index(elem)-2]+ jour[jour.index(elem)-1] +jour[jour.index(elem)+1] +jour[jour.index(elem)+2])/5)<seuil_3:
                    jour_congestion_2019_15min.append(flat_list.index(jour))
                    
                    
    jour_congestion_2019_30min = []
    
  
    for jour in flat_list:
        for elem in jour[10:-10]:
            if  0<elem<seuil_3 and (elem +jour[jour.index(elem)-5]+jour[jour.index(elem)-4]+jour[jour.index(elem)-3] +jour[jour.index(elem)-2]+ jour[jour.index(elem)-1] +jour[jour.index(elem)+1] +jour[jour.index(elem)+2] + jour[jour.index(elem)+3] + jour[jour.index(elem)+4])/10<seuil_3:
                jour_congestion_2019_30min.append(flat_list.index(jour))
                
            
    jour_congestion_2019_60min = []

  
    for jour in flat_list:
        for elem in jour[20:-20]:
            if  0<elem<seuil_3 and (elem +jour[jour.index(elem)-10] + jour[jour.index(elem)-9] + jour[jour.index(elem)-8] + jour[jour.index(elem)-7]+ jour[jour.index(elem)-6] +jour[jour.index(elem)-5]+jour[jour.index(elem)-4]+jour[jour.index(elem)-3] +jour[jour.index(elem)-2]+ jour[jour.index(elem)-1] +jour[jour.index(elem)+1] +jour[jour.index(elem)+2] + jour[jour.index(elem)+3] + jour[jour.index(elem)+4] + jour[jour.index(elem)+5] +jour[jour.index(elem)+6] + jour[jour.index(elem)+7] + jour[jour.index(elem)+8]+jour[jour.index(elem)+9])/20<seuil_3:
                jour_congestion_2019_60min.append(flat_list.index(jour))                
    
    
    dictionnaire= {"trajet":collections[v],
                   "Vmoy_SA_2019": mean(moyenne_samedi_24_2019) ,
                   "Vmed_SA_2019": median(median_samedi_hvs_2019),
                   
                   "Vmed_SA_HC_2019":  median(median_samedi_hvs_hc_2019),
                   "Vmed_SA_HPS_2019": median(median_samedi_hvs_hps_2019),
                  
                   "Vmoy_MJ_2019" : mean(mardi_jeudi_24_2019),
                   "Vmed_MJ_2019": median(median_mar_jeu_hvs_2019),   
                   
                   "Vmoy_MJ_HC_2019" :mean(moyenne_hc_mj_2019),  
                   "Vmed_MJ_HC_2019": median(median_mar_jeu_hvs_hc_2019),
                   
                   "Vmoy_MJ_HPM_2019":mean(moyenne_hpm_mj_2019),
                   "Vmed_MJ_HPM_2019": median(median_mar_jeu_hvs_hpm_2019),
                   
                   "Vmoy_MJ_HPS_2019": mean(moyenne_hps_mj_2019),
                   "Vmed_MJ_HPS_2019": median(median_mar_jeu_hvs_hps_2019),
                  
                   "Vmoy_VS_2019": mean(moyenne_vacances_2019),
                   "Vmed_VS_2019": median(median_vs_2019),
                  
                   "congestion_niv1_VS_2019": nb_heures_congestion_niv1_vacances_24h_2019,
                   "congestion_niv2_VS_2019": nb_heures_congestion_niv2_vacances_24h_2019,
                   "congestion_niv3_VS_2019": nb_heures_congestion_niv3_vacances_24h_2019,
                   
                   "congestion_niv1_MJ_2019": nb_heures_congestion_niv1_marjeu_24h_2019,
                   "congestion_niv2_MJ_2019": nb_heures_congestion_niv2_marjeu_24h_2019,
                   "congestion_niv3_MJ_2019": nb_heures_congestion_niv3_marjeu_24h_2019,
                   
                   "congestion_niv1_SA_2019": nb_heures_congestion_niv1_samedi_24h_2019,
                   "congestion_niv2_SA_2019": nb_heures_congestion_niv2_samedi_24h_2019,
                   "congestion_niv3_SA_2019": nb_heures_congestion_niv3_samedi_24h_2019,
                   
                   "jours_congestion_niv3_15_min_MJ_2019" : len(np.unique(jour_congestion_2019_15min)),
                   "jours_congestion_niv3_30_min_MJ_2019" : len(np.unique(jour_congestion_2019_30min)),
                   "jours_congestion_niv3_60_min_MJ_2019" : len(np.unique(jour_congestion_2019_60min))}
                   
    if nb>900:
        dictionnaire.update({"Vmoy_SA_2017": mean(moyenne_samedi_24_2017),
                       "Vmed_SA_2017": median(median_samedi_hvs_2017),
                       
                       "Vmed_SA_HC_2017":  median(median_samedi_hvs_hc_2017),
                       "Vmed_SA_HPS_2017": median(median_samedi_hvs_hps_2017),
                      
                       "Vmoy_MJ_2017" : mean(mardi_jeudi_24_2017),
                       "Vmed_MJ_2017": median(median_mar_jeu_hvs_2017),   
                       
                       "Vmoy_MJ_HC_2017" :mean(moyenne_hc_mj_2017),  
                       "Vmed_MJ_HC_2017": median(median_mar_jeu_hvs_hc_2017),
                       
                       "Vmoy_MJ_HPM_2017":mean(moyenne_hpm_mj_2017),
                       "Vmed_MJ_HPM_2017": median(median_mar_jeu_hvs_hpm_2017),
                       
                       "Vmoy_MJ_HPS_2017": mean(moyenne_hps_mj_2017),
                       "Vmed_MJ_HPS_2017": median(median_mar_jeu_hvs_hps_2017),
                      
                       "Vmoy_VS_2017": mean(moyenne_vacances_2017),
                       "Vmed_VS_2017": median(median_vs_2017),
                      
                       "congestion_niv1_VS_2017": nb_heures_congestion_niv1_vacances_24h_2017,
                       "congestion_niv2_VS_2017": nb_heures_congestion_niv2_vacances_24h_2017,
                       "congestion_niv3_VS_2017": nb_heures_congestion_niv3_vacances_24h_2017,
                       
                       "congestion_niv1_MJ_2017": nb_heures_congestion_niv1_marjeu_24h_2017,
                       "congestion_niv2_MJ_2017": nb_heures_congestion_niv2_marjeu_24h_2017,
                       "congestion_niv3_MJ_2017": nb_heures_congestion_niv3_marjeu_24h_2017,
                       
                       "congestion_niv1_SA_2017": nb_heures_congestion_niv1_samedi_24h_2017,
                       "congestion_niv2_SA_2017": nb_heures_congestion_niv2_samedi_24h_2017,
                       "congestion_niv3_SA_2017": nb_heures_congestion_niv3_samedi_24h_2017,
                       
                       "jours_congestion_niv3_15_min_MJ_2017" : len(np.unique(jour_congestion_2017_15min)),
                       "jours_congestion_niv3_30_min_MJ_2017" : len(np.unique(jour_congestion_2017_30min)),
                       "jours_congestion_niv3_60_min_MJ_2017" : len(np.unique(jour_congestion_2017_60min))})
        
    if 600<nb:
        dictionnaire.update({
        

                 
                   "Vmoy_SA_2018": mean(moyenne_samedi_24_2018) ,
                   "Vmed_SA_2018": median(median_samedi_hvs_2018),
                   
                   "Vmed_SA_HC_2018":  median(median_samedi_hvs_hc_2018),
                   "Vmed_SA_HPS_2018": median(median_samedi_hvs_hps_2018),
                  
                   "Vmoy_MJ_2018" : mean(mardi_jeudi_24_2018),
                   "Vmed_MJ_2018": median(median_mar_jeu_hvs_2018),   
                   
                   "Vmoy_MJ_HC_2018" :mean(moyenne_hc_mj_2018),  
                   "Vmed_MJ_HC_2018": median(median_mar_jeu_hvs_hc_2018),
                   
                   "Vmoy_MJ_HPM_2018":mean(moyenne_hpm_mj_2018),
                   "Vmed_MJ_HPM_2018": median(median_mar_jeu_hvs_hpm_2018),
                   
                   "Vmoy_MJ_HPS_2018": mean(moyenne_hps_mj_2018),
                   "Vmed_MJ_HPS_2018": median(median_mar_jeu_hvs_hps_2018),
                  
                   "Vmoy_VS_2018": mean(moyenne_vacances_2018),
                   "Vmed_VS_2018": median(median_vs_2018),
                  
                   "congestion_niv1_VS_2018": nb_heures_congestion_niv1_vacances_24h_2018,
                   "congestion_niv2_VS_2018": nb_heures_congestion_niv2_vacances_24h_2018,
                   "congestion_niv3_VS_2018": nb_heures_congestion_niv3_vacances_24h_2018,
                   
                   "congestion_niv1_MJ_2018": nb_heures_congestion_niv1_marjeu_24h_2018,
                   "congestion_niv2_MJ_2018": nb_heures_congestion_niv2_marjeu_24h_2018,
                   "congestion_niv3_MJ_2018": nb_heures_congestion_niv3_marjeu_24h_2018,
                   
                   "congestion_niv1_SA_2018": nb_heures_congestion_niv1_samedi_24h_2018,
                   "congestion_niv2_SA_2018": nb_heures_congestion_niv2_samedi_24h_2018,
                   "congestion_niv3_SA_2018": nb_heures_congestion_niv3_samedi_24h_2018,
                   
                   "jours_congestion_niv3_15_min_MJ_2018" : len(np.unique(jour_congestion_2018_15min)),
                   "jours_congestion_niv3_30_min_MJ_2018" : len(np.unique(jour_congestion_2018_30min)),
                   "jours_congestion_niv3_60_min_MJ_2018" : len(np.unique(jour_congestion_2018_60min))})

                   
    
    list_dicts.append(dictionnaire)
    
export= pd.DataFrame(list_dicts)
export.to_csv("C:\\Users\jeanneau\Desktop\\test.csv", index=False)

    