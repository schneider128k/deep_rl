import gym
from gym import spaces
from gym.utils import seeding


class BanditEnv(gym.Env):
    """
    Bandit environment base

    arms:
        Number of arms
    """
    def __init__(self, arms: int):
        self.arms = arms
        self.action_space = spaces.Discrete(self.arms)
        self.observation_space = spaces.Discrete(1)
        self.np_random = None
        self.seed()
        self.reset()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self):
        pass

    def step(self, action: int):
        pass

    def render(self, mode='human', close=False):
        pass

