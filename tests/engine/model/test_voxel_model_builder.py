import unittest

import numpy as np

from engine.model import VoxelModelBuilder
from data.model import VoxelModel


class TestVoxelModelBuilder(unittest.TestCase):

    def setUp(self):
        self.sut = VoxelModelBuilder()

    def test_add_layer(self):
        # Act
        self.sut.add_layer(np.array([[1, 0], [1, 0]]))
        # Assert
        self.assertEqual(1, self.sut.layer)

    def test_build(self):
        # Arrange
        self.__build_test_model()
        # Act
        result: VoxelModel = self.sut.build()
        # Assert
        self.assertEqual((2, 2, 5), result.voxels.shape)

    def __build_test_model(self):
        self.sut.add_layer(np.array([[1, 0], [0, 1]]))
        self.sut.add_layer(np.array([[1, 0], [0, 1]]))
        self.sut.add_layer(np.array([[1, 0], [0, 1]]))
        self.sut.add_layer(np.array([[1, 0], [0, 1]]))
        self.sut.add_layer(np.array([[1, 0], [0, 1]]))


if __name__ == '__main__':
    unittest.main()
