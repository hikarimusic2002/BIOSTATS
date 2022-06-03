import matplotlib.pyplot as plt
import seaborn as sns

def process(data):
    for col in data:
        try: 
            data[col] = data[col].astype('float64')
        except:
            pass  

def histogram(data, x, band, color=None):

    sns.set_theme()
    process(data)

    fig, ax = plt.subplots()
    sns.histplot(data=data, x=x, bins=band, hue=color, ax=ax)
        
    return fig


def density_plot(data, x, smooth, color=None):

    sns.set_theme()
    process(data)

    fig, ax = plt.subplots()
    sns.kdeplot(data= data, x=x, bw_adjust=smooth, hue=color, ax=ax)
    
    return fig

def cumulative_plot(data, x, color=None):

    sns.set_theme()
    process(data)

    fig, ax = plt.subplots()
    sns.ecdfplot(data= data, x=x, hue=color, ax=ax)
    
    return fig

def histogram_2D(data, x, y, color=None):

    sns.set_theme()
    process(data)

    fig, ax = plt.subplots()
    sns.histplot(data=data, x=x, y=y, hue=color, ax=ax)
        
    return fig

def density_plot_2D(data, x, y, color=None):

    sns.set_theme()
    process(data)

    fig, ax = plt.subplots()
    sns.kdeplot(data=data, x=x, y=y, hue=color, ax=ax)
        
    return fig