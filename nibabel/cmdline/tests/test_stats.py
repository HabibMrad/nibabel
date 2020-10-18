#!python
# emacs: -*- mode: python-mode; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the NiBabel package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##

from nibabel.testing import test_data
from nibabel.cmdline.stats import main


def test_volume():
    infile = test_data(fname="anatomical.nii")
    args = (f"{infile} --Volume")
    vol_mm3 = main(args.split())
    args = (f"{infile} --Volume --units vox")
    vol_vox = main(args.split())

    assert float(vol_mm3) == 2273328656.0
    assert float(vol_vox) == 284166082.0

