# import pandas as pd

# # Charger les fichiers CSV
# youtube_df = pd.read_csv('youtube.csv')
# webpage_df = pd.read_csv('webpage.csv')

# # Fonction pour nettoyer le niveau (retirer le mot "niveau" et convertir en entier)
# def clean_level(level):
#     return int(level.split()[-1])

# # Appliquer la fonction de nettoyage sur les deux DataFrames
# youtube_df['level'] = youtube_df['level'].apply(clean_level)
# webpage_df['level'] = webpage_df['level'].apply(clean_level)

# # Diviser en trois DataFrames en fonction du niveau
# niveau1_df = pd.concat([youtube_df[youtube_df['level'] == 1], webpage_df[webpage_df['level'] == 1]])
# niveau2_df = pd.concat([youtube_df[youtube_df['level'] == 2], webpage_df[webpage_df['level'] == 2]])
# niveau3_df = pd.concat([youtube_df[youtube_df['level'] == 3], webpage_df[webpage_df['level'] == 3]])

# # Enregistrer les nouveaux DataFrames dans des fichiers CSV
# niveau1_df.to_csv('niveau1.csv', index=False)
# niveau2_df.to_csv('niveau2.csv', index=False)
# niveau3_df.to_csv('niveau3.csv', index=False)





##########################################################################################

import pandas as pd

# Charger les fichiers CSV fusionnés
niveau1_df = pd.read_csv('niveau1.csv')
niveau2_df = pd.read_csv('niveau2.csv')
niveau3_df = pd.read_csv('niveau3.csv')

# Supprimer la colonne "level"
niveau1_df.drop(columns=['level'], inplace=True)
niveau2_df.drop(columns=['level'], inplace=True)
niveau3_df.drop(columns=['level'], inplace=True)

# Enregistrer les DataFrames modifiés dans les fichiers CSV existants
niveau1_df.to_csv('niveau1.csv', index=False)
niveau2_df.to_csv('niveau2.csv', index=False)
niveau3_df.to_csv('niveau3.csv', index=False)
