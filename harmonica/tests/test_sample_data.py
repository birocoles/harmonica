"""
Test the sample data loading functions.
"""
import numpy.testing as npt

from ..datasets.sample_data import (
    fetch_gravity_earth,
    fetch_topography_earth,
    fetch_rio_magnetic,
)


def test_gravity_earth():
    "Sanity checks for the loaded grid"
    grid = fetch_gravity_earth()
    assert grid.gravity.shape == (361, 721)
    npt.assert_allclose(grid.gravity.max(), 9.8018358e05)
    npt.assert_allclose(grid.gravity.min(), 9.7476403e05)
    assert grid.height_over_ell.shape == (361, 721)
    npt.assert_allclose(grid.height_over_ell, 10000)


def test_topography_earth():
    "Sanity checks for the loaded grid"
    grid = fetch_topography_earth()
    assert grid.topography.shape == (361, 721)
    npt.assert_allclose(grid.topography.max(), 5622)
    npt.assert_allclose(grid.topography.min(), -8397)


def test_rio_magnetic():
    "Sanity checks for the loaded dataset"
    data = fetch_rio_magnetic()
    assert data.shape == (81796, 6)
    npt.assert_allclose(data.longitude.min(), -43.199966)
    npt.assert_allclose(data.longitude.max(), -41.950012)
    npt.assert_allclose(data.latitude.min(), -22.569992)
    npt.assert_allclose(data.latitude.max(), -22.050003)
    npt.assert_allclose(data.total_field_anomaly_nt.min(), -636.180000)
    npt.assert_allclose(data.total_field_anomaly_nt.max(), 875.120000)
    npt.assert_allclose(data.altitude_m.min(), 62.180000)
    npt.assert_allclose(data.altitude_m.max(), 300.000000)
    npt.assert_allclose(data.line_number.min(), 1680)
    npt.assert_allclose(data.line_number.max(), 9600)
    assert set(data.line_type.unique()) == {"TIE", "LINE"}