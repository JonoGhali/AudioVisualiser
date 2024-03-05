from pydub import AudioSegment
from pydub.playback import play
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtMultimedia import QSound, QSoundEffect
from PyQt5.QtCore import QUrl
import matplotlib.pyplot as plt
import numpy as np

# create a main window with buttons for effects
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Audio Effects Processor")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.audio_file = None

        # Load Audio Button
        self.load_button = QPushButton("Load Audio File")
        self.load_button.clicked.connect(self.load_audio)
        self.layout.addWidget(self.load_button)

        # Play Button
        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_audio)
        self.layout.addWidget(self.play_button)

        # Add more buttons for other effects

    def load_audio(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Audio Files (*.mp3 *.wav *.m4a *.flac)")
        file_dialog.setViewMode(QFileDialog.List)
        if file_dialog.exec_():
            filenames = file_dialog.selectedFiles()
            if filenames:
                self.audio_file = filenames[0]
                print(f"Loaded audio file: {self.audio_file}")

    def play_audio(self):
        print("'Play Audio' Button Engaged")
        if self.audio_file:
            audio = AudioSegment.from_file(self.audio_file)
            audio.export("output.wav", format="wav")
            print("Audio Playing: {}".format(self.audio_file))
            play(audio)
            plot_waveform(audio)
        else:
            print("No audio file loaded. Please load an audio file first.")

    # Implement functions for other effects

def plot_waveform(audio):
    # Convert audio to numpy array
    samples = np.array(audio.get_array_of_samples())
    sample_rate = audio.frame_rate

    # Create time axis
    duration = len(samples) / sample_rate
    time_axis = np.linspace(0, duration, len(samples))

    # Plot waveform
    plt.figure(figsize=(8, 4))
    plt.plot(time_axis, samples)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title("Audio Waveform")
    plt.grid(True)
    plt.show()


def apply_effect1(self):
    # Apply effect 1 (e.g., echo)
    pass

# Implement functions for other effects

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()



