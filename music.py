import discord
from discord.ext import commands
from pytube import YouTube, Playlist
from http.client import IncompleteRead
import os
import asyncio
import random
from youtube_search import YoutubeSearch
from export_bass_boost import export_audio_mega
from spotify import get_track_name_spotify, get_track_names_from_list_spotify
from radio import play_radio

class music(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    async def joined(self, ctx) -> bool or None:
        if ctx.author.voice is None:
            await ctx.send("Join a voice channel first.")
        voice_channel = ctx.author.voice.channel

        voice = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
        
        if ctx.voice_client is None:
            await voice_channel.connect()
            return True if voice == None else False
        else:
            await ctx.voice_client.move_to(voice_channel)
            return True if voice == None else False
            
    @commands.command(name="stop", aliases=['STOP','ыещз', 'ЫЕЩЗ'])
    async def stop(self, ctx):
        ctx.voice_client.stop()
        await ctx.voice_client.disconnect()
    
    @commands.command(name='skip', aliases=['SKIP','ылшз', 'ЫЛШЗ'])
    async def skip(self, ctx):
        ctx.voice_client.stop()

    @commands.command(name='play', aliases=['PLAY','здфн', 'ЗДФН'], description='play mega bass boost')
    async def play_mega(self, ctx, *, url):
        joined_now = await self.joined(ctx)
        
        ctx.voice_client.stop()
        vc = ctx.voice_client

        ctx.voice_client.play(discord.FFmpegPCMAudio(source='howdy.wav')) if joined_now else None

        if url.startswith("https://open.spotify.com/track/") is True:
            #search = YoutubeSearch(get_track_name_spotify(url), max_results=1).to_dict()
            search = (await asyncio.to_thread(YoutubeSearch, get_track_name_spotify(url), max_results=1)).to_dict()
            url = f"https://www.youtube.com/watch?v={search[0]['id']}"

        elif url.startswith("https://www.youtube.com/watch?") is False:
            search = (await asyncio.to_thread(YoutubeSearch, url, max_results=1)).to_dict()
            url = f"https://www.youtube.com/watch?v={search[0]['id']}"
        
        repl = ["/", "\\", ":", "*", "?", "<", ">", "|", '"']
        yt = await asyncio.to_thread(YouTube, url)
        
        if yt.length < 7201:
            audio = yt.streams.filter(only_audio=True).first()
            video_title = yt.title

            await ctx.send(video_title)

            for symbol in repl:
                video_title = video_title.replace(symbol, "")
            await asyncio.to_thread(audio.download, output_path="downloads/", filename=f"{video_title}.wav")

            await asyncio.to_thread(export_audio_mega, video_title)

            vc.play(discord.FFmpegPCMAudio(source=f'downloads/{video_title}.wav'))
            await asyncio.sleep(2)
            os.remove(f'downloads/{video_title}.wav')
        else:
            await ctx.send('Pick a video shorter than 2 hours')
    
    @commands.command(name='playlist', aliases=['PLAYLIST', 'здфндшые', 'ЗДФНДШЫЕ'])
    async def playlist(self, ctx, url=None, rand=None):
        if url is None:
            await ctx.send("syntax: playlist <link> (you can add r after the link to play in a random order: playlist <link> r)")
            return
        
        joined_now = await self.joined(ctx)

        ctx.voice_client.stop()
        vc = ctx.voice_client

        ctx.voice_client.play(discord.FFmpegPCMAudio(source='howdy.wav')) if joined_now else None

        if 'https://www.youtube.com/playlist?' in url:
            playlist = list(Playlist(url))

        elif 'https://open.spotify.com/playlist' in url:
            playlist = await asyncio.to_thread(get_track_names_from_list_spotify, url)
        
        if rand == 'r':
            random.shuffle(playlist)
        
        await ctx.send(f"{type(playlist)}, {playlist}")
        for url in playlist:
            repl = ["/", "\\", ":", "*", "?", "<", ">", "|", '"']
            yt = YouTube(url=url)

            if yt.length < 7201:
                try: 
                    audio = yt.streams.filter(only_audio=True).first()
                except IncompleteRead:
                    continue
                    
                video_title = yt.title

                await ctx.send(video_title)

                for symbol in repl:
                    video_title = video_title.replace(symbol, "")
                await asyncio.to_thread(audio.download, output_path="downloads/", filename=f"{video_title}.wav")

                await asyncio.to_thread(export_audio_mega, video_title)

                vc.play(discord.FFmpegPCMAudio(source=f'downloads/{video_title}.wav'))
                await asyncio.sleep(2)
                os.remove(f'downloads/{video_title}.wav')
                try: 
                    while ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
                        await asyncio.sleep(1)
                except AttributeError:
                    break
            else:
                await ctx.send('Pick a video shorter than 2 hours')

    @commands.command(name='radio')
    async def radio(self, ctx, station=None):
        station_names = ['global', 'mellow', 'rock', 'jazz', 'blues', 'dance', 'christmas', 'russian']
        if station == None or station not in station_names:
            await ctx.send(', '.join(station_names))
            return
        else:
            joined_now = await self.joined(ctx)

            ctx.voice_client.stop()
            vc = ctx.voice_client

            ctx.voice_client.play(discord.FFmpegPCMAudio(source='howdy.wav')) if joined_now else None
            await asyncio.sleep(2) if joined_now else None

            await play_radio(ctx, vc, station, station_names)
            
    @commands.command(name='pause', aliases=['зфгыу'])
    async def pause(self, ctx):
        try:
            await ctx.voice_client.pause()
        except:
            pass

    @commands.command(name='resume', aliases=['куыгьу'])
    async def resume(self, ctx):
        try:
            await ctx.voice_client.resume()
        except:
            pass
    

def setup(client):
    client.add_cog(music(client))
    