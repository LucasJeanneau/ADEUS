
import pandas as pd
 
df = pd.read_csv (r'C:\Users\jeanneau\Desktop\\test.csv')

columns_to_keep = [x for x in range(df.shape[1]) if x in [0,1,18,35]]
vitesse_moyenne_24h_s_hvs = df.iloc[:, columns_to_keep]

vitesse_moyenne_24h_s_hvs.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\moyenne24shvs.csv", index=False)

columns_to_keep = [x for x in range(df.shape[1]) if x in [0,2,19,36]]
vitesse_mediane_24h_s_hvs = df.iloc[:, columns_to_keep]

vitesse_mediane_24h_s_hvs.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\mediane24shvs.csv", index=False)

columns_to_keep = [x for x in range(df.shape[1]) if x in [0,3,20,37]]
vitesse_mediane_hc_s_hvs = df.iloc[:, columns_to_keep]

vitesse_mediane_hc_s_hvs.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\medianehcshvs.csv", index=False)

columns_to_keep = [x for x in range(df.shape[1]) if x in [0,4,21,38]]
vitesse_mediane_hps_s_hvs = df.iloc[:, columns_to_keep]

vitesse_mediane_hps_s_hvs.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\medianehpsshvs.csv", index=False)


columns_to_keep = [x for x in range(df.shape[1]) if x in [0,5,22,39]]
vitesse_moyenne_24h_mj_hvs = df.iloc[:, columns_to_keep]

vitesse_moyenne_24h_mj_hvs.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\moyenne24mjhvs.csv", index=False)


columns_to_keep = [x for x in range(df.shape[1]) if x in [0,6,23,40]]
vitesse_mediane_24h_mj_hvs = df.iloc[:, columns_to_keep]

vitesse_mediane_24h_mj_hvs.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\mediane24mjhvs.csv", index=False)


columns_to_keep = [x for x in range(df.shape[1]) if x in [0,7,24,41]]
vitesse_moyenne_hc_mj_hvs = df.iloc[:, columns_to_keep]

vitesse_moyenne_hc_mj_hvs.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\moyennehcmjhvs.csv", index=False)

columns_to_keep = [x for x in range(df.shape[1]) if x in [0,8,25,42]]
vitesse_mediane_hc_mj_hvs = df.iloc[:, columns_to_keep]

vitesse_mediane_hc_mj_hvs.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\medianehcmjhvs.csv", index=False)


columns_to_keep = [x for x in range(df.shape[1]) if x in [0,9,26,43]]
vitesse_moyenne_hpm_mj_hvs = df.iloc[:, columns_to_keep]

vitesse_moyenne_hpm_mj_hvs.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\moyennehpmjhvs.csv", index=False)


columns_to_keep = [x for x in range(df.shape[1]) if x in [0,10,27,44]]
vitesse_mediane_hpm_mj_hvs = df.iloc[:, columns_to_keep]

vitesse_mediane_hpm_mj_hvs.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\medianehpmmjhvs.csv", index=False)

columns_to_keep = [x for x in range(df.shape[1]) if x in [0,11,28,45]]
vitesse_moyenne_hps_mj_hvs = df.iloc[:, columns_to_keep]

vitesse_moyenne_hps_mj_hvs.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\moyennehpsmjhvs.csv", index=False)


columns_to_keep = [x for x in range(df.shape[1]) if x in [0,12,29,46]]
vitesse_mediane_hps_mj_hvs = df.iloc[:, columns_to_keep]

vitesse_mediane_hps_mj_hvs.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\medianehpsmjhvs.csv", index=False)


columns_to_keep = [x for x in range(df.shape[1]) if x in [0,13,30,47]]
vitesse_moyenne_24h_vs = df.iloc[:, columns_to_keep]

vitesse_moyenne_24h_vs.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\moyenne24vs.csv", index=False)


columns_to_keep = [x for x in range(df.shape[1]) if x in [0,14,31,48]]
vitesse_mediane_24h_vs = df.iloc[:, columns_to_keep]

vitesse_mediane_24h_vs.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\mediane24vs.csv", index=False)


columns_to_keep = [x for x in range(df.shape[1]) if x in [0,15,32,49]]
nb_heures_congestion_vs_24h = df.iloc[:, columns_to_keep]

nb_heures_congestion_vs_24h.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\heure24vs.csv", index=False)

columns_to_keep = [x for x in range(df.shape[1]) if x in [0,16,33,50]]
nb_heures_congestion_s_24h = df.iloc[:, columns_to_keep]

nb_heures_congestion_s_24h.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\heure24s.csv", index=False)

columns_to_keep = [x for x in range(df.shape[1]) if x in [0,17,34,51]]
nb_heures_congestion_mj_24h = df.iloc[:, columns_to_keep]

nb_heures_congestion_mj_24h.to_csv("C:\\Users\\jeanneau\\Desktop\\x\\Data\\heure24mj.csv", index=False)

        
