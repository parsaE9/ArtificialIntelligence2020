from functions import *
from poet import Poet


if __name__ == "__main__":

    h3 = 0.9
    h2 = 0.099
    h1 = 0.001
    e = 0.00002

    ferdowsi = Poet('train_set//ferdowsi_train.txt', 'ferdowsi')
    hafez = Poet('train_set//hafez_train.txt', 'hafez')
    molavi = Poet('train_set//molavi_train.txt', 'molavi')

    verify_test_set(h3, h2, h1, e, ferdowsi, hafez, molavi, 'test_set//test_file.txt')