from pydub import AudioSegment
from pydub.effects import spatialize

def export_bass_boost(file_path):
    # Load the input audio sample
    sample = AudioSegment.from_file(f"downloads/{file_path}.wav")
    
    boosted_sample = sample.low_pass_filter(210)

    # Adjust volume and overlay boosted track
    adjusted_sample = sample - 8
    combined = adjusted_sample.overlay(boosted_sample)
    
    # Export the enhanced audio
    combined.export(f"downloads/{file_path}.wav", format="wav")

def export_8d(file_path):
    sample = AudioSegment.from_file(f"downloads/{file_path}.wav")
    audio_8d = spatialize(sample, spatial_type='8d')
    audio_8d.export(f"downloads/{file_path}.wav", format="wav")

if __name__ == "__main__":
    # export_bass_boost("input")
    # export_8d("input")
    pass
