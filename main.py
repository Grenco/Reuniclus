from pathlib import Path

from dependency_injector.wiring import Provide, inject

from engine.services import ConverterService
from container import Container


@inject
def main(converter_service: ConverterService = Provide[Container.converter_service]):
    path = Path(r"./local_resources/dicom_example/")
    converter_service.convert(path)


if __name__ == '__main__':
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    main()
