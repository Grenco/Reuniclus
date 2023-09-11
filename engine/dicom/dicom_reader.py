import pydicom as dicom

import numpy as np
from pathlib import Path


class DicomReader:
    """Used for extracting information from a given dicom file"""
    def __init__(self):
        self.SUPPORTED_FILE_TYPES = [".dcm"]

    def get_image(self, path: Path) -> np.ndarray:
        """Extracts the image from the given file path"""
        dicom_file = self.__read(path)
        img = dicom_file.pixel_array
        return img

    def __read(self, path: Path) -> dicom.FileDataset:
        """Read a dicom file at a given path"""
        ext: str = path.suffix
        if ext not in self.SUPPORTED_FILE_TYPES:
            raise ValueError(f"File extension \"{ext}\" is not supported. "
                             f"Supported file types: {self.SUPPORTED_FILE_TYPES}. "
                             f"Path: {path}")
        return dicom.dcmread(path)
