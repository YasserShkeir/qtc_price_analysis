from operator import index
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='QTC Assessment', layout='wide')

# Headers
st.write("""
# QTC Pricing Analysis
# """)

# qtc_df = pd.read_csv('C:/Users/Lenovo/Desktop/New folder (2)/QTC Formulary.csv', encoding='cp1252')
# gpo_df = pd.read_csv('C:/Users/Lenovo/Desktop/New folder (2)/Academy Report 2.csv', encoding='cp1252')

# # st.write('qtc_df b4 with length: ' + str(len(qtc_df)), qtc_df)
# qtc_df = qtc_df.rename(columns={'Mfr #':'CTLG_NUM'})
# qtc_df['CTLG_NUM'] = qtc_df['CTLG_NUM'].replace(' ', '')

# def remove_sign(x):
#     x = str(x)
#     return x[1:]

# qtc_df['Price'] = qtc_df['Price'].apply(remove_sign)
# qtc_df = qtc_df[qtc_df['Price'] != 'an']
# qtc_df['Price'] = qtc_df['Price'].str.replace(',', '').astype('float')
# qtc_df['Total'] = qtc_df['Total'].apply(remove_sign)
# # st.write('qtc_df after with length: ' + str(len(qtc_df)), qtc_df)

# # st.write('gpo_df b4 with length: ' + str(len(gpo_df)), gpo_df)
# gpo_df = gpo_df.drop(columns=['ITEM_E1_NUM',' Difference ','PARNT_SUPLR_NAME','CNTRCT_START_DT','CNTRCT_END_DT','COST_START_DT','COST_END_DT','Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20'], axis=1)

# gpo_df[' GPO Price '] = gpo_df[' GPO Price '].apply(remove_sign)
# gpo_df[' Price 4/14/22 '] = gpo_df[' Price 4/14/22 '].apply(remove_sign)
# gpo_df[' GPO Price '] = gpo_df[' GPO Price '].apply(remove_sign)
# gpo_df[' Price 4/14/22 '] = gpo_df[' Price 4/14/22 '].apply(remove_sign)

# gpo_df['CTLG_NUM'] = gpo_df['CTLG_NUM'].replace(' ', '')

# gpo_df = gpo_df.rename(columns={' GPO Price ': 'Old_Pricing',' Price 4/14/22 ':'New_Pricing'})

# # st.write('gpo_df after with length: ' + str(len(gpo_df)), gpo_df)

# s1 = pd.merge(qtc_df, gpo_df, how='inner', on=['CTLG_NUM'])
# s1 = s1.drop(columns=[' Old Price ', 'Qty', 'Total'], axis=1)

# s1['Old_Pricing'] = pd.to_numeric(s1['Old_Pricing'])
# s1['New_Pricing'] = pd.to_numeric(s1['New_Pricing'])

# s1['Match'] = (s1['New_Pricing'] == s1['Price'])

# s1['Price_Difference'] = (s1['Old_Pricing']) - (s1['New_Pricing'])
# s1['Price_Difference_%'] = (s1['Price_Difference'] / s1['Old_Pricing'])*100

# s1 = s1.rename(columns={
#     'Item #':'ITEM_NUM_L1',
#     'Description':'DESC_L1',
#     'Manufacturer':'MANUF_L1',
#     'UOM':'UOM_L1',
#     'Price':'PRICE_L1',})

# # st.write('MERGED with length: ' + str(len(s1)), s1)

# # s1.to_csv(r'C:/Users/Lenovo/Desktop/New folder (2)/common.csv', index=False)

final = pd.read_csv('Final.csv')

def remove_sign2(x):
        x = str(x)
        return x[:-1]

final['PERCENT_DIFF'] = pd.to_numeric(final['PERCENT_DIFF'].apply(remove_sign2))
final = final.rename(columns={'CTGRY':'Category'})

final_graph_sum = final.groupby(['Category']).mean()
final_graph_sum = final_graph_sum.rename(columns={'Price_Difference':'Average Price Difference','PERCENT_DIFF':'Average % Saved'})
final_graph_sum = final_graph_sum.drop(columns=['Item # ','PRICE_L1', 'Old_Pricing', 'New_Pricing', 'Match'], axis=1)

st.write(final_graph_sum)

col1, col2 = st.columns(2)

with col1:
    fig = px.bar(final_graph_sum, x=final_graph_sum.index, y='Average Price Difference')
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})

    st.plotly_chart(fig)

with col2:
    fig2 = px.bar(final_graph_sum, x=final_graph_sum.index, y='Average % Saved')
    fig2.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})

    st.plotly_chart(fig2)
