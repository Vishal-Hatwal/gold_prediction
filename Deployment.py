# -*- coding: utf-8 -*-
"""
Created on 

@author:
"""

import pandas as pd
import streamlit as st
from datetime import date
import matplotlib.pyplot as plt
from plotly import graph_objs as go
from pickle import dump
from pickle import load
from statsmodels.tsa.holtwinters import Holt

st.title('Gold Price Forecasting')

n_days = st.number_input("Enter number of days",0,150)
period = n_days

data = pd.read_csv(r"D:\Data Science\Jupyter Notebook\Time Series Models\Gold_data.csv",date_parser=['date'])
st.subheader('Raw data')
st.write(data.tail())

def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['date'], y=data['price'],name="data"))
	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
    
plot_raw_data()

## Load the model
loaded_model = load(open('D:\Data Science\Jupyter Notebook\Time Series Models\hw_model.sav', 'rb'))
X=period
pred=loaded_model.forecast(X)
st.subheader('Forecasted data')
pred
st.line_chart(pred)