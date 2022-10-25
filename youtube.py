from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'format: bestaudio/best'
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec':  'mp3',
        'preferredquality': '192',
    }]
}
a = input("Digite aqui o link: ")
print('baixando...')
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([a])
print('download completo!')