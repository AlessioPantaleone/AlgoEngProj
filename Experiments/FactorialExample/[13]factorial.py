#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:03:49 2020

@author: anonym
"""

#factorial design
import csv
import matplotlib.pyplot as plt

import time
import pandas as pd
import seaborn as sns

def algorithm(m,n,r):
  
    # for j in range():
    time.sleep(int(((m+3)*4*r)/(1+n))/500)

        
        
if __name__ == "__main__":

    m=[10,20]
    n=[5,10]
    r=[20,40]
    
    
    with open('../../../../Desktop/D', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["F1", "F2", "F3","hF1", "hF2", "hF3", "Time"])
        for mm in m:
            for nn in n:
                for rr in r: #all combinations
                    cpu=time.process_time();

                    algorithm(mm,nn,rr);
                    
                    elapsed=time.process_time()-cpu;
                    writer.writerow([mm, nn, rr,"High" if mm==m[1] else "Low","High" if  nn==n[1]  else "Low","High" if  rr==r[1] else "Low",elapsed])
                   
    df = pd.read_csv('../../../../Desktop/D')
    print(df)    

    sns.set(style="ticks", color_codes=True, font_scale=3)
    plt.rcParams['figure.figsize'] = (12.0, 7.0)
    plt.rc('text', usetex=True)
    # plt.rc('text.latex', unicode=True)
    # q = 'algo ==  "genetic"'
    # selected_df=df.query(q)
    ax = sns.lineplot(x="F3", y="Time", hue="hF2",style="hF1",data=df,linewidth=5)
    # ax = sns.lineplot(x="F2", y="Time", hue="hF3",style="hF1",data=df,linewidth=5)

    # ax = sns.lineplot(x="F1", y="Time", hue="hF3",style="hF2",data=df,linewidth=5)

    # plt.legend(loc=0,fontsize='24',handlelength=1,frameon=False)
    # ax.set(xlabel='\\textsc{eras}', ylabel='\\textsc{time}')
    # ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
    # ax.grid();
    # plt.xlim(0, None)
    sns.despine()
    plt.show()
    # plt.savefig(outpath+instance+"_"+op+"_eras_time.pdf", bbox_inches='tight');
