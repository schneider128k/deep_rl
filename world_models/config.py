train_envs = ['car_racing']
test_envs = ['car_racing']


def generate_data_action(t, env):
    a = env.action_space.sample()
    return a


def adjust_obs(obs):
    return obs.astype('float32') / 255.


def adjust_reward(reward):
    if reward > 0:
        reward = 1
    else:
        reward = 0
    return reward
