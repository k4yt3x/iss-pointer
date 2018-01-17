#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cardinal is the voice assistant for
ISS pointer
"""
import pygame
import os


def get_cpu_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return (temp.replace("temp=", ""))


class Cardinal:

    def __init__(self):
        self.voicefolder = './voicelines/'
        self.voicelines = {
            'cleargpio': 'cleargpio.mp3',
            'cpuoverheat': 'cpuoverheat.mp3',
            'issonline': 'issonline.mp3',
            'motorinit': 'motorinit.mp3',
            'servoinit': 'servoinit.mp3',
            'syncisstle': 'syncisstle.mp3',
            'termination': 'termination.mp3',
            'tlefail': 'tlefail.mp3',
            'tlesuccess': 'tlesuccess.mp3'
        }

    def sound_engine_init(self):
        pygame.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()

    def say(self, speech):
        try:
            vname = self.voicelines[speech]
        except FileNotFoundError:
            return False
        pygame.mixer.music.load(self.voicefolder + vname)
        clock = pygame.time.Clock()
        pygame.mixer.music.play()
        while pygame.mixer.get_busy():
            clock.tick(10)
