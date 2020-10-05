import plotly.figure_factory as ff
import statistics
import random
import csv
import plotly.graph_objects as go
import pandas as pd
df=pd.read_csv("newdata.csv")
data=df["average"].tolist()
population_mean=statistics.mean(data)
population_stdev=statistics.stdev(data)
print(population_mean)
print(population_stdev)
#fig=ff.create_distplot([data],["average"],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
#fig.show()
def randomSetOfMean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    st_dev=statistics.stdev(dataset)
    print(mean)
    print(st_dev)
    return mean
def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["average"],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        setOfMeans=randomSetOfMean(100)
        mean_list.append(setOfMeans)
    show_fig(mean_list)

setup()
