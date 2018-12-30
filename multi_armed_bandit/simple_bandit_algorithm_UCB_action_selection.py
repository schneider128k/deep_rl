import gym_bandits
import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make("BanditTenArmedGaussian-v0")

# A simple bandit algorithm
# Modification of algorithm on page 32 of Reinforcement Learning by Sutton and Barto (2nd edition)
# Upper-confidence-bound action selection instead of epsilon-greedy action selection
# Section 2.7 on page 35

steps = 500

arms = env.action_space.n

env.seed(42)
env.reset()

q_values = np.zeros(arms)
nums = np.zeros(arms)

cumulative_reward = 0.0
average_cumulative_rewards = np.zeros(steps)

# constant controlling exploration
c = 2.0

for step in np.arange(steps):

    if step < arms:
        action = step
    else:
        action = np.argmax(q_values + c * np.sqrt(np.log(step + 1.0) / nums))

    _, reward, _, _ = env.step(action)
    nums[action] += 1.0
    q_values[action] = q_values[action] + (1.0 / nums[action]) * (reward - q_values[action])

    cumulative_reward += reward
    average_cumulative_rewards[step] = (1.0 / (step + 1)) * cumulative_reward

plt.plot(average_cumulative_rewards)

plt.plot(np.full(steps, np.max(env.means)))
plt.legend(
    (r'$c=$' + str(c), 'max mean'),
    shadow=True, loc=(0.5, 0.5), handlelength=1.5, fontsize=16)
plt.xlabel('Steps')
plt.ylabel('Average reward')
plt.title(r'Performance of a simple bandit algorithm with UCB action selection')
plt.show()
