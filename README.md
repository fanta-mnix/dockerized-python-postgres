# Test for Inkitt
This project was created to answers the questions in Inkitt test.

## Requirements
There are no requirements if you simply want to view the results. However, if you want to reproduce the analysis, you will need [Docker](https://docs.docker.com/engine/installation/).
 
## Reviewing
If you are only interested in the results, open the `Analysis.html` file in your browser.

## Reproducing
If you also want to reproduce the results, run the `run.sh` script to build the docker images and launch the containers. Don't hold your breath, as it will take a while for the procedure to complete.

You will be able to start the Jupyter Notebook when something similar to `The Jupyter Notebook is running at http://0.0.0.0:8888` appears in your console. To open the notebook, go to [http://localhost:8888](http://localhost:8888), type the password `inkitt` and select the `analysis.ipynb` file. That's all there is to it!


## Troubleshooting
Make sure that the port `8888` is available on you machine.
