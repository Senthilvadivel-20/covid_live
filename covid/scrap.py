import pandas as pd
import matplotlib.pyplot as plt
import datetime

from  bs4 import BeautifulSoup
import requests

# from PIL import Image
# import io
# import numpy as np

df=pd.read_csv('.\Files\covid.csv')
df=df[['Time', 'Cases', 'Death', 'Recover']]



def covid():
    URL="https://www.worldometers.info/coronavirus/"
    r=requests.get(URL)

    content=r.content

    soup=BeautifulSoup(r.content,"html.parser")

    #cases=soup.findAll('div',attrs={'class':'maincounter-number'})

    Deaths=soup.findAll(attrs={'id':'maincounter-wrap'})

    case=[]
    num=[]
    for i in Deaths:
        case.append(i.h1.text)
        num.append(i.span.text)

    # cvd=[]
    # for i in range(len(case)):
    #     inf=f'{case[i]} :{num[i]} '
    #     cvd.append(inf)

    num1=[]
    for i in range(len(num)):
        li=num[i].split(',')
        temp=''
        for j in li:
            temp=temp+j
        num1.append(temp.strip())

    idx=len(df)
    x=datetime.datetime.now()

    df.loc[idx,'Time']=x
    df.loc[idx,'Cases']=int(num1[0])
    df.loc[idx,'Death']=int(num1[1])
    df.loc[idx,'Recover']=int(num1[2])
    df.to_csv('.\Files\covid.csv')

    return num1

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')

def cases_plot():
    fig=plt.figure(figsize=[10,7])
    x=df['Time'].tail(20).to_list()
    y=df['Cases'].tail(20).to_list()
    plt.plot(x,y,linestyle='--',marker='o',markerfacecolor='red',markersize=12)
    plt.xlabel("Time period")
    plt.ylabel("No of Cases")
    plt.title("Covid Cases plot")
    plt.grid()
    fig.savefig('.\static\coivd\images\\cases')

def death_plot():
    fig1=plt.figure(figsize=[10,7])
    x=df['Time'].tail(20).to_list()
    y=df['Death'].tail(20).to_list()
    plt.plot(x,y,linestyle='--',marker='o',markerfacecolor='red',markersize=10)
    plt.xlabel("Time Period")
    plt.ylabel("Deaths")
    plt.title('Covid Death plot')
    plt.grid()
    fig1.savefig('.\static\coivd\images\\death')

def recovery_plot():
    fig1=plt.figure(figsize=[10,7])
    x=df['Time'].tail(20).to_list()
    y=df['Recover'].tail(20).to_list()
    plt.plot(x,y,linestyle='--',marker='o',markerfacecolor='red',markersize=10)
    plt.xlabel("Time Period")
    plt.ylabel("Recovery")
    plt.title('Covid Recover plot')
    plt.grid()
    fig1.savefig('.\static\coivd\images\\recovery')


cases_plot()
death_plot()
recovery_plot()

