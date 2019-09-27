## Install OpenAI gym on Windows 10

- install Anaconda Python 3.7 version 64-Bit from [Anaconda](https://www.anaconda.com/) 

- install Microsoft Visual Studio 2017 Community (version 15.9) and Build Tools for Visual Studio 2017 (version 15.9) from [Visual Studio download older versions](https://my.visualstudio.com/Downloads?q=visual%20studio%202017&wt.mc_id=o~msft~vscom~older-downloads)

It is important that the versions of python and build tools are compatible. See [python-windows-visual-c-14-required](https://www.scivision.dev/python-windows-visual-c-14-required/). I was getting the error *python-windows-visual-c-14-required* when trying to build atari-py because I had initially created the anaconda environment with the wrong version of python 3.5 instead of 3.6.

Runn the following commands insider an Anaconda powershell.

```
conda create --name gym python=3.6 pip
conda activate gym
conda env list
pip install gym
conda install git
pip install git+https://github.com/Kojoley/atari-py.git
conda install swig
pip install box2d-py
pip install gym[box2d]
```

After running the above commands the following packages are installed in the environment ```gym```:

```
(gym) C:\Users\PW>
# packages in environment at C:\anaconda\envs\gym:
#
# Name                    Version                   Build  Channel
atari-py                  1.2.1                    pypi_0    pypi
box2d-py                  2.3.8                    pypi_0    pypi
certifi                   2019.6.16                py36_1
cloudpickle               1.2.2                    pypi_0    pypi
future                    0.17.1                   pypi_0    pypi
git                       2.20.1               h6bb4b03_0
gym                       0.14.0                   pypi_0    pypi
numpy                     1.17.2                   pypi_0    pypi
pip                       19.2.2                   py36_0
pyglet                    1.3.2                    pypi_0    pypi
python                    3.6.9                h5500b2f_0
scipy                     1.3.1                    pypi_0    pypi
setuptools                41.0.1                   py36_0
six                       1.12.0                   pypi_0    pypi
sqlite                    3.29.0               he774522_0
swig                      3.0.12               h047fa9f_3
vc                        14.1                 h0510ff6_4
vs2015_runtime            14.16.27012          hf0eaf9b_0
wheel                     0.33.4                   py36_0
wincertstore              0.2              py36h7fe50ca_0
```

### Jupyter notebook 

The best is to use Anaconda navigator to launch jupyter Notebook.

I initially tried following [jupyter virtual environments](https://janakiev.com/blog/jupyter-virtual-envs/), but I decided that it's easier to use Anaconda navigator.
