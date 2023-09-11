from pathlib import Path
import numpy as np

from engine.dicom import DicomReader
from engine.image import CTImageProcessor
from engine.model import VoxelModelBuilder, VoxelProcessor, VoxelRendererABC


class ConverterService:
    """Converts dicom files into a mesh"""
    def __init__(self,
                 reader: DicomReader,
                 image_processor: CTImageProcessor,
                 voxel_processor: VoxelProcessor,
                 renderer: VoxelRendererABC,
                 model_builder: VoxelModelBuilder):
        self._reader = reader
        self._image_processor = image_processor
        self._voxel_processor = voxel_processor
        self._renderer = renderer
        self._model_builder = model_builder

    def convert(self, path: Path):

        self._model_builder.clear()
        for dicom in path.iterdir():
            img: np.ndarry = self._reader.get_image(dicom)
            bone_layer: np.ndarray = self._image_processor.extract_bone_data(img)
            self._model_builder.add_layer(bone_layer)

        model = self._model_builder.build()
        model = self._voxel_processor.resize(model, 0.1)

        self._renderer.render(model)
