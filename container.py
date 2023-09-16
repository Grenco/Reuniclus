
from dependency_injector import containers, providers

from engine import dicom, image, model, services


class Container(containers.DeclarativeContainer):
    """Dependency container for implementing DI"""

    # Services
    dicom_reader = providers.Singleton(dicom.DicomReader)

    image_processor = providers.Singleton(image.CTImageProcessor)

    voxel_builder = providers.Factory(model.VoxelModelBuilder)
    voxel_processor = providers.Singleton(model.VoxelProcessor)
    voxel_renderer = providers.Singleton(model.VoxelmapVoxelRenderer)

    converter_service = providers.Singleton(services.ConverterService,
                                            reader= dicom_reader,
                                            image_processor= image_processor,
                                            voxel_processor= voxel_processor,
                                            renderer= voxel_renderer,
                                            model_builder= voxel_builder)
    # TODO: Add logging
