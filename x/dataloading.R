library(readr)
library(dplyr)

all<- read.csv("Data/data.csv")

moyenne24shvs <- all %>% select(trajet,Vmoy_SA_2017, Vmoy_SA_2018, Vmoy_SA_2019)
moyenne24mjhvs <- all %>% select(trajet, Vmoy_MJ_2017,Vmoy_MJ_2018,Vmoy_MJ_2019) 
moyenne24vs <- all %>% select(trajet, Vmoy_VS_2017, Vmoy_VS_2018,Vmoy_VS_2019)
moyennehpmmjhvs <- all %>% select(trajet,Vmoy_MJ_HPM_2017,Vmoy_MJ_HPM_2018,Vmoy_MJ_HPM_2019)
moyennehcmjhvs <- all %>% select(trajet, Vmoy_MJ_HC_2017,Vmoy_MJ_HC_2018,Vmoy_MJ_HC_2019)
moyennehpsmjhvs <- all %>% select(trajet, Vmoy_MJ_HPS_2017,Vmoy_MJ_HPS_2018,Vmoy_MJ_HPS_2019)

heure24mj_niv1<-  all %>% select(trajet,congestion_niv1_MJ_2017,congestion_niv1_MJ_2018,congestion_niv1_MJ_2019)
heure24mj_niv2<-  all %>% select(trajet,congestion_niv2_MJ_2017,congestion_niv2_MJ_2018,congestion_niv2_MJ_2019)
heure24mj_niv3<-  all %>% select(trajet,congestion_niv3_MJ_2017,congestion_niv3_MJ_2018,congestion_niv3_MJ_2019)

heure24vs_niv1<-  all %>% select(trajet,congestion_niv1_VS_2017,congestion_niv1_VS_2018,congestion_niv1_VS_2019)
heure24vs_niv2<-  all %>% select(trajet,congestion_niv2_VS_2017,congestion_niv2_VS_2018,congestion_niv2_VS_2019)
heure24vs_niv3<-  all %>% select(trajet,congestion_niv3_VS_2017,congestion_niv3_VS_2018,congestion_niv3_VS_2019)
                                 
heure24s_niv1<-  all %>% select(trajet,congestion_niv1_SA_2017,congestion_niv1_SA_2018,congestion_niv1_SA_2019)
heure24s_niv2<-  all %>% select(trajet,congestion_niv2_SA_2017,congestion_niv2_SA_2018,congestion_niv2_SA_2019)
heure24s_niv3<-  all %>% select(trajet,congestion_niv3_SA_2017,congestion_niv3_SA_2018,congestion_niv3_SA_2019)

jour_niv3_15min <- all %>% select(trajet,jours_congestion_niv3_15_min_MJ_2017,jours_congestion_niv3_15_min_MJ_2018,jours_congestion_niv3_15_min_MJ_2019)
jour_niv3_30min <- all %>% select(trajet,jours_congestion_niv3_30_min_MJ_2017,jours_congestion_niv3_30_min_MJ_2018,jours_congestion_niv3_30_min_MJ_2019)
jour_niv3_60min <- all %>% select(trajet,jours_congestion_niv3_60_min_MJ_2017,jours_congestion_niv3_60_min_MJ_2018,jours_congestion_niv3_60_min_MJ_2019)


mediane24mjhvs<-all %>% select(trajet,Vmed_MJ_2017,Vmed_MJ_2018,Vmed_MJ_2019)                                                                                               
mediane24shvs<-all %>% select(trajet,Vmed_SA_2017,Vmed_SA_2018,Vmed_SA_2019)
mediane24vs<-all %>% select(trajet,Vmed_VS_2017,Vmed_VS_2018,Vmed_VS_2019)
medianehcmjhvs<-all %>% select(trajet,Vmed_MJ_HC_2017,Vmed_MJ_HC_2018,Vmed_MJ_HC_2019)
medianehcshvs<-all %>% select(trajet,Vmed_SA_HC_2017,Vmed_SA_HC_2018,Vmed_SA_HC_2019)
medianehpmmjhvs<-all %>% select(trajet,Vmed_MJ_HPM_2017,Vmed_MJ_HPM_2018,Vmed_MJ_HPM_2019)
medianehpsmjhvs<-all %>% select(trajet,Vmed_MJ_HPS_2017,Vmed_MJ_HPS_2018,Vmed_MJ_HPS_2019)
medianehpsshvs<-all %>% select(trajet,Vmed_SA_HPS_2017,Vmed_SA_HPS_2018,Vmed_SA_HPS_2019)

dflist <- list(heure24mj_niv1,heure24mj_niv2,heure24mj_niv3,heure24s_niv1,heure24s_niv2,heure24s_niv3,heure24vs_niv1,heure24vs_niv2,heure24vs_niv3,jour_niv3_15min,mediane24mjhvs,mediane24shvs,mediane24vs,medianehcmjhvs,medianehcshvs,medianehpmmjhvs,medianehpsmjhvs,medianehpsshvs,moyenne24mjhvs,moyenne24shvs,moyenne24vs,moyennehcmjhvs,moyennehpmmjhvs,moyennehpsmjhvs,jour_niv3_30min,jour_niv3_60min)
colnames <- c("trajet",2017,2018,2019)

for (i in seq_along(dflist)){
  colnames(dflist[[i]]) <- colnames
  rownames(dflist[i])<-NULL
}

