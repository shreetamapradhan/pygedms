import pygedm
import numpy as np
from astropy.coordinates import Angle
from astropy.units import Unit, Quantity
import astropy.units as u
import pytest

def test_raises():
    """ Test that IGM mode FAILS as expected """
    with pytest.raises(RuntimeError):
         pygedm.dm_to_dist(100, 10, 100, method='ymw1066')
    with pytest.raises(RuntimeError):
         pygedm.dist_to_dm(100, 10, 100, method='ne2020')
    with pytest.raises(RuntimeError):
         pygedm.calculate_electron_density_xyz(100, 10, 100, method='tc93')
    with pytest.raises(RuntimeError):
         pygedm.calculate_electron_density_lbr(100, 10, 100, method='ymwPaleolithic')

if __name__ == "__main__":
    test_raises()
