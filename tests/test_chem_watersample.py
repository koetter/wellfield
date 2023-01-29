import pytest
from wellfield.chemistry import watersample

def test_chem_ionbytningsgrad():
    sample = {"na": 23, "cl": 35.5}
    expected = 1
    ws = watersample.Watersample(sample)
    ig = ws.ionbytningsgrad()
    assert ig == expected
