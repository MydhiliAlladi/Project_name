import os
from pydub import AudioSegment

RAW_AUDIO_PATH = "../data/raw_audio"
PROCESSED_AUDIO_PATH = "../data/processed_audio"

os.makedirs(PROCESSED_AUDIO_PATH, exist_ok=True)

for file in os.listdir(RAW_AUDIO_PATH):
    if file.endswith((".mp3", ".wav", ".m4a")):
        input_path = os.path.join(RAW_AUDIO_PATH, file)
        output_file = file.split(".")[0] + ".wav"
        output_path = os.path.join(PROCESSED_AUDIO_PATH, output_file)

        print(f"Processing: {file}")

        audio = AudioSegment.from_file(input_path)
        audio = audio.set_frame_rate(16000).set_channels(1)
        audio.export(output_path, format="wav")

        print(f"Saved: {output_file}")

print("Audio preprocessing completed successfully.")
