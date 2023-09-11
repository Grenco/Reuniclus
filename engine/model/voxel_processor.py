from scipy.ndimage import zoom

from data.model import VoxelModel


class VoxelProcessor:

    def resize(self, model: VoxelModel, scale_factor: float) -> VoxelModel:
        resized = zoom(model.voxels, scale_factor)
        resized[resized > 0.5] = 1  # TODO: Round instead of setting everything to 0/1
        resized[resized < 0.5] = 0

        return VoxelModel(resized)
