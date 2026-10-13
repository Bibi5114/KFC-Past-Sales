import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

st.set_page_config(page_title='KFC Sales Dashboard', layout='wide')

# Page title
st.title('KFC Sales Performance Dashboard')
st.caption(
    'For regional operations managers: monitor sales performance '
    'and identify branches that may need attention.'
)

# Load data
df = pd.read_csv('KFC_Past_Sales_Dataset.csv')

# Put months in calendar order
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df['Month'] = pd.Categorical(df['Month'], categories=months, ordered=True)

# Sidebar filters
st.sidebar.header('Filters')

country = st.sidebar.selectbox(
    'Country',
    ['All'] + sorted(df['Country'].unique().tolist())
)

if country != 'All':
    df = df[df['Country'] == country]

branch = st.sidebar.selectbox(
    'Branch',
    ['All'] + sorted(df['Branch_ID'].unique().tolist())
)

if branch != 'All':
    df = df[df['Branch_ID'] == branch]

year = st.sidebar.selectbox(
    'Year',
    ['All'] + sorted(df['Year'].unique().tolist())
)

if year != 'All':
    df = df[df['Year'] == year]

# Three headline metrics
st.subheader('Sales Overview')

col1, col2, col3 = st.columns(3)

avg_sales = df['Sales'].mean()
avg_customers = df['Customers'].mean()
sales_per_customer = df['Sales'].sum() / df['Customers'].sum()

col1.metric('Avg. Sales per Record', f'{avg_sales:,.0f}')
col2.metric('Avg. Customers per Record', f'{avg_customers:,.0f}')
col3.metric('Sales per Customer', f'{sales_per_customer:,.2f}')

st.caption('Sales currency is not specified in the dataset.')

# Chart 1: monthly sales trend
st.subheader('Monthly Sales Trend')

monthly_sales = df.groupby(
    ['Year', 'Month'], observed=True
)['Sales'].mean().reset_index()

monthly_sales['Date'] = pd.to_datetime(
    monthly_sales['Year'].astype(str) + '-' +
    (monthly_sales['Month'].cat.codes + 1).astype(str) + '-01'
)
monthly_sales = monthly_sales.sort_values('Date')

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(monthly_sales['Date'], monthly_sales['Sales'], marker='o', markersize=3)
ax.set_xlabel('Month')
ax.set_ylabel('Average Sales per Record')
ax.set_title('Monthly Average Sales')
plt.xticks(rotation=30)
plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

# Chart 2: branch comparison
st.subheader('Branch Performance Comparison')

branch_sales = df.groupby('Branch_ID')['Sales'].mean().sort_values()

fig, ax = plt.subplots(figsize=(10, 4))
branch_sales.plot.barh(ax=ax)
ax.set_xlabel('Average Sales per Record')
ax.set_ylabel('Branch')
ax.set_title('Average Sales by Branch')
plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

# Data period and intended refresh
st.caption(
    'Data: 2018-2024 | Kaggle historical snapshot | '
    'Intended refresh in production: Daily | Manager review: Weekly'
)

