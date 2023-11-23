from pydub import AudioSegment

def export_bass_boost(file_path):
    # Load the input audio sample
    sample = AudioSegment.from_file(f"downloads/{file_path}.wav")
    
    boosted_sample = sample.low_pass_filter(210)

    # Adjust volume and overlay boosted track
    adjusted_sample = sample - 8
    combined = adjusted_sample.overlay(boosted_sample)
    
    # Export the enhanced audio
    combined.export(f"downloads/{file_path}.wav", format="wav")

if __name__ == "__main__":
    export_bass_boost("input")
