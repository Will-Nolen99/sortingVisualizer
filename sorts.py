import pygame as pg
from draw import draw_sort
from element import Element
from bubble import bubble
from selection import selection
from quick import quick
from shell import shell
from gravity import gravity
from insertion import insertion
from radix import radix
from pancake import pancake


def get_sorts():
    
    algorithm = {
        "Selection sort": selection,
        "Bubble sort": bubble,
        "Quick sort": quick,
        "Shell sort": shell,
        "Gravity sort": gravity,
        "Insertion sort": insertion,
        "Radix sort": radix,
        "Pancake sort": pancake
    }
    
    return algorithm
 