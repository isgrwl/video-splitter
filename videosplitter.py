from moviepy.editor import * #import editor library
from zipfile import *
import os


def splitVideo(n,c,ff="mp4",t=None,f=None): 
    video = VideoFileClip(n) 

    clipSize = c #size of each clip
    cleanVideoLength = video.duration - (video.duration % clipSize)
    subclips = []
    filesToZip = []

    try:
        os.remove("clips.zip") #remove existing clips zip file
    except:
        pass

    for i in range(int(cleanVideoLength//clipSize)): # break into (clipSize) second clips
        subclips.append(video.subclip(i*clipSize,i*clipSize+clipSize))

    subclips.append(video.subclip(cleanVideoLength,video.duration)) # turn remaining time into final clip

    for i in range(len(subclips)): 
        newClipName= f"clip({i+1}).{ff}"
        subclips[i].write_videofile(newClipName,threads=t,fps=f) #create a video file for each subclip
        filesToZip.append(newClipName)

    with ZipFile("clips.zip","w") as zip: #zip the clips
        for clip in filesToZip:
            zip.write(clip)

    for clip in filesToZip: #delete all the unzipped files
        os.remove(clip)


splitVideo("sample.mp4",15,"mp4",1,30)
