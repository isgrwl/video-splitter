from moviepy.editor import * #import MoviePy
from zipfile import *
import os

def splitVideo(n,c,fe,t,fps): 
    video = VideoFileClip(n) 

    clipSize = c #size of each clip
    cleanVideoLength = video.duration - (video.duration % clipSize)
    subclips = []
    filesToZip = []

    try:
        os.remove("clips.zip") #remove existing clips zip file in case program is run multiple times
    except:
        pass

    for i in range(int(cleanVideoLength//clipSize)): # break into (clipSize) second clips
        subclips.append(video.subclip(i*clipSize,i*clipSize+clipSize))

    subclips.append(video.subclip(cleanVideoLength,video.duration)) # turn remaining time into final clip

    for i in range(len(subclips)): 
        newClipName= f"clip({i+1}).{fe}"
        subclips[i].write_videofile(newClipName,threads=t,fps=f) #create a video file for each subclip
        filesToZip.append(newClipName)

    with ZipFile("clips.zip","w") as zip: #zip the clips
        for clip in filesToZip:
            zip.write(clip)

    for clip in filesToZip: #delete all the unzipped files
        os.remove(clip)

def main():
    fileName = "sample.mp4" #name of input file
    clipLength = 60 #length of output clips (in seconds)
    fileType = ".mp4" #output clip filetype
    threads = 1 #change this to however many threads your pc can use
    fps = 30 #fps of output clips

    splitVideo(fileName,clipLength,fileType,threads,fps)


main()
