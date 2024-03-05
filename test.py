from pydub import AudioSegment
from pydub.playback import play
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtMultimedia import QSound, QSoundEffect
from PyQt5.QtCore import QUrl
import matplotlib.pyplot as plt
import numpy as np

def playAudio():
    audio = AudioSegment.from_file("sleeper.flac", format="flac")
    audio.export("output.wav", format="wav")
    play(audio)


if __name__ == "__main__":
    playAudio()