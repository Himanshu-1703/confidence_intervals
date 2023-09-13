import streamlit as st
from scipy.stats import chi2
import numpy as np
import matplotlib.pyplot as plt


# title for the page
st.title('Chi Square Distribution')

# set the sidebar menu
st.sidebar.title('Parameters')

# degree of freedom 
dof = st.sidebar.slider(label='Degrees of Freedom',min_value=1,
                  max_value=100,value=5)

# make x
x = np.linspace(chi2.ppf(0.01, df=dof),
                chi2.ppf(0.99, df=dof), 100)

# make the chi square distribution and get the probability density values for x
pdf = chi2.pdf(x,df=dof)

# plot the distribution
fig,ax  = plt.subplots(1,1,figsize=(15,7))
ax.plot(x,pdf,color='red',label=f'Degree of Freedom = {dof}')
ax.set_title('Chi Square Distribution')
plt.legend()

# show the fig
st.pyplot(fig)

