# xvfb-run -s "-screen 0 1400x900x24" python 01_generate_data.py
# car_racing --total_episodes 200 --time_steps 300

import numpy as np
import random
import argparse

from custom_envs.env import make_env, generate_data_action, adjust_obs, adjust_reward

DIR_NAME = './data/rollout/'


def generate_data(arguments):
    env_name = arguments.env_name
    total_episodes = arguments.total_episodes
    time_steps = arguments.time_steps
    render = arguments.render
    action_refresh_rate = arguments.action_refresh_rate

    print(f'Generating data for env {env_name}')
    env = make_env(env_name)
    # env = gym.make('CarRacing-v0')

    for episode_index in np.arange(total_episodes):
        episode_id = random.randint(0, 2**31 - 1)
        filename = f'{DIR_NAME}{episode_id}.npz'

        # data that will be generated
        #
        # s (state)               s' (new state)
        # r (reward)  a (action)  r' (new reward)
        # d (done)                d' (new done)
        #
        # this means that the number of states, rewards, done flags is larger than the number of actions by 1
        # the initial reward is 0

        # initial state
        observation = env.reset()
        observation = adjust_obs(observation)
        obs_sequence = [observation]
        reward_sequence = [0.0]
        done_sequence = [False]
        action_sequence = []
        # action=None needed; otherwise IDE warning about about potentially uninitialized variable
        action = None

        env.render()

        total_reward = 0.0
        for step in np.arange(time_steps):
            # select new action
            if step % action_refresh_rate == 0:
                action = generate_data_action(env)
            # take action
            action_sequence.append(action)
            observation, reward, done, _ = env.step(action)
            observation = adjust_obs(observation)
            obs_sequence.append(observation)
            # reward = adjust_reward(reward)
            reward_sequence.append(reward)
            done_sequence.append(done)

            total_reward += reward
            # print(total_reward)

            if total_reward < -10.0:
                break

            if render:
                env.render()

            if done:
                break

        print(f'Episode {episode_index} finished after {step} time steps')

        np.savez_compressed(filename,
                            obs=obs_sequence,
                            action=action_sequence,
                            reward=reward_sequence,
                            done=done_sequence)

    env.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create new training data')
    parser.add_argument('--env_name',
                        type=str,
                        default='car_racing',
                        help='name of environment')
    parser.add_argument('--total_episodes',
                        type=int,
                        default=200,
                        help='total number of episodes')
    parser.add_argument('--time_steps',
                        type=int,
                        default=300,
                        help='how many time steps at start of episode?')
    parser.add_argument('--action_refresh_rate',
                        type=int,
                        default=20,
                        help='how often to change the random action, in frames')
    parser.add_argument('--render',
                        type=int,
                        default=0,
                        help='render the env as data is generated')
    args = parser.parse_args()
    # generate arguments
    generate_data(args)
