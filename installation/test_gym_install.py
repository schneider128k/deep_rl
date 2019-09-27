import gym

max_num_steps = 10000

env_ids = [
    'ChopperCommand-v0',
    'BattleZone-v0',
    'SpaceInvaders-v0',
    'Acrobot-v1',
    'CartPole-v0',
    'Taxi-v2',
    'LunarLander-v2',
    'BipedalWalker-v2',
    'CarRacing-v0'
]

for env_id in env_ids:

    env = gym.make(env_id)
    env.reset()

    for _ in range(max_num_steps):
        env.render()
        _, _, done, _ = env.step(env.action_space.sample())
        if done:
            break

    env.close()
