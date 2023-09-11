import voxelmap as vm

from data.model import VoxelModel
from . import VoxelRendererABC


class VoxelmapVoxelRenderer(VoxelRendererABC):
    def render(self, model: VoxelModel):
        model = vm.Model(model.voxels)
        model.draw()
