import argparse
import pandas as pd
import json
import sys
from progress_bar import InitBar as ib
from datetime import datetime as dt
import datetime
import os

parser=argparse.ArgumentParser()
parser.add_argument("-d","--dataset",
                    help="Path of dataset. default: extra/sample_data.csv",
                    default="extra/data.csv/train.csv")
parser.add_argument("-o","--output",
                    help="Path of output. default: sample/dbscan/DBSCAN_XX_YY.txt",
                    default="./sample/")
parser.add_argument("-s","--start",
                    help="Start interval : H/d/m/y",
                    )
parser.add_argument("-e","--end",
                    help="End interval : H/d/m/y"
                    )

args = parser.parse_args()
print("Parsing datas ...")
datas_brute = pd.read_csv(args.dataset,converters={'TRIP_ID':lambda x: x[-8:]+"_"+x,'TIMESTAMP':lambda x: dt.fromtimestamp(int(x))})
datas = datas_brute.loc[(datas_brute['TIMESTAMP'] >= dt.strptime(args.start,'%H/%d/%m/%Y')) & (datas_brute['TIMESTAMP'] < dt.strptime(args.end,'%H/%d/%m/%Y'))].loc[datas_brute['MISSING_DATA'] == False]
# print(datas.head())
# with pb.ProgressBar(max_value=datas.shape[0]) as bar:
pbar = ib()
print("Datarow building ...")
for i,row in datas.iterrows():
    pbar(i/datas.shape[0])
    g = open("./meta/inputTID.txt","a")
    print(row['TRIP_ID'],file=g)
    g.close()
    cpt = 0
    for i,point in enumerate(json.loads(row['POLYLINE'])):
        if(i%4 == 0):
            key = "DBScan"+(row['TIMESTAMP']+datetime.timedelta(seconds=60*cpt)).strftime('_%H_%M')+".txt"
            cpt += 1
            f = open(args.output+key,"a")
            print(row['TRIP_ID']+" "+str(point[1])+" "+str(point[0]),file=f)
            f.close()
del pbar
