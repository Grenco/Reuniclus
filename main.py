from pathlib import Path
import numpy as np

from engine.dicom import DicomReader
from engine.image import CTImageProcessor
from engine.model import VoxelModelBuilder, VoxelProcessor, VoxelmapVoxelRenderer, VoxelRendererABC


def main():
    path = Path(r"./local_resources/dicom_example/")
    reader = DicomReader()
    image_processor = CTImageProcessor()
    voxel_processor = VoxelProcessor()
    renderer: VoxelRendererABC = VoxelmapVoxelRenderer()
    model_builder = VoxelModelBuilder()

    for dicom in path.iterdir():
        img: np.ndarry = reader.get_image(dicom)
        bone_layer: np.ndarray = image_processor.extract_bone_data(img)
        model_builder.add_layer(bone_layer)

    model = model_builder.build()
    model = voxel_processor.resize(model, 0.1)

    renderer.render(model)


if __name__ == '__main__':
    main()
