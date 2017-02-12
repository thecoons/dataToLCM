# Taxi trajectory data treatement for LCM.

## Dataset

You can download dataset and documentation about it, [here](https://www.kaggle.com/c/pkdd-15-predict-taxi-service-trajectory-i/data)

## Instructions
0. You have to pull the project and create `/meta/`,`/sample/`,`/output/`
1. Install `pip`, a python package manager. [here](https://pip.pypa.io/en/stable/)
2. Use `pip install -r requirements.txt` commande for install dependency package.
3. Firstly, we have to build from data, the datarow indeed for DBSCAN. Use `format_to_dbscan.py` for generate temporal sample and id travel list, use the parameter `--help` for get man. (ex: `python scripts/format_to_dbscan.py -s 18/01/10/2013 -e 21/01/10/2013`)
4. Then, you have to use `dbscan.jar` wich will use the sample et id travel for create DBScan output in `./output/`. Use `java -jar dbscan.jar `
