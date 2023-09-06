import streamlit as st
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

# title
st.title("Student's T-Distribution")

# make the t distribution plot for a particular degree of freedom
st.sidebar.title('Menu')

dof = st.sidebar.slider(label='Degrees of Freedom',
                        min_value=5,max_value=200,
                        step=1)

# make the two distributions
normal = stats.norm.rvs(loc=0,scale=1,size=5000,random_state=1)

t_dist = stats.t.rvs(loc=0,scale=1,size=5000,random_state=1,df=dof)

# plot the two distribution

fig = plt.figure(figsize=(15,10))

sns.kdeplot(normal,label='Normal Distribution')
sns.kdeplot(t_dist,label=f'T Distribution with df={dof}')
plt.legend()
plt.xlim((-3,3))

st.pyplot(fig=fig)