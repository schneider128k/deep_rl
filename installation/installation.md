## Install OpenAI gym on Windows 10

install Anaconda Python 3.7 version 64-Bit using Anaconda 2019.07 for Windows Installer; downloaded from [Anaconda Distribution](https://www.anaconda.com/distribution/) on 09/27/2019

use path ```C:\anaconda``` to install anaconda distribution

install Microsoft Visual Studio 2017 Community (version 15.9) and Build Tools for Visual Studio 2017 (version 15.9) from [Visual Studio download older versions](https://my.visualstudio.com/Downloads?q=visual%20studio%202017&wt.mc_id=o~msft~vscom~older-downloads)

It is important that the versions of python and build tools are compatible. See [python-windows-visual-c-14-required](https://www.scivision.dev/python-windows-visual-c-14-required/). I was getting the error *python-windows-visual-c-14-required* when trying to build atari-py because I had initially created the anaconda environment with the wrong version of python 3.5 instead of 3.6.

Using Anaconda navigotor create python 3.6 environment ```gym``` and install the following packages:

- ```jupyter```
- ```swig```
- ```git```
- ```pip``` 

Run the following commands inside an Anaconda powershell. Make sure that the ```gym``` environment is activated.

```
conda activate gym
pip install box2d-py
pip install gym
pip install git+https://github.com/Kojoley/atari-py.git
```

I think that it is best to install as many packages as possible with Anaconda Navigator or ```conda install``` instead of ```pip install```.  It is not possible to use ```conda install``` for the above three packages ```box2d-py```, ```gym```, and ```atari-py```. When pip installing these package, the following package are pip installed as well: ```cloudpickle```, ```numpy```, ```scipy```, ```future```, and ```pyglet```.  I haven't checked with, but maybe it would be better to conda install these packages, before pip installing the gym environment.  I will test this approach when installing everything from scratch 

### Create Conda environment in PyCharm

Follow instructions in [screenshot of Add Python Interpreter window in PyCharm](https://github.com/schneider128k/deep_rl/blob/master/installation/conda_environment_pycharm.png).

### Test gym install 

Run [```test_gym_install.py```](https://github.com/schneider128k/deep_rl/blob/master/installation/test_gym_install.py) to iterate though a couple of gym environments. Note that above installation does not include MuJoCo, which is required for some environments.

### Jupyter notebook 

The best is to use Anaconda navigator to launch jupyter Notebook.

### Tensorflow/Keras

Use Anaconda navigator to install ```tensorflow-gpu``` and ```keras-gpu```. I am working here with tensorflow 1.14.  Eventually, I plan to port to tensorflow 2.0.
