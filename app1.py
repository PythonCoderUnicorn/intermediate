# streamlit app 1

import streamlit as st 
import datetime
import pandas as pd



# age = st.slider("How old are you?", 0, 100000, 1000)
# st.write(f"### Cash & cash equivalent $ {age:,.2f}")

# --- slider range
# values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
# st.write("Values:", values)

# yr_select = st.selectbox(
#     "Select the Year for balance sheet",
#     ("2025", "2024", "2023","2022","2021","2020","2019","2018"),
# )

# st.write("You selected:", yr_select)

# st.write(f"### Total Current Assets ({k[1]})  $ {s1:,.2f}")
# st.write(f"### Total Current Assets ({k[2]})  $ {s2:,.2f}")

# st.metric(label="Total Current Assets", value=f"${s1:,.2f}")
# st.metric(label="Total Current Assets", value=f"${s2:,.2f}")


# with col3:
#     st.header(f"{k[2]}")
#     st.metric(label="Total Non-Current Assets", value=f"${noncurr_assets_2 :,.2f}",delta_color="normal")

# with col4:
#     st.header(f"{k[2]}")
#     st.metric(label="Total Current Assets", value=f"${curr_assets_2:,.2f}",delta_color="normal")

# st.write(f"### Total Current Assets ................. $ {total_current_assets:,.2f}")

# st.write(f"### Total Non-Current Assets ......... $ {total_noncurrent_assets:,.2f}")

# st.write(f"### Total Assets ............................. $ {total_assets:,.2f}")

# message = st.text_area("Message", value="Lorem ipsum.\nStreamlit is cool.")

# if st.button("Prepare download"):
#     st.download_button(
#         label="Download text",
#         data=message,
#         file_name="message.txt",
#         on_click="ignore",
#         type="primary",
#         icon=":material/download:",
#     )


# =========== current assets
# st.subheader("Current Assets")

# cash_cash_equiv = st.number_input("Enter a value for cash and cash equivalents", value=0, placeholder="Type a number...")

# trade = st.number_input("Enter a value for trade & other receivables", value=0, placeholder="Type a number...")

# inventories = st.number_input("Enter a value for inventories", value=0, placeholder="Type a number...")

# total_current_assets = cash_cash_equiv + trade + inventories 


# ======== non-current assets
# st.subheader("Non-Current Assets")

# available_for_sale_investment = st.number_input("Enter a value for svailable for sale investments", value=0, placeholder="Type a number..")
# investments_in_associates = st.number_input("Enter a value for svailable investments in associates", value=0, placeholder="Type a number..")
# grapevines = st.number_input("Enter a value for grapevines", value=0, placeholder="Type a number..")
# property_plant_equip = st.number_input("Enter a value for Property, Plant and Equipment - net", value=0, placeholder="Type a number..")
# intangible_assets = st.number_input("Enter a value for intangible assets", value=0, placeholder="Type a number..")
# deferred_income_tax = st.number_input("Enter a value for deferred income tax", value=0, placeholder="Type a number..")
# assets_held_for_sale = st.number_input("Enter a value for assets held for sale (discontinued operations)", value=0, placeholder="Type a number...")

# total_noncurrent_assets = available_for_sale_investment + investments_in_associates \
#     + grapevines + property_plant_equip \
#     + intangible_assets + deferred_income_tax + assets_held_for_sale




# total_assets = total_current_assets + total_noncurrent_assets


# options = st.multiselect(
#     "What are your favorite colors",
#     ["Green", "Yellow", "Red", "Blue","Purple"],
#     ["Yellow", "Purple"],
# )

# st.write("You selected:", options)


















st.header("Intermediate Accounting App")

st.subheader("Balance Sheet")
st.write("Using Python for calculating financial position to generate a balance sheet.") 


company_name = st.text_input("Enter the company name","Placeholder")


d = st.date_input("Enter date for balance sheet", datetime.date(2020, 12,31))
# st.write(f"Balance Sheet date: {d}")











st.divider()
# -----
st.write(f"### {company_name}\n### Balance Sheet {d}")

st.markdown("*Each cell can be modified, the values are not static. Double-Click on a dataframe cell and enter a new value.*")




df1 = pd.DataFrame(
    [
       {"Current Assets": "cash & cash equivalents", "2021": 1215, "2020": 11405},
       {"Current Assets": "trade & other receivables", "2021": 15820, "2020": 13600},
       {"Current Assets": "inventories", "2021": 8180, "2020": 7230},
   ]
)
edited_df = st.data_editor(df1)

curr_assets_1 = df1['2021'].sum()
curr_assets_2 = df1['2020'].sum()
k = df1.keys()






df2 = pd.DataFrame(
    [
       {"Non-Current Assets": "available for sale investment", "2021": 3620, "2020": 3200},
       {"Non-Current Assets": "investment in associates", "2021": 5500, "2020": 5e3},
       {"Non-Current Assets": "grapevines", "2021": 22e3, "2020": 20e3 },
       {"Non-Current Assets": "property plant & equipment - net", "2021": 34e3, "2020": 30500 },
       {"Non-Current Assets": "intangible assets", "2021": 1, "2020": 1 },
       {"Non-Current Assets": "deferred income tax", "2021": 27, "2020": 24 },
       {"Non-Current Assets": "assets held for sale (discontinued operations)", "2021": 0, "2020": 2630 },
   ]
)
edited_df = st.data_editor(df2)

noncurr_assets_1 = df2['2021'].sum()
noncurr_assets_2 = df2['2020'].sum()
k = df2.keys()



total_assets_1 = sum( [curr_assets_1 , noncurr_assets_1 ,   ])
total_assets_2 = sum( [curr_assets_2 ,  noncurr_assets_2  ])


df3 = pd.DataFrame(
    [
       {"Current Liabilities": "trade & other payables", "2021": 10700, "2020": 9450 },
       {"Current Liabilities": "provision for warranties", "2021": 90, "2020": 80 },
       {"Current Liabilities": "taxes payable", "2021": 280, "2020": 250 },
       {"Current Liabilities": "current portion of finance lease obligation", "2021": 370, "2020": 340 },
       {"Current Liabilities": "current portion of long term debt", "2021": 10e3, "2020": 8e3 },
    #    {"Current Liabilities": "deferred income tax", "2021": 27, "2020": 24 },
    #    {"Current Liabilities": "assets held for sale (discontinued operations)", "2021": 0, "2020": 2630 },
   ]
)
edited_df = st.data_editor(df3)

curr_liab_1 = df3['2021'].sum()
curr_liab_2 = df3['2020'].sum()
k = df3.keys()



df4 = pd.DataFrame(
    [
       {"Non-Current Liabilities": "finance lease obligation", "2021": 2480, "2020": 2850 },
       {"Non-Current Liabilities": "long term debt", "2021": 20e3, "2020": 30e3 },
       {"Non-Current Liabilities": "deferred income tax", "2021": 3720, "2020": 3190 },
       {"Non-Current Liabilities": "employee pension benefits", "2021": 1470, "2020": 1350 },
       {"Non-Current Liabilities": "liabilities of discontinued operations", "2021": 0, "2020": 1440 },
   ]
)
edited_df = st.data_editor(df4)

non_curr_liab_1 = df4['2021'].sum()
non_curr_liab_2 = df4['2020'].sum()
k = df4.keys()

total_liab_1 = curr_liab_1 + non_curr_liab_1
total_liab_2 = curr_liab_2 + non_curr_liab_2




df5 = pd.DataFrame(
    [
       {"Equity": "share capital (1M issued & outstanding)", "2021": 15e3, "2020": 13e3 },
       {"Equity": "reserves", "2021": 660, "2020": 240 },
       {"Equity": "retained earnings", "2021": 25593, "2020": 23400 },
   ]
)
edited_df = st.data_editor(df5)

equity_1 = df5['2021'].sum()
equity_2 = df5['2020'].sum()
k = df5.keys() 


TOTAL_1 = total_liab_1 + equity_1
TOTAL_2 = total_liab_2 + equity_2



















# ================================== summary

col1,col2,col3, col4 = st.columns(4)

with col1:

    de_curr_assets = str(curr_assets_2- curr_assets_1)
    de_liab = str(curr_liab_1 - curr_liab_2 )
    de_equity = str(equity_1 - equity_2)
    st.header(f"{k[1]}")

    st.metric(label=f"Total Current Assets ", value=f"${curr_assets_1:,.2f}", delta=de_curr_assets)
    st.metric(label=f"Total Current Liabilities ", value=f"${curr_liab_1 :,.2f}", delta=de_liab )
    st.metric(label=f"Total Equity ", value=f"${equity_1 :,.2f}", delta=de_equity )


with col2:
    de_non_curr = str(noncurr_assets_1 - noncurr_assets_2 )
    de_non_liab = str(non_curr_liab_1 - non_curr_liab_2)
    st.header(f" ")
    st.metric(label=f"Total Non-Current Assets ", value=f"${noncurr_assets_1 :,.2f}", delta= de_non_curr )
    st.metric(label=f"Total Non-Current Liabilities ", value=f"${non_curr_liab_1:,.2f}", delta=de_non_liab)



with col3:
    de = str(total_assets_2 - total_assets_1 )
    de_liab_total = str(total_liab_1 - total_liab_2 )
    # st.header(f"{k[1]}")
    st.header(f" ")
    st.metric(label=f"Total Assets ", value=f"${total_assets_1 :,.2f}", delta=de)
    st.metric(label=f"Total Liabilities ", value=f"${total_liab_1 :,.2f}", delta= de_liab_total)



st.header("Total liabilities & equity")
    
de_total = str(TOTAL_1 - TOTAL_2)
# st.write(TOTAL_1)
st.metric(label="Total liabilities and equity", value=f"$ {TOTAL_1:,.2f}", delta= de_total)







def convert_for_download(df):
    return df.to_csv().encode("utf-8")

# csv = convert_for_download(df= df1)

# st.download_button(
#     label="Download CSV",
#     data= csv,
#     file_name="accounting_data.csv",
#     mime="text/csv",
#     icon=":material/download:"
# )






st.divider()

col10,col11,col12 = st.columns(3)

with col10:

    agree = st.checkbox("Download Current Assets")

    if agree:
        csv1 = convert_for_download(df= df1)
        st.write("Great!")
        st.download_button(
        label="Download CSV",
        data= csv1,
        file_name="accounting_balancesheet1.csv",
        mime="text/csv",
        icon=":material/download:"
    )

with col11:
    data2 = st.checkbox("Download Non-Current Assets")
    if data2:
        csv2 = convert_for_download(df= df2)
        st.write("Great!")
        st.download_button(
        label="Download CSV",
        data= csv2,
        file_name="accounting_balancesheet2.csv",
        mime="text/csv",
        icon=":material/download:"
)
        
with col12:
    data3 = st.checkbox("Download Current Liabilities")
    if data3:
        csv3 = convert_for_download(df= df3)
        st.write("Great!")
        st.download_button(
        label="Download CSV",
        data= csv3,
        file_name="accounting_balancesheet2.csv",
        mime="text/csv",
        icon=":material/download:"
)
     

# st.markdown("<span style='color: red;'>This text is red.</span>", unsafe_allow_html=True)


# uploaded_files = st.file_uploader(
#     "Choose a CSV file", accept_multiple_files=True
# )
# for uploaded_file in uploaded_files:
#     bytes_data = uploaded_file.read()
#     st.write("filename:", uploaded_file.name)
#     st.write(bytes_data)

# uploaded_file = pd.DataFrame()
# # edited_df = st.data_editor(df5)
# up_df = st.data_editor( uploaded_file)

