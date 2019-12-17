def make_env(env_name, seed=None, model=None):  # PW: removed unused value render_mode argument
	if env_name == 'car_racing':
		from custom_envs.car_racing import CarRacing
		env = CarRacing()
	elif env_name == 'car_racing_dream':
		from custom_envs.car_racing_dream import CarRacingDream
		env = CarRacingDream(model)
	else:
		print(f'environment {env_name} does not exist')
		# PW: added
		env = None

	if seed is not None:
		env.seed(seed)

	return env


def generate_data_action(env):
	a = env.action_space.sample()
	return a


def adjust_obs(obs):
	return obs.astype('float32') / 255.


def adjust_reward(reward):
	if reward > 0:
		reward = 1.0
	else:
		reward = 0.0
	return reward

