import json

import numpy as np
import whisper_timestamped as whisper
from moviepy.editor import VideoFileClip

# Charger le modèle Whisper Timestamped
model = whisper.load_model("tiny", device="cpu")

# Chemin de la vidéo MP4
video_path = "2.mov"

# Extraire l'audio de la vidéo en utilisant moviepy
# video = VideoFileClip(video_path)
# audio = video.audio.to_soundarray()

# Ca marche mieux avec ça
audio = whisper.load_audio("nom_de_la_video.mp4")
audio = whisper.pad_or_trim(audio)

sample_rate = 44100  # Fréquence d'échantillonnage standard pour l'audio

# Définir la longueur des segments audio en secondes
segment_length = 10

# Diviser l'audio en segments plus petits
num_samples_per_segment = int(segment_length * sample_rate)
num_segments = len(audio) // num_samples_per_segment
audio_segments = np.array_split(audio, num_segments)

# Effectuer la transcription en anglais avec les horodatages pour chaque segment
transcriptions = []
for i, segment in enumerate(audio_segments):
    result = whisper.transcribe(model, segment, language="english")
    transcriptions.append(result)

# Afficher les résultats (un résultat pour chaque segment)
for i, result in enumerate(transcriptions):
    print(f"Transcription pour le segment {i + 1}:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
