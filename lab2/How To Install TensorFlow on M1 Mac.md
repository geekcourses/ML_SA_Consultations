# Install TensorFlow on M1 Mac

### Reference: [https://www.tensorflow.org/install/pip](https://www.tensorflow.org/install/pip)

1. Homebrew:
   1. Check if it is installed:
		open terminal and type:

		`brew`
   2. If not installed:

   `/bin/bash -c “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

2. Install Xcode Command Line Tools:

	`xcode-select --install`

3. Install miniforge for arm64 (Apple Silicon) from [miniforge GitHub](https://github.com/conda-forge/miniforge).

4. Turn off the default base conda env by:

   `conda config --set auto_activate_base false`

5. Create a virtual environment:

	`conda create --name ml_38 python=3.8`

6. Activate it:

	`conda activate mlp`

7. Update pip:

   `pip install --upgrade pip`

8. Install Tensorflow-MacOS:

	```
	#  Tensorflow dependencies:
	conda install -c apple tensorflow-deps

	#  base TensorFlow:
	pip install tensorflow-macos

	# metal plugin:
	pip install tensorflow-metal
	```

9.  Run a Benchmark by training the MNIST dataset:

   `pip install tensorflow_datasets`

10. Create new python file with next code to show device info:

	```
	import tensorflow as tf

	print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
	print("Num CPUs Available: ", len(tf.config.experimental.list_physical_devices('CPU')))

	```

11. Run the benchmark code, given in: [github.com/apple/tensorflow_macos/issues/25](https://github.com/apple/tensorflow_macos/issues/25)