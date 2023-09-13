import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# set the title
st.title('Confidence Intervals')

# make the sidebar
st.sidebar.title('Options')

# select the method 
method =  st.sidebar.selectbox(label='Select the Method',
                               options=['Z Procedure','T Procedure'])


## Population Parameters
st.sidebar.header('Population parameters')

# select the population mean
pop_mean = st.sidebar.slider(label='Population Mean',
                            min_value=10,
                            max_value=100,
                            value=50,
                            step=5)

# Select the population std
pop_std = st.sidebar.slider(label='Population Standard Deviation',
                            min_value=1,
                            max_value=30,
                            value=15,
                            step=1)

## Sample Parameters
st.sidebar.header('Sample parameters')

# select the number of samples
num_samples = st.sidebar.slider(label='Number of Samples',
                            min_value=10,
                            max_value=100,
                            value=30,
                            step=5)

# confience level
confidence_level = st.sidebar.slider(label='Confidence Level (%)',
                                        min_value=1,
                                        max_value=100,
                                        step=1,
                                        value=95)

# Select the number of iterations of sampling
num_of_steps = num_samples = st.sidebar.slider(label='Number of Iterations',
                            min_value=100,
                            max_value=500,
                            value=100,
                            step=50)

# button to proceed
btn = st.sidebar.button(label='Apply')

if btn:
    np.random.seed(42)
    
    upper_bounds = []
    lower_bounds = []
    colors = []
    means = []
    area = (((confidence_level + 100) / 100 )/2)

    for i in range(num_of_steps):
        sample = np.random.normal(loc=pop_mean,scale=pop_std,size=num_samples)
        sample_mean = np.mean(sample)
        means.append(sample_mean)
        sample_std = np.std(sample,ddof=1)
        
        if method == 'Z Procedure':
            critical_val = stats.norm.ppf(area)
            standard_error = pop_std / np.sqrt(num_samples)
        elif method =='T Procedure':
            dof = num_samples - 1
            critical_val = stats.t.ppf(area,df=dof)
            standard_error = sample_std / np.sqrt(num_samples)
            
        upper_bound = sample_mean + (critical_val * standard_error)
        lower_bound = sample_mean - (critical_val * standard_error)
            
        upper_bounds.append(upper_bound)
        lower_bounds.append(lower_bound)
        
        if lower_bound <= pop_mean <= upper_bound:
            color = 'blue'
            colors.append(color)
        else:
            color = 'orange' 
            colors.append(color)

    count_orange = colors.count('orange')
    
    # plot the graph
    fig = plt.figure(figsize=(15,7))

    plt.axhline(y=pop_mean,linestyle='--',color='red',label='Population Mean')
    plt.scatter(x=np.arange(1,num_of_steps+1,1),y=means,s=30,edgecolor='grey',linewidth=2,label='Sample Mean')
    plt.vlines(x=np.arange(1,num_of_steps+1,1),ymin=lower_bounds,ymax=upper_bounds,colors=colors,label='Confidence Intervals')
    plt.scatter(x=np.arange(1,num_of_steps+1,1),y=upper_bounds,c=colors,marker='_')
    plt.scatter(x=np.arange(1,num_of_steps+1,1),y=lower_bounds,c=colors,marker='_')
    plt.xlabel('Iterations')
    plt.legend()
    
    # plot on page
    st.pyplot(fig)
    
    # print the statistics on page
    st.write(f'The Population Mean is in {num_of_steps-count_orange} confidence intervals out of {num_of_steps} which is {(((num_of_steps-count_orange)/num_of_steps)*100):.2f}% of times')



