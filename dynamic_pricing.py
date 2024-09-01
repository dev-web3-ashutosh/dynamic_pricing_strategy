import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data=pd.read_csv('dynamic_pricing.csv')
# print(data.head())

# describe data
# print(data.describe())

fig=px.scatter(data, x='Expected_Ride_Duration', y='Historical_Cost_of_Ride', title='Expected Ride Duration vs. Historical Cost', trendline='ols', trendline_color_override='red')
fig.show()
