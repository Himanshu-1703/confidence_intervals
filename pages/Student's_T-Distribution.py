import streamlit as st
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# title
st.title("Student's T-Distribution")

# make the t distribution plot for a particular degree of freedom
st.sidebar.title('Menu')

dof = st.sidebar.slider(label='Degrees of Freedom',
                        min_value=1,max_value=200,
                        step=1,value=10)

# make X
x = np.linspace(-5,5,1000)

# make the two distributions
normal = stats.norm.pdf(x)

t_dist = stats.t.pdf(x,df=dof)

# plot the two distribution

fig = plt.figure(figsize=(15,10))

sns.lineplot(normal,label='Normal Distribution')
sns.lineplot(t_dist,label=f'T Distribution with df={dof}')
plt.title('Normal vs T-Distribution')
plt.legend()


st.pyplot(fig=fig)