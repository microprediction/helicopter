
######################################################################################
#  Code that uses SciML helicopter challenge data in a loop at Microprediction.Org   #
######################################################################################
# Please resist the urge to cheat. No cash prizes attached to this one.

from microprediction import PandasLoop, new_key
import pandas as pd
from pprint import pprint

ORIGIN = 1594147541

# Helicopter challenge data
DF = pd.read_csv('https://raw.githubusercontent.com/SciML/HelicopterSciML.jl/master/data/Lab-Helicopter_Experimental-data.csv')
DF.drop(DF.columns[len(DF.columns) - 1], axis=1, inplace=True)             # Drop last column which has time
DF.columns = ['helicopter_pitch', 'helicopter_yaw', 'helicopter_theta', 'helicopter_psi']  # Nicer names, and ensure there are still only four columns
DF = DF[['helicopter_theta', 'helicopter_psi']]           # Just using the two fast moving ones. Could add the others as auxiliary data

def logtime(res):
    """ Primitive logging function """
    pprint(res)
    print(' ',flush=True)

def helicopter_stream(write_key):
    loop = PandasLoop(write_key=WRITE_KEY, interval=7, origin=1594147541, df=DF, with_copulas=True)
    loop.publish_callback = logtime
    loop.run(minutes=50000)

if __name__=="__main__":
    WRITE_KEY = new_key(difficulty=13)  # Takes many days ... info@microprediction.com if you have a good use case and don't want to wait
    print(WRITE_KEY)
    helicopter_stream(write_key=WRITE_KEY)