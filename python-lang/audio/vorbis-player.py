import sys
import pygame
import time
from mutagen.oggvorbis import OggVorbis
pygame.init()


file = OggVorbis(sys.argv[1])
pygame.mixer.music.load(sys.argv[1])
pygame.mixer.music.play()
time.sleep(file.info.length)
