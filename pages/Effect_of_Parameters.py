import streamlit as st
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


# set the title for the page
st.title('Effects of Different Parameters on Confidence Intervals')

# set the sidebar title
st.sidebar.title('Parameters')

## make the options

# confidence level
confidence_level = st.sidebar.slider(label='Confidence Level %',
                  min_value=5,max_value=100,
                  value=95,step=5)

# population standard deviation
pop_std = st.sidebar.slider(label='Population Standard Deviation',
                  min_value=1,max_value=30,
                  value=15,step=1)

# sample size
n = st.sidebar.number_input(label='Sample Size',
                        min_value=50,max_value=1000,
                        value=100)

# radio button to display graphs
toggle = st.sidebar.radio(label='Show Additional Graphs',
                          options=['No','Yes'],index=0)

# apply button
btn = st.sidebar.button(label='Apply')

if btn:
    # create a sample
    sample = np.random.normal(loc=50,scale=pop_std,size=int(n))
    
    # find the sample mean
    sample_mean = np.mean(sample)
    
    # find the crtical value based on the confidence level
    critical_value = norm.ppf(((confidence_level + 100)/100)/2)
    
    # find the standard error
    standard_error = pop_std / np.sqrt(n)
    
    # find the margin of error
    margin_of_error = critical_value * standard_error
    
    # confidence intervals
    upper_bound = sample_mean + margin_of_error
    lower_bound = sample_mean - margin_of_error
    
    # display the results
    st.write(f'Critical Value = {critical_value:.2f}')
    st.write(f'Sample Mean = {sample_mean:.2f}')
    st.write(f'Confidence Interval [{lower_bound:.3f} - {upper_bound:.3f}]')
    st.write(f'Margin of Error = {margin_of_error:.2f}')
    
    # plot the graph
    
    fig,ax = plt.subplots(1,1,figsize=(10,7))
    
    ax.axhline(y=sample_mean,linestyle='solid',color='k',label='Sample Mean',linewidth=3)
    ax.bar(x=['Lower Bound','Upper Bound'],
           height=[lower_bound,upper_bound],
           alpha=0.6,color=['blue','green'])
    ax.set_title('Effect of Different Parameters on Confidence Intervals')
    ax.plot(['Lower Bound','Upper Bound'],[lower_bound,upper_bound],linewidth=4,
            color='red',linestyle='--',label='Distance of Error')
    plt.legend()
    # show the graph
    st.pyplot(fig)

    st.markdown('----')
    
# plot the other graphs
    if toggle == 'Yes':
        st.subheader('Effect of Different parameters on Margin Of Error')
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.image('margin of error vs confidence level.png')
        with col2:
            st.image('margin of error vs sample size.png')
        with col3:
            st.image('margin of error vs population standard deviation.png')
               
            
        