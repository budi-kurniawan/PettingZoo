from pettingzoo.utils import random_demo
from pettingzoo.butterfly import pistonball_v3
env = pistonball_v3.env()

random_demo(env, render=True, cycles=1000)