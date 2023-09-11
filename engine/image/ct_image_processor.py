import numpy as np


class CTImageProcessor:

    def __init__(self):
        self.BONE_MIN_VALUE = 180

    def extract_bone_data(self, img: np.ndarray) -> np.ndarray:
        """:returns: ndarray of ints where the value is 0 for none-bone pixels and 1 for bone pixels"""
        copy = img.copy()
        copy[img < self.BONE_MIN_VALUE] = 0
        copy[img >= self.BONE_MIN_VALUE] = 1
        return copy
