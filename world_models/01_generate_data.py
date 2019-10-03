# xvfb-run -s "-screen 0 1400x900x24" python 01_generate_data.py
# car_racing --total_episodes 200 --time_steps 300

import numpy as np
import random
import argparse

import gym

# project modules
import config
from env import make_env

DIR_NAME = './data/rollout/'


def generate_data(arguments):

    env_name = arguments.env_name
    total_episodes = arguments.total_episodes
    time_steps = arguments.time_steps
    render = arguments.render
    run_all_envs = arguments.run_all_envs
    action_refresh_rate = arguments.action_refresh_rate

    if run_all_envs:
        envs_to_generate = config.train_envs
    else:
        envs_to_generate = [env_name]

    for current_env_name in envs_to_generate:
        print("Generating data for env {}".format(current_env_name))

        env = make_env(current_env_name)
        # env = gym.make('CarRacing-v0')
        episode_idx = 0

        while episode_idx < total_episodes:

            episode_id = random.randint(0, 2**31 - 1)
            filename = DIR_NAME + str(episode_id) + ".npz"

            step = 0
            observation = env.reset()
            env.render()
            observation = config.adjust_obs(observation)
            obs_sequence = [observation]
            action_sequence = []
            reward_sequence = []
            done_sequence = []
            action = None

            while True:
                if step % action_refresh_rate == 0:
                    action = config.generate_data_action(env)

                observation, reward, done, info = env.step(action)
                if render:
                    env.render()
                observation = config.adjust_obs(observation)

                obs_sequence.append(observation)
                action_sequence.append(action)
                reward_sequence.append(reward)
                done_sequence.append(done)

                step += 1

                if done or step == time_steps:
                    break

            print("Episode {} finished after {} timesteps".format(episode_idx, step))

            np.savez_compressed(filename,
                                obs=obs_sequence,
                                action=action_sequence,
                                reward=reward_sequence,
                                done=done_sequence)

            episode_idx = episode_idx + 1

        env.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create new training data')
    parser.add_argument('env_name', type=str, help='name of environment')
    parser.add_argument('--total_episodes', type=int, default=200,
                        help='total number of episodes to generate per worker')
    parser.add_argument('--time_steps', type=int, default=300,
                        help='how many time steps at start of episode?')
    parser.add_argument('--render', default=0, type=int,
                        help='render the env as data is generated')
    parser.add_argument('--action_refresh_rate', default=20, type=int,
                        help='how often to change the random action, in frames')
    parser.add_argument('--run_all_envs', action='store_true',
                        help='if true, will ignore env_name and loop over all envs in train_envs variables in config.py')

    args = parser.parse_args()
    generate_data(args)
