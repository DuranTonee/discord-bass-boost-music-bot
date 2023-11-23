from pydub import AudioSegment
import numpy as np
import math

def export_audio_mega(file_path):
    # Load the input audio sample
    sample = AudioSegment.from_file(f"downloads/{file_path}.wav")
    sample_track = np.array(sample.get_array_of_samples())
    
    boosted_sample = sample_track.low_pass_filter(400)

    # Adjust volume and overlay boosted track
    adjusted_sample = sample - 8
    combined = adjusted_sample.overlay(boosted_sample)
    
    # Export the enhanced audio
    combined.export(f"downloads/{file_path}.wav", format="wav")

if __name__ == "__main__":
    export_audio_mega("input")
