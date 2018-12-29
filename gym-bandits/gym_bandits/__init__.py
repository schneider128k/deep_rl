from gym.envs.registration import register

register(
    id = 'BanditTenArmedGaussian-v0',
    entry_point = 'gym_bandits.envs:BanditTenArmedGaussianEnv',
    nondeterministic = True
)
