import numpy as np
import matplotlib.pyplot as plt
from utils import *
import copy
import math

# matplotlib inline

# load dataset
X_train, y_train = load_data("data/ex2data1.txt")

print(X_train[2, 1])