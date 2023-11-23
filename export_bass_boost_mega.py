from pydub import AudioSegment
import numpy as np
import math

def apply_bass_boost(sample_track, est_mean, est_std):
    bass_factor = int(round((est_std - est_mean) * 0.010))
    print(bass_factor)

    boosted_track = sample_track.low_pass_filter(bass_factor)

    return boosted_track

def export_audio_mega(file_path):
    # Load the input audio sample
    sample = AudioSegment.from_file(f"downloads/{file_path}.wav")
    sample_track = np.array(sample.get_array_of_samples())
    
    est_mean = np.mean(sample_track)
    est_std = 3 * np.std(sample_track) / (math.sqrt(2))

    # Apply the bass boost effect
    boosted_sample = apply_bass_boost(sample, est_mean, est_std)

    # Adjust volume and overlay boosted track
    adjusted_sample = sample - 8
    combined = adjusted_sample.overlay(boosted_sample)
    
    # Export the enhanced audio
    combined.export(f"downloads/{file_path}.wav", format="wav")

if __name__ == "__main__":
    export_audio_mega("input")
