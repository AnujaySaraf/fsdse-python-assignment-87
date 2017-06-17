import pandas as pd


def solution(array):
    """
    Series 2 panda
    """
    pandaArray = pd.Series(array)
    print pandaArray
    return pandaArray

solution([2, 4, 6, 8, 10])
