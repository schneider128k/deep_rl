# Deep reinforcement learning

I am offering a weekly seminar on deep reinforcement learning in Spring 2019.  My goal is put together materials and code for a course on deep reinforcement learning that I would teach in Fall 2019 or Spring 2020.

### Meeting on 02/08

I introduced the key concepts in RL and gave an overview of RL algorithms. I presented the mathematics behind the simplest policy gradient for categorical policies.

- [Part 1: Key Concepts in RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)
- [Part 2: Kinds of RL Algorithms](https://spinningup.openai.com/en/latest/spinningup/rl_intro2.html)
- [Part 3: Intro to Policy Optimization](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html)

### Meeting on 02/15

I want to discuss the derivation of the improved reward-to-go policy gradient and to present its implementation in TensorFlow and Keras. I also want to apply it this algorithm to problems such as 
- [Acrobot](https://gym.openai.com/envs/Acrobot-v1/)
- [Cartpole](https://gym.openai.com/envs/CartPole-v1/)
- [Lunar lander](https://gym.openai.com/envs/LunarLander-v2/)

---

### Topics for future meetings

- Policy gradients for continuous action spaces
- [Proximal policy optimization](https://blog.openai.com/openai-baselines-ppo/)
- ...

---

- The folder ```colab``` contains instructions how to install ```gym-retro``` (Atari games) on Google colab. More generally, it contains instructions how to access files in Google drive from a Colab notebook.
- The folder ```gym-bandits``` contains a new OpenAI environment for the multi-armed bandit problem. It can serve as a blue print for implementing new environments.
- The folder ```multi_armed_bandits``` contains some simple algorithms for the multi-armed bandit problem.
- In the folder ```tex```, I started describing basic RL algorithms. 
