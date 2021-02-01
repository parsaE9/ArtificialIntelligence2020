from functions import *
from poet import Poet


if __name__ == "__main__":

    h3 = 0.8
    h2 = 0.2
    h1 = 0.1
    e = 0.2

    ferdowsi = Poet('train_set//ferdowsi_train.txt', 'ferdowsi', h3, h2, h1, e)
    hafez = Poet('train_set//hafez_train.txt', 'hafez', h3, h2, h1, e)
    molavi = Poet('train_set//molavi_train.txt', 'molavi', h3, h2, h1, e)

