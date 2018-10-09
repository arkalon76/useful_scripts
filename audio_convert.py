#!/usr/bin/python3
import glob, os
from pymediainfo import MediaInfo

rootDir = './Downloads'

def findTrueHDFiles():
    for dirName, subdirList, fileList in os.walk(rootDir):
        #print('Found directory: %s' % dirName)
        for fname in fileList:
            if fname[-3:] == 'mkv' and "sample" not in fname:
                print('\t%s' % fname)
                os.chdir(dirName)
                media_info = MediaInfo.parse(fname)
                for track in media_info.tracks:
                    if track.track_type == 'Audio' and "Atmos" in track.codec:
                        print('Converting ' + fname)
                        os.system('ffmpeg -y -i ' + fname + ' -c:v copy -c:a eac3 ' + os.path.splitext(fname)[0] + '.mp4')
                #os.system('ffmpeg -i ' + fname + ' -c:v copy -c:a eac3 ' + os.path.splittext(fname)[0] )

if __name__ == "__main__":
    filesToConvert = findTrueHDFiles()
