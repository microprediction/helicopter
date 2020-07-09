
from microprediction import MicroReader
mr = MicroReader()

def test_wind():
    """ Retrieve bivariate wind data lagged values """
    HELISTREAM = 'z2~seattle_wind_direction~seattle_wind_speed~70.json'
    lagged_values = mr.get_lagged_values(name=HELISTREAM)
    assert len(lagged_values)>10