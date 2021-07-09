import tensorflow as tf
import tensorflow_io as tfio

audio = tfio.audio.AudioIOTensor('audio/example1.m4a')

print(audio)
