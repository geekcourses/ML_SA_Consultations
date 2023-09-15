import tensorflow as tf
print(tf.__version__)
# physical_devices = tf.config.list_physical_devices('GPU')
# tf.print(physical_devices)


print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
print("Num CPUs Available: ", len(tf.config.experimental.list_physical_devices('CPU')))