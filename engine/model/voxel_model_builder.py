import numpy as np

from data.model import VoxelModel


class VoxelModelBuilder:
    """Build a voxel model from given data"""

    @property
    def layer(self):
        return self.__layer

    def __init__(self):
        self.__layers: list[np.ndarray[int]] = []
        self.__layer: int = 0

    def add_layer(self, layer: np.ndarray[int]):
        self.__layers.append(layer)
        self.__layer += 1

    def build(self) -> VoxelModel:
        layer_shape = self.__layers[0].shape
        shape = (layer_shape[0], layer_shape[1], self.__layer)
        array = np.ndarray(shape)

        i = 0
        for layer in self.__layers:
            array[:, :, i] = layer
            i += 1

        return VoxelModel(array)
