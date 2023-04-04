import moviepy.editor as mp

clip=mp.VideoFileClip(r"Singham Dialogue.mp4")

clip.audio.write_audiofile(r"Singham Audio File.mp3")
