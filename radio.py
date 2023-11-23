import discord
import random

async def play_radio(ctx, vc, station, station_names):
    await ctx.send('Radio mode. Global. Source: http://stream.radioparadise.com/global-128') and vc.play(discord.FFmpegPCMAudio('http://stream.radioparadise.com/global-128')) if station == station_names[0] else None
    if station == 'mellow':
        mellow_stations = ['http://stream.radioparadise.com/mellow-128', 
                            'http://listen.181fm.com/181-mellow_128k.mp3?noPreRoll=true',
                            'https://ais-edge106-live365-dal02.cdnstream.com/a56104',
                            ]
        mellow_link = random.choice(mellow_stations)
        await ctx.send(f'Radio mode. Mellow. Source: {mellow_stations.index(mellow_link)+1}. {mellow_link}') and vc.play(discord.FFmpegPCMAudio(mellow_link))

    if station == 'rock':
        rock_stations = ['http://stream.radioparadise.com/rock-128', 
                            'http://s4-webradio.rockantenne.de/90er-rock/stream/mp3?aw_0_1st.playerid=com',
                            'http://stream.104.6rtl.com/rtl-poprock/mp3-192/',
                            'https://stream.starfm.de/feelgood/mp3-192'
                            ]
        rock_link = random.choice(rock_stations)
        await ctx.send(f'Radio mode. Rock. Source: {rock_stations.index(rock_link)+1}. {rock_link}') and vc.play(discord.FFmpegPCMAudio(rock_link))

    if station == 'jazz':
        jazz_stations = ['https://smoothjazz.cdnstream1.com/2586_256.mp3', 
                            'http://52.201.196.36/ppm-jazz24mp3-ibc1?session-id=452acb7e65b6165f076db770fcdf77a5',
                            'http://stream-158.zeno.fm/tvt6bya8hg8uv?zs=wBua8mH8Qi2OBM1UbH0-Pg',

                            ]
        jazz_link = random.choice(jazz_stations)
        await ctx.send(f'Radio mode. Jazz. Source: {jazz_stations.index(jazz_link)+1}. {jazz_link}') and vc.play(discord.FFmpegPCMAudio(jazz_link))

    if station == 'blues':
        blues_stations = ['https://starfm.streamabc.net/30-bluesrock-aacplus-64-4776790?sABC=6554r4r8%230%234q21ss1n5q12ss419pq09o7sq86q3382%23&aw_0_1st.playerid=&amsparams=playerid:;skey:1700062440',
                            'https://i4.streams.ovh/sc/bluesrad/stream',
                            'http://regiocast.streamabc.net/regc-radiobobblues6003375-mp3-192-4052902?sABC=6554r55s%230%235n58rs2708468248rpnos73r7pqr9716%23&aw_0_1st.playerid=&amsparams=playerid:;skey:1700062559',
                            'http://listen.181fm.com/181-blues_128k.mp3?noPreRoll=true',
                            ]
        blues_link = random.choice(blues_stations)
        await ctx.send(f'Radio mode. Blues. Source: {blues_stations.index(blues_link)+1}. {blues_link}') and vc.play(discord.FFmpegPCMAudio(blues_link))

    if station == 'dance':
        dance_stations = ['http://stream-154.zeno.fm/cygwwun7a5zuv?zs=sxyxlB7PQu2UqdX1DBPWEg']
        dance_link = random.choice(dance_stations)
        await ctx.send(f'Radio mode. Dance. Source: {dance_stations.index(dance_link)+1}. {dance_link}') and vc.play(discord.FFmpegPCMAudio(dance_link))

    if station == 'christmas':
        xmas_stations = ['https://starfm.streamabc.net/30-christmasrock-mp3-192-7174283?sABC=6553nn0q%230%234q21ss1n5q12ss419pq09o7sq86q3382%23&aw_0_1st.playerid=&amsparams=playerid:;skey:1699981837', ]
        xmas_link = random.choice(xmas_stations)
        await ctx.send(f'Radio mode. Christmas. Source: {xmas_stations.index(xmas_link)+1}. {xmas_link}') and vc.play(discord.FFmpegPCMAudio(xmas_link))

    if station == 'russian':
        russian_stations = ['http://live.ruradio.md:8000/ruradio']
        russian_link = random.choice(russian_stations)
        await ctx.send(f'Radio mode. Russian. Source: {russian_stations.index(russian_link)+1}. {russian_link}') and vc.play(discord.FFmpegPCMAudio(russian_link))


# ctx.voice_client.play(discord.FFmpegPCMAudio(source='downloads/howdy.wav')) if joined_now else None