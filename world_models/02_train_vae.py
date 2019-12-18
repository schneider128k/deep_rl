#python 02_train_vae.py --new_model

import argparse
import numpy as np
import os
import sys

from vae.arch import VAE

DIR_NAME = './data/rollout/'
M = 300 + 1  # time steps plus 1
SCREEN_SIZE_X = 64
SCREEN_SIZE_Y = 64


def import_data(num_episodes):
    filenames = os.listdir(DIR_NAME)
    filenames = [filename for filename in filenames if filename.endswith('.npz')]
    filenames.sort()

    num_episodes = min(num_episodes, len(filenames))
    filenames = filenames[:num_episodes]
    # assumes that number of observations is 301 (time steps plus 1)
    # shorter episodes will be skipped
    data = np.zeros((M * num_episodes, SCREEN_SIZE_X, SCREEN_SIZE_Y, 3), dtype=np.float32)
    imported_idx = 0

    for idx in np.arange(num_episodes):
        try:
            new_data = np.load(DIR_NAME + filenames[idx])['obs']
            print(new_data.shape)
            data[imported_idx * M:(imported_idx + 1) * M, :, :, :] = new_data[:M, :, :, :]
            imported_idx += 1

        except (IOError, ValueError):
            print(f'=======================> Skipped {filenames[idx]}')

    print(f'Imported {imported_idx} out of {num_episodes} episodes')

    return data, num_episodes


def main(args):
    reuse_weights = args.reuse_weights
    num_episodes = int(args.num_episodes)
    epochs = int(args.epochs)

    vae = VAE()

    if reuse_weights:
        try:
            print('===> loading previously saved weights')
            vae.set_weights('./vae/weights.h5')

        except:  # do not use bare except
            print("Either set --new_model or ensure ./vae/weights.h5 exists")
            raise

    try:
        data, num_episodes = import_data(num_episodes)

    except:  # do not use bare except
        print('NO DATA FOUND')
        raise

    print(f'DATA SHAPE = {data.shape}')

    for epoch in range(epochs):
        print('EPOCH ' + str(epoch))
        vae.train(data)
        vae.save_weights('./vae/weights.h5')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train VAE')
    parser.add_argument('--num_episodes', default=200, help='number of episodes to use to train')
    parser.add_argument('--reuse_weights', default=True, help='start a new model from scratch?')
    parser.add_argument('--epochs', default=10, help='number of epochs to train for')
    args = parser.parse_args()

    main(args)
