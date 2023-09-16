# Reuniclus (pre-alpha)

*NOTE: This is in very early stages of development and does not function as intended.

## Introduction

Reuniclus (named after the Pokémon which looks like a living x-ray) is a
tool for reading CT and MRI scans from DICOM files and converting them to
3D models.

## Running

To run, just add the desired DICOM directory into the path variable in main.py 
and press run (we're in very early stages here).

## Linting

Lint the project with `Ruff` by installing with:

`pip install ruff`

and then:

`ruff --fix [path/to/project]`

## Updating Dependencies

To automatically update `dependencies.txt`, ensure pipreqs is installed
with:

`pip install pipreqs`

and run:

`pipreqs [path/to/project]`