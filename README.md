# Test Mammograms

The purpose of this repo is to provide a handful of mammograms for unit testing, not for executing a performance test of statistical significance.

## Use

```python
from mammograms import gen_cases

for case in gen_cases():
    for view, dicom_path in case.items():
        # `view` may be "rcc", "lmlo", etc.
        # `dicom_path` will be Path(.../FILENAME.dcm)
```

## Cases
This repo includes `sfm-benign-0` and `sfm-malign-0` which are taken from DDSM.

DDSM was originally provided by the University of South Florida and can be downloaded [here](http://www.eng.usf.edu/cvprg/mammography/database.html), and a curated version known as CBIS-DDSM can be downloaded [here](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=22516629). Please also take a look at the license for CBIS-DDSM [here](https://creativecommons.org/licenses/by/3.0/).

The DICOMs provided in this repo were taken from CBIS-DDSM and compressed with [RLE](https://en.wikipedia.org/wiki/Run-length_encoding).