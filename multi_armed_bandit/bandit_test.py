import gym_bandits
import gym
import numpy as np

env = gym.make("BanditTenArmedGaussian-v0") # Replace with relevant env

env.reset()

steps = 1000
average = 0.0

print("Number of actions", env.action_space.n)

for _ in np.arange(steps):
    _, reward, _, _ = env.step(0)
    average += reward

average /= steps

print("average reward:", average)
