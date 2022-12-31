from pytube import Youtube
import moviepy.editor as mp
import re
import os

link = input ("Digite o link do video: ")
path = input ("Digite o dir que deseja salvar o video: ")
yt = Youtube()

print("Baixando")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Dowload completo!")


#convertendo mp4 para mp3
print("Convertendo...")
for file in os.search('mp4', file):
    mp4_path = os.path.join(path, file)
    mp3_path = os.path.join(path,os.path.splitext(file)[0]+'.mp3')
    new_file=mp.AudioFileClip(mp4_path)
    new_file.write_audiofile(mp3_path)
    os.remove(mp4_path)
print('Sucesso!')
