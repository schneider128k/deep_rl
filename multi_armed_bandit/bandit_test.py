import gym_bandits
import gym
import numpy as np

env = gym.make("BanditTenArmedGaussian-v0")
env.seed(42)
env.reset()

steps = 10000
average = 0.0

print("BanditTenArmedGaussian-v0")
print("Means:", env.means)

for _ in np.arange(steps):
    _, reward, _, _ = env.step(0)
    average += reward

average /= steps

print("Average reward for arm 0:", average)
