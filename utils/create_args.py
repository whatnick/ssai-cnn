#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def create_args():
    parser = argparse.ArgumentParser()

    # Training settings
    parser.add_argument('--model', type=str, default='models/MnihCNN.py')
    parser.add_argument('--gpu', type=int, default=0)
    parser.add_argument('--epoch', type=int, default=10000)
    parser.add_argument('--batchsize', type=int, default=64)
    parser.add_argument('--prefix', type=str, default='MnihCNN')
    parser.add_argument('--snapshot', type=int, default=10)

    # Dataset paths
    parser.add_argument('--train_ortho_db', type=str,
                        default='data/mass_buildings/train/ortho.lmdb')
    parser.add_argument('--train_label_db', type=str,
                        default='data/mass_buildings/train/label.lmdb')
    parser.add_argument('--valid_ortho_db', type=str,
                        default='data/mass_buildings/valid/ortho.lmdb')
    parser.add_argument('--valid_label_db', type=str,
                        default='data/mass_buildings/valid/label.lmdb')

    # Dataset info
    parser.add_argument('--ortho_original_side', type=int, default=96)
    parser.add_argument('--label_original_side', type=int, default=24)
    parser.add_argument('--ortho_side', type=int, default=64)
    parser.add_argument('--label_side', type=int, default=16)
    parser.add_argument('--channels', type=int, default=1)

    # Options for data augmentation
    parser.add_argument('--fliplr', type=int, default=1)
    parser.add_argument('--rotate', type=int, default=1)
    parser.add_argument('--angle', type=int, default=90)
    parser.add_argument('--norm', type=int, default=1)
    parser.add_argument('--clip', type=int, default=1)

    # Optimization settings
    parser.add_argument('--opt', type=str, default='Adam',
                        choices=['MomentumSGD', 'Adam', 'AdaGrad'])
    parser.add_argument('--weight_decay', type=float, default=0.0005)
    parser.add_argument('--alpha', type=float, default=0.001)
    parser.add_argument('--lr', type=float, default=0.0005)
    parser.add_argument('--lr_decay_freq', type=int, default=100)
    parser.add_argument('--lr_decay_ratio', type=float, default=0.1)
    parser.add_argument('--seed', type=int, default=1701)

    args = parser.parse_args()

    return args
