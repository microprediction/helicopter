
# A collection of mostly standalone functions illustrating copula functionality at dev.microprediction.org

# See also https://github.com/microprediction/PDCI/blob/master/helicopula.ipynb
# See article at https://www.linkedin.com/pulse/helicopulas-peter-cotton-phd/

import pandas as pd
import matplotlib.pyplot as plt
from microprediction import MicroReader, MicroWriter, new_key
from copulas.multivariate import GaussianMultivariate
import numpy as np
from pprint import  pprint

mr = MicroReader()

def get_wind_z2():
    """ Retrieve bivariate wind data lagged values """
    HELISTREAM = 'z2~seattle_wind_direction~seattle_wind_speed~70.json'
    lagged_values = mr.get_lagged_values(name=HELISTREAM)
    return lagged_values

def plot_helicopter_data():
    """ Plot SciML helicopter challenge data """
    pd.read_csv('https://raw.githubusercontent.com/SciML/HelicopterSciML.jl/master/data/Lab-Helicopter_Experimental-data.csv').plot()


def plot_helicopter_lags():
    """ Plot a subset of the SciML helicopter challenge data .. psi only """
    mr = MicroReader()
    xs = mr.get_lagged_values('helicopter_psi.json')
    plt.plot(xs)


def get_stream_lagged_values(name=None):
    """ Get bivariate data from helicopter that is disguised as univariate data """
    name = name or 'z2~helicopter_psi~helicopter_theta~70.json'
    return mr.get_lagged_values(name=name)

def interpret_z2(lagged_values=None,do_plot=False):
    """ Illustrates how z2 stream values can be interpreted
    :param lagged_values:
    :param do_plot:
    :return:
    """
    if lagged_values is None:
        lagged_values = get_stream_lagged_values()
    points = [ mr.from_zcurve( zvalue=z, dim=2) for z in lagged_values ]
    zpitch,zyaw = zip(*points)
    if do_plot:
        plt.scatter(zpitch,zyaw)
        plt.xlabel('Pitch - transformed')
        plt.ylabel('Yaw - transformed')
    return zpitch, zyaw

def fit_copula_to_z2_data(name=None, do_plot=False):
    """ Example of fitting a copula to z2 stream data

    :param   name:  stream name
    :return: copula  obj
    """
    name = name or 'z2~helicopter_psi~helicopter_theta~70.json'
    assert 'z2~' in name, "Expecting a bivariate stream"

    lagged_values = get_stream_lagged_values(name=name)
    normalized_points = [mr.norminv(mr.from_zcurve(zvalue=z, dim=2)) for z in lagged_values]
    npitch, nyaw = zip(*normalized_points)

    copula = GaussianMultivariate()
    X = np.array([npitch, nyaw]).transpose()
    copula.fit(X)

    synthetic_points = copula.sample(len(X))
    spitch = synthetic_points[0]
    syaw = synthetic_points[1]
    if do_plot:
        plt.scatter(spitch, syaw)
        plt.xlabel('Simulated Pitch - normalized')
        plt.ylabel('Simulated Yaw - normalized')
        plt.show()
    return copula


def create_a_write_key():
    """ Takes a while """
    print(new_key(difficulty=10))

def project(p,q):
    """ Convert normally distributed prediction pair into scalar """
    return mr.to_zcurve([mr.normcdf(p),mr.normcdf(q)] )

def example_z2_prediction(write_key, name=None):
    """
        :param write_key str  See above for creating a write_key
        :param name      str  Name of a bivariate stream, such as  'z2~helicopter_psi~helicopter_theta~70.json'
    """
    if name is None:
        name = 'z2~helicopter_psi~helicopter_theta~70.json'
    copula = fit_copula_to_z2_data()
    submitted_points = copula.sample(mr.num_predictions)
    qpitch = submitted_points[0]
    qyaw   = submitted_points[1]
    values = sorted([project(p, q) for p, q in zip(qpitch, qyaw)])

    # Now submit them
    mw = MicroWriter(write_key=write_key)
    print(mw.animal + ' is submitting ')
    horizon = 70
    reply = mw.submit(name=name, values=values, delay=horizon)
    pprint(reply)


if __name__=="__main__":
    fit_copula_to_z2_data(do_plot=True)