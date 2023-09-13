import streamlit as st
from scipy.stats import f
import numpy as np
import matplotlib.pyplot as plt


# title for the page
st.title('F Distribution')

# set the sidebar menu
st.sidebar.title('Parameters')

# degree of freedom 
dof1 = st.sidebar.slider(label='Degrees of Freedom [1]',min_value=1,
                  max_value=100,value=5)
dof2 = st.sidebar.slider(label='Degrees of Freedom [2]',min_value=1,
                  max_value=100,value=5)

# make x
x = np.linspace(f.ppf(0.01, dfn=dof1, dfd=dof2),
                f.ppf(0.99, dfn=dof1, dfd=dof2), 100)


# make the chi square distribution and get the probability density values for x
pdf = f.pdf(x,dfn=dof1,dfd=dof2)

# plot the distribution
fig,ax  = plt.subplots(1,1,figsize=(15,7))
ax.plot(x,pdf,color='red',label=f'Degree of Freedom = [{dof1} and {dof2}]')
ax.set_title('F Distribution')
plt.legend()


# show the fig
st.pyplot(fig)

