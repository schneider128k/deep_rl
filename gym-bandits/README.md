# Bandit Environments

## Code History

I had started out with the code in [https://github.com/JKCooper2/gym-bandits](https://github.com/JKCooper2/gym-bandits). 
I have completely rewritten and reorganized the code. In particular, it now follows the guidelines 
in [https://github.com/openai/gym/tree/master/gym/envs](https://github.com/openai/gym/tree/master/gym/envs).  

## Description 

Consider the following learning problem. You are faced repeatedly with a choice among
k different options, or actions. After each choice you receive a numerical reward chosen
from a stationary probability distribution that depends on the action you selected. Your
objective is to maximize the expected total reward over some time period, for example,
over 1000 action selections, or time steps.

This is the original form of the k-armed bandit problem, so named by analogy to a slot
machine, or “one-armed bandit,” except that it has k levers instead of one. Each action
selection is like a play of one of the slot machine’s levers, and the rewards are the payoffs
for hitting the jackpot. Through repeated action selections you are to maximize your
winnings by concentrating your actions on the best levers.

**Currently, only** 

`BanditTenArmedGaussian-v0` 

**is available. I am working on implementing other k-armed bandit problem.**

* `BanditTenArmedGaussian-v0`: 10 armed bandit mentioned on page 30 of [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html) (Sutton and Barto)

## Installation

```
git clone https://github.com/schneider128k/drl.git
cd gym-bandits
pip install .
```

In your gym environment
```python
import gym_bandits
env = gym.make("BanditTenArmedGaussian-v0") # Replace with relevant env
```