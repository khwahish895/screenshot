from moviepy.editor import *

clip = VideoFileClip("Karur_Exports_Company_-_Virtual_Fair(360p).mp4")

clip = clip.margin(60)
clip.write.videofile("new_margin.mp4")