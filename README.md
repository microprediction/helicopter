# helicopter

## Fork me

Tiny repo that creates a helicopter data stream at Microprediction.Org

It also contains some snippets of code showing how to:
 
 - Retrive and interpret bivariate stream data at Microprediction.Org
 - Fit a copula function
 - Make a prediction submission 

See [article](https://www.linkedin.com/pulse/helicopulas-peter-cotton-phd/) for more explanation. 


![https://www.linkedin.com/pulse/helicopulas-peter-cotton-phd/](https://i.imgur.com/vuWAeLg.png)


## Background information 

Yes this is a Python package but it was inspired by the Helicopter Julia Challenge created by Chris Rackausckas of the SciML group at MIT. In that challenge
contestants are provided incomplete data from a helicopter and asked to infer the latent dynamics. 


- Video of the helicopter https://www.youtube.com/watch?v=2g1-sDZ3BVw
- Home page of challenge https://github.com/SciML/HelicopterSciML.jl
- Chris will be teaching how to do automated discovery of missing physical equations from a first principle model at at workshop on July 26th, 2020. Sign up for JuliaCon at https://juliacon.org/2020/

The goal of the Julia challenge is to utilize automated tools to discover a physcially-explainable model that accurately predicts the dynamics of the system.

## A quick peek at the helicopter data

    import pandas as pd 
    data = pd.read_csv('https://raw.githubusercontent.com/SciML/HelicopterSciML.jl/master/data/Lab-Helicopter_Experimental-data.csv').plot()
    
## Fitting implied helicopter data 

See [helicopter/exploratory/helicopula.py](https://github.com/microprediction/helicopter/blob/master/exploratory/helicopula.py) 

## If you prefer notebooks: 

   https://github.com/microprediction/PDCI/blob/master/helicopula.ipynb
   

   

