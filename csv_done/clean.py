# import pandas as pd
# import ast
# from sklearn.feature_extraction.text import TfidfVectorizer

# # Charger le fichier CSV
# df = pd.read_csv('main.csv')

# # Fonction pour nettoyer les mots-clés
# def nettoyer_mots_cles(keywords):
#     try:
#         mots_cles_liste = ast.literal_eval(keywords)

#         # Extraire uniquement les mots de la liste
#         mots_seuls = [mot[0] for mot in mots_cles_liste]

#         # Utiliser TfidfVectorizer avec IDF pour calculer l'importance des mots
#         vectorizer = TfidfVectorizer()
#         X = vectorizer.fit_transform([' '.join(mots_seuls)])

#         # Récupérer les noms des fonctionnalités (mots)
#         noms_mots = vectorizer.get_feature_names_out()

#         # Trier les mots en fonction de leur importance (IDF)
#         mots_importants = sorted(zip(noms_mots, X[0].toarray()[0]), key=lambda x: x[1], reverse=True)

#         # Sélectionner les 30 premiers mots-clés
#         mots_cles_propres = [mot[0] for mot in mots_importants[:30]]  # Ajustez le nombre selon vos besoins

#         return ', '.join(mots_cles_propres)
#     except (SyntaxError, ValueError):
#         return None

# # Appliquer la fonction de nettoyage à la colonne "keywords"
# df['keywords'] = df['keywords'].apply(nettoyer_mots_cles)

# # Enregistrer le DataFrame modifié dans un nouveau fichier CSV
# df.to_csv('main_propre.csv', index=False)



##################################################################################################################################



import pandas as pd

# Charger le fichier CSV propre
df = pd.read_csv('main_propre.csv')

# Créer des DataFrames pour chaque niveau
niveau1_df = df[df['niveau'] == 1].copy()
niveau2_df = df[df['niveau'] == 2].copy()
niveau3_df = df[df['niveau'] == 3].copy()

# Supprimer la colonne 'niveau'
niveau1_df.drop(columns=['niveau'], inplace=True)
niveau2_df.drop(columns=['niveau'], inplace=True)
niveau3_df.drop(columns=['niveau'], inplace=True)

# Enregistrer chaque DataFrame dans un fichier CSV distinct
niveau1_df.to_csv('niveau1_short.csv', index=False)
niveau2_df.to_csv('niveau2_short.csv', index=False)
niveau3_df.to_csv('niveau3_short.csv', index=False)

