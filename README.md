# discord-bass-boost-music-bot
This project is a Discord bot designed to enhance your audio experience by playing bass-boosted music from YouTube and Spotify. It uses the [discord.py](https://github.com/Rapptz/discord.py) library to handle interactions with the Discord API and employs the [pydub](https://github.com/jiaaro/pydub) library to create a bass boost effect.
# Features
* **YouTube and Spotify Integration**: Play your favorite bass-boosted tracks from YouTube and Spotify.
* **Bass Boost Effect**: Experience enhanced audio with a powerful bass boost effect
* **Radio Streaming**: Explore a variety of music genres by tuning into radio stations
# Quick notes
* The bot does not extract the audio, but downloads it for later filtering.
* [Pytube](https://github.com/pytube/pytube) was used instead of [youtube-dl](https://github.com/ytdl-org/youtube-dl) because of the download speed.
* It takes some time to download and apply filters to the audio depending on your PC and internet.
* Supports playlists (YouTube and Spotify) instead of making queues.
# Commands
* **play** - plays bass boosted version of the track
* **playlist** - plays bass boosted version of tracks in the playlist (can play in random order: `!playlist <link> r`
* **skip** - stops the current track (and plays the next one, if it's playlist)
* **stop** - stops the current track and disconnects from the channel. **Required to reset the playlist** <sub>sorry</sub>
* **radio** - plays streamed audio from different sources
# Getting started (more info below)
1. Install requirements:
   `pip install -r requirements.txt`
2. Create .env file at your project's root directory.
3. Add your _sensitive_ information:
   ```
    # discord bot token
    BOT_TOKEN = ""
    # spotify stuff
    CLIENT_ID=""
    CLIENT_SECRET=""
   ```
   Acquire CLIENT_ID and CLIENT_SECRET from your [Spotify app](https://developer.spotify.com/dashboard)
4. Run main.py
   
> [!TIP]
> You may encounter **AgeRestrictedError** while downloading a YouTube video. Solution [here](https://stackoverflow.com/questions/75791765/how-to-download-videos-that-require-age-verification-with-pytube)
# How some parts work
## Spotify (spotify.py)
Of course it doesn't download directly from Spotify. The bot parses data (track name and author) using [Spotify for Developers](https://developer.spotify.com/) and then searches YouTube via [youtube-search](https://pypi.org/project/youtube-search/)
![image](https://github.com/DuranTonee/discord-bass-boost-music-bot/assets/95922080/37f9e0ed-c511-4ffc-a722-e3258818b63a)

Supports playlists:

![image](https://github.com/DuranTonee/discord-bass-boost-music-bot/assets/95922080/ed0e6f94-1c33-4d82-bb2b-23c4c8ba41bd)

> [!IMPORTANT]
> You have to acquire CLIENT_ID and CLIENT_SECRET from your [Spotify app](https://developer.spotify.com/dashboard)

## Bass boost effect (export_audio.py)
Downloads the audio from YouTube and applies low_pass_filter effect to the sample and combines original and filtered samples:
```
...
boosted_sample = sample.low_pass_filter(210)

adjusted_sample = sample - 8
combined = adjusted_sample.overlay(boosted_sample)
...
```
## Radio (radio.py)
Streams the audio from radio station links divided by different genres (rock, jazz, mellow...) 

**_Disclaimer: I do not own any of these radio stations nor sources. They are the property of their rightful owners._** 

Some of them have different sources that will be played randomly:
```
...
if station == 'rock':
    rock_stations = ['http://stream.radioparadise.com/rock-128', 
                        'http://s4-webradio.rockantenne.de/90er-rock/stream/mp3?aw_0_1st.playerid=com',
                        'http://stream.104.6rtl.com/rtl-poprock/mp3-192/',
                        'https://stream.starfm.de/feelgood/mp3-192'
                        ]
    rock_link = random.choice(rock_stations)
    await ctx.send(f'Radio mode. Rock. Source: {rock_stations.index(rock_link)+1}. {rock_link}') and vc.play(discord.FFmpegPCMAudio(rock_link))
...
```
