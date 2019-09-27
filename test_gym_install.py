import gym
import tensorflow as tf

# env = gym.make('SpaceInvaders-v0')
# env = gym.make('CartPole-v0')
# env = gym.make('Taxi-v2')
# env = gym.make('LunarLander-v2')

print(tf.__version__)

env = gym.make('CarRacing-v0')
env.reset()

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())

env.close()
