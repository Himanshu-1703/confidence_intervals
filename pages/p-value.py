import streamlit as st
import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# set the title
st.title('P value Demonstration')

# set the sidebar
st.sidebar.title('Options')

# value of prob
prob = st.sidebar.slider(label='Select the number of heads',
                         min_value=50,max_value=80,
                         value=50,step=1)


def decision(p_value,alpha=0.05):
    if p_value <= alpha:
        return 'Reject the Null hypothesis, The coin is unfair'
    else:
        return 'Fail to reject the Null Hypothesis, The coin is fair'

# make a binomial distribution

k = 100
n = 10000
p = 0.5

# set the random seed
np.random.seed(42)

sample = np.random.binomial(n=k,p=p,size=n)

# apply button
btn = st.sidebar.button(label='Apply')

    # make dataframe
if btn:

    hue = np.where(sample>=prob,1,0)

    df = pd.DataFrame({'sample':sample,'hue':hue})

    # do the calculations
    distribution = stats.binom(n=k,p=p)
    probability = distribution.pmf(prob)
    
    p_val = distribution.sf(prob)
    

    # display the results

    st.write(f'Probability of getting exactly {prob} out of 100 is {probability:.2f}')
    st.write(f'P value is {p_val:.2f}')
    st.write(decision(p_val))
    
    st.subheader('Binomial Distribution')
    
    # plot the graph
    # Set the color palette
    colors = ['blue','red']
    
    fig,ax = plt.subplots(1,1,figsize=(15,10))

    sns.histplot(data=df,x='sample',bins=40,hue='hue',
                alpha=1,palette=colors,ax=ax,
                stat='probability',legend=False)
    
    st.pyplot(fig)