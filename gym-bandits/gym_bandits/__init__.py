from gym.envs.registration import register

register(
    id = 'BanditTenArmedGaussian-v0',
    entry_point = 'gym_bandits.envs:BanditTenArmedGaussianEnv',
    timestep_limit = 1000,
    nondeterministic = True
)
