from setuptools import setup

setup(
    name = 'gym_bandits',
    version = '0.0.1',
    description = 'OpenAI gym environments - various multi armed bandit problems',
    author = 'Pawel Wocjan',
    packages = ['gym_bandits', 'gym_bandits.envs'],
    license = 'MIT License',
    install_requires = ['gym']  # And any other dependencies gym_bandits needs
)