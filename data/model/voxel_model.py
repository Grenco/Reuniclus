from dataclasses import dataclass
import numpy as np


@dataclass
class VoxelModel:
    voxels: np.ndarray[int] | np.ndarray[bool]
