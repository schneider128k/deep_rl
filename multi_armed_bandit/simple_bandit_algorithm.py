import gym_bandits
import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make("BanditTenArmedGaussian-v0")

# A simple bandit algorithm
# Algorithm on page 32 of Reinforcement Learning by Sutton and Barto (2nd edition)

steps = 1000

arms = env.action_space.n

epsilons = [0.1, 0.01]

for epsilon in epsilons:
    env.seed(42)
    env.reset()

    q_values = np.zeros(arms)
    nums = np.zeros(arms)

    cumulative_reward = 0.0
    average_cumulative_rewards = np.zeros(steps)

    for step in np.arange(steps):
        if env.np_random.uniform() < epsilon:
            action = env.np_random.randint(arms)
        else:
            action = np.argmax(q_values)

        _, reward, _, _ = env.step(action)
        nums[action] = nums[action] + 1
        q_values[action] = q_values[action] + (1.0 / nums[action]) * (reward - q_values[action])

        cumulative_reward += reward
        average_cumulative_rewards[step] = (1.0 / (step + 1)) * cumulative_reward

    plt.plot(average_cumulative_rewards)

plt.plot(np.full(steps, np.max(env.means)))
plt.legend(
    (r'$\varepsilon=$' + str(epsilons[0]), r'$\varepsilon=$' + str(epsilons[1]), 'max mean'),
    shadow=True, loc=(0.5, 0.5), handlelength=1.5, fontsize=16)
plt.xlabel('Steps')
plt.ylabel('Average reward')
plt.title(r'Performance of a simple bandit algorithm with $\varepsilon$-greedy exploration')
plt.show()
