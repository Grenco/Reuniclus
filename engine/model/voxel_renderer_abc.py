from abc import ABCMeta, abstractmethod

from data.model import VoxelModel


class VoxelRendererABC(metaclass=ABCMeta):
    """Create a render of a given voxel model"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'render') and
                callable(subclass.render))

    @abstractmethod
    def render(self, model: VoxelModel):
        """Render the given model"""
        raise NotImplementedError

