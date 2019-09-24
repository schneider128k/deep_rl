# Deep reinforcement learning

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

---

---

NEEDS TO BE UPDATED:

I am offering a weekly seminar on deep reinforcement learning in Spring 2019.  My goal is put together materials and code for a course on deep reinforcement learning that I would teach in Fall 2019 or Spring 2020.

### Rendering openai gym in Google colab ###

For demonstration purposes, it will be convenient to render opengym in Google colab. Here is a colab notebook showing how to accomplish this.

[Render openai gym in Google colab](https://colab.research.google.com/drive/1_fY8w7kqNE_vqB9QQWN6yJi0_Tb2OMJa)

[Train Acrobot with reward-to-go policy gradient, render performance after training](https://colab.research.google.com/drive/1uWByWJ2muHDVf3w6fl8PrQ74CL3DX-4s), the rendering is too slow

### Meeting on 02/08

I introduced the key concepts in RL and gave an overview of RL algorithms. I presented the mathematics behind the simplest policy gradient for categorical policies.

- [Part 1: Key Concepts in RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)
- [Part 2: Kinds of RL Algorithms](https://spinningup.openai.com/en/latest/spinningup/rl_intro2.html)
- [Part 3: Intro to Policy Optimization](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html)

The TensorFlow implementation of the simple gradient is available at [```1_simple_pg.py```](https://github.com/openai/spinningup/blob/master/spinup/examples/pg_math/1_simple_pg.py).

### Meeting on 02/15

I want to discuss the derivation of the improved *reward-to-go* policy gradient and to present its implementation in TensorFlow, which is  available at [```2_rtg_pg.py```](https://github.com/openai/spinningup/blob/master/spinup/examples/pg_math/2_rtg_pg.py).

Use the reward-to-go policy gradient algorithm to solve the following simple problems: 

- [Acrobot](https://gym.openai.com/envs/Acrobot-v1/)
- [Cartpole](https://gym.openai.com/envs/CartPole-v1/)
- [Lunar lander](https://gym.openai.com/envs/LunarLander-v2/)

Reimplement this algorithm using Keras.

[Solution for lunar lander](https://colab.research.google.com/drive/1uWByWJ2muHDVf3w6fl8PrQ74CL3DX-4s)

The policy found at the end managed to land the lunar lander, but only got approx. 50 as total reward. TODO: add the ability to save and load model.

### Meeting on 02/22

- Recap of reward-to-go policy gradient
- Improvements of reward-to-go policy gradient with baselines (value, q, and advantage functions)

## Meeting on 03/22

- Review of reinforcement learning basics (MDP, state value functions, state-action value functions, Bellman equations, temporal difference learning)

---

## Meeting

- policy gradient with base lines

### Meeting 

- Trust region policy gradient (TRPO)

### Meeting 

- Proximal policy optimization (PPO)

---

### Topics for future meetings

- Continuous action spaces
- [Trust region policy optimization](https://spinningup.openai.com/en/latest/algorithms/trpo.html)

  [Notes on trust region policy optimization](http://blog.luyiren.me/posts/trpo.html), 
  [MM algorithms](http://personal.psu.edu/drh20/papers/mmtutorial.pdf),
  [Trust region](https://en.wikipedia.org/wiki/Trust_region), 
  [Kakade et al.](https://papers.nips.cc/paper/2073-a-natural-policy-gradient.pdf), and
  [Kakade and Langford](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/KakadeLangford-icml2002.pdf)
  
  [Advanced policy gradient methods: natural gradient, TRPO, and more](http://rll.berkeley.edu/deeprlcourse/docs/lec5.pdf)
- [Proximal policy optimization](https://blog.openai.com/openai-baselines-ppo/)
- ...

---

### Review fundamental results

- gradient
- Jacobian matrix
- conjugate gradient method

  [Hessian free optimization](http://andrew.gibiansky.com/blog/machine-learning/hessian-free-optimization/), [Numerical optimization: understanding L-BFGS](http://aria42.com/blog/2014/12/understanding-lbfgs)
- KKT conditions
- Lagrangian duality

  [Lagrangian duality for dummies](https://cs.stanford.edu/people/davidknowles/lagrangian_duality.pdf)
- ...

---

### Folders

- The folder ```colab``` contains instructions how to install ```gym-retro``` (Atari games) on Google colab. More generally, it contains instructions how to access files in Google drive from a Colab notebook.
- The folder ```gym-bandits``` contains a new OpenAI environment for the multi-armed bandit problem. It can serve as a blue print for implementing new environments.
- The folder ```multi_armed_bandits``` contains some simple algorithms for the multi-armed bandit problem.
- In the folder ```tex```, I started describing basic RL algorithms. 
