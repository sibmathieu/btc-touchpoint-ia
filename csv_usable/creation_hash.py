# import os
# import pandas as pd
# import hashlib
# import json

# # Fonction pour calculer le hash MD5
# def calculate_hash(link, text):
#     hash_input = link + text
#     return hashlib.md5(hash_input.encode()).hexdigest()

# # Fonction pour créer le fichier JSON pour chaque ligne
# def create_json(row, output_folder):
#     data = {
#         "id": row['id'],
#         "text": "",
#         "title": row['title'],
#         "subtitle": row['subtitle'],
#         "description": row['description'],
#         "link": row['links'],
#         "quadrant": row['quadrant']
#     }
    
#     # Créer un fichier JSON dans le dossier spécifié avec le hash comme nom
#     with open(os.path.join(output_folder, f"{row['id']}.json"), 'w') as json_file:
#         json.dump(data, json_file)

# # Charger les fichiers CSV
# niveau1_df = pd.read_csv('niveau1.csv')
# niveau2_df = pd.read_csv('niveau2.csv')
# niveau3_df = pd.read_csv('niveau3.csv')

# # Créer une copie des DataFrames pour éviter de modifier les fichiers d'origine
# niveau1_df_copy = niveau1_df.copy()
# niveau2_df_copy = niveau2_df.copy()
# niveau3_df_copy = niveau3_df.copy()

# # Ajouter une colonne "id" avec le hash à chaque DataFrame
# niveau1_df_copy['id'] = niveau1_df_copy.apply(lambda row: calculate_hash(row['links'], row['description']), axis=1)
# niveau2_df_copy['id'] = niveau2_df_copy.apply(lambda row: calculate_hash(row['links'], row['description']), axis=1)
# niveau3_df_copy['id'] = niveau3_df_copy.apply(lambda row: calculate_hash(row['links'], row['description']), axis=1)

# # Créer un dossier pour les fichiers JSON
# output_folder = 'json_output'
# os.makedirs(output_folder, exist_ok=True)

# # Appliquer la fonction pour créer le fichier JSON pour chaque ligne
# niveau1_df_copy.apply(create_json, axis=1, output_folder=output_folder)
# niveau2_df_copy.apply(create_json, axis=1, output_folder=output_folder)
# niveau3_df_copy.apply(create_json, axis=1, output_folder=output_folder)

# # Enregistrer les DataFrames modifiés dans de nouveaux fichiers CSV
# niveau1_df_copy.to_csv('niveau1_modified.csv', index=False)
# niveau2_df_copy.to_csv('niveau2_modified.csv', index=False)
# niveau3_df_copy.to_csv('niveau3_modified.csv', index=False)










import os
import pandas as pd
import hashlib
import json

# Fonction pour calculer le hash MD5
def calculate_hash(link, text):
    hash_input = link + text
    return hashlib.md5(hash_input.encode()).hexdigest()

def get_text_from_transcript(link, ytb_transcript, web_transcript):
    if "youtube.com" in link:
        video_id_parts = link.split("v=")[1].split("&") if "&" in link else link.split("v=")[1:]
        if video_id_parts:
            video_id = video_id_parts[0]
            video_texts = []
            for entry in ytb_transcript:
                if entry.get("id", "") == video_id:
                    video_texts.extend(segment["text"] for segment in entry.get("transcripts", []))
            return "".join(video_texts)
    else:
        return web_transcript.get(link, {}).get("text", "")

# Fonction pour créer le fichier JSON pour chaque ligne
def create_json(row, output_folder, ytb_transcript, web_transcript):
    data = {
        "id": row['id'],
        "text": get_text_from_transcript(row['links'], ytb_transcript, web_transcript),
        "title": row['title'],
        "subtitle": row['subtitle'],
        "description": row['description'],
        "link": row['links'],
        "quadrant": row['quadrant']
    }

    # Créer un fichier JSON dans le dossier spécifié avec le hash comme nom
    with open(os.path.join(output_folder, f"{row['id']}.json"), 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)  # Ajout de l'argument indent


# Charger les fichiers CSV
niveau1_df = pd.read_csv('niveau1.csv')
niveau2_df = pd.read_csv('niveau2.csv')
niveau3_df = pd.read_csv('niveau3.csv')

# Créer une copie des DataFrames pour éviter de modifier les fichiers d'origine
niveau1_df_copy = niveau1_df.copy()
niveau2_df_copy = niveau2_df.copy()
niveau3_df_copy = niveau3_df.copy()

# Charger les fichiers de transcriptions
with open('C:/Users/maxim/Desktop/btc-touchpoint-ia/ytb_transcript.json', 'r', encoding='utf-8') as ytb_file:
    ytb_transcript_data = json.load(ytb_file)

with open('C:/Users/maxim/Desktop/btc-touchpoint-ia/venv/web_transcript.json', 'r', encoding='utf-8') as web_file:
    web_transcript_data = json.load(web_file)

# Ajouter une colonne "id" avec le hash à chaque DataFrame
niveau1_df_copy['id'] = niveau1_df_copy.apply(lambda row: calculate_hash(row['links'], row['description']), axis=1)
niveau2_df_copy['id'] = niveau2_df_copy.apply(lambda row: calculate_hash(row['links'], row['description']), axis=1)
niveau3_df_copy['id'] = niveau3_df_copy.apply(lambda row: calculate_hash(row['links'], row['description']), axis=1)

# Créer un dossier pour les fichiers JSON
output_folder = 'json_output'
os.makedirs(output_folder, exist_ok=True)

# Appliquer la fonction pour créer le fichier JSON pour chaque ligne
niveau1_df_copy.apply(create_json, axis=1, output_folder=output_folder, ytb_transcript=ytb_transcript_data, web_transcript=web_transcript_data)
niveau2_df_copy.apply(create_json, axis=1, output_folder=output_folder, ytb_transcript=ytb_transcript_data, web_transcript=web_transcript_data)
niveau3_df_copy.apply(create_json, axis=1, output_folder=output_folder, ytb_transcript=ytb_transcript_data, web_transcript=web_transcript_data)

# Enregistrer les DataFrames modifiés dans de nouveaux fichiers CSV
niveau1_df_copy.to_csv('niveau1_modified.csv', index=False)
niveau2_df_copy.to_csv('niveau2_modified.csv', index=False)
niveau3_df_copy.to_csv('niveau3_modified.csv', index=False)
