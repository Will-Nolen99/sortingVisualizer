from noise import snoise2
import random as r


def make_array(length):
    random_num = r.randint(0, 10000)
    array = [ 500 * abs(snoise2(.005 * i, random_num)) for i in range(length)]
    return list(map(lambda x: Element(x), array))


class Element:
    def __init__(self, val):
        self.val = val
        self.status = "normal"