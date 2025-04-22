
# https://docs.streamlit.io/develop/api-reference


# chapter 3 - structure of financial reports

# balance sheet

financial_position = {
    "year 2021": {
        "current assets": {
            "cash_cash_equivalents": 1215,
            "trade_other_receivables": 15820,
            "inventories":8180
        },
        "non-current assets": {
            "available-for-sale investments": 3620,
            "investments in associates": 5500,
            "grapevines": 22000,
            "property plant equipment net": 34000,
            "intangible assets": 1,
            "deferred income tax": 27
        },
        "assets held for sale (discont. ops)": 0,
        "current liabilities": {
            "trade & other payables": 10700,
            "provision for warranties": 90,
            "taxes payable": 280,
            "current portion of finance lease obligation": 370,
            "current portion of long term debt": 10e3
        },
        "non-current liabilities": {
            "finance lease obligations": 2480,
            "long term debt": 20e3,
            "deferred income debt":3720,
            "employee pension benefits": 1470
        },
        "liabilities of discontinued operations": 0,
        "equity": {
            "share capital (issued & outstanding)": 15e3,
            "reserves": 660,
            "retained earnings": 25593
        }

    },

    "year 2020": {
        "current assets": {
            "cash_cash_equivalents": 11405,
            "trade_other_receivables": 13600,
            "inventories":7230
        },
        "non-current assets": {
            "available-for-sale investments": 3200,
            "investments in associates": 5000,
            "grapevines": 20000,
            "property plant equipment net": 30500,
            "intangible assets": 1,
            "deferred income tax": 24
        },
        "assets held for sale (discont. ops)": 2630,
        "current liabilities": {
            "trade & other payables": 9450,
            "provision for warranties": 80,
            "taxes payable": 250,
            "current portion of finance lease obligation": 340,
            "current portion of long term debt": 8e3
        },
        "non-current liabilities": {
            "finance lease obligations": 2850,
            "long term debt": 30e3,
            "deferred income debt":3190,
            "employee pension benefits": 1350
        },
        "liabilities of discontinued operations": 1440,
        "equity": {
            "share capital (issued & outstanding)": 13e3,
            "reserves": 240,
            "retained earnings": 23400
        }
    }
}




total_current_assets = sum(financial_position["year 2021"]['current assets'].values() )
print(total_current_assets)

total_noncurrent_assets = sum(financial_position["year 2021"]['non-current assets'].values() )
print(total_noncurrent_assets)

total_assets = total_current_assets + total_noncurrent_assets + financial_position["year 2021"]['assets held for sale (discont. ops)']
print(f"total assets = {total_assets}")

sum_liabilities = sum( financial_position["year 2021"]['current liabilities'].values() )
print("sum liabilities --",sum_liabilities)

total_noncurrent_liabilities = sum(financial_position["year 2021"]['non-current liabilities'].values() )
print(total_noncurrent_liabilities)

total_liabilities = sum_liabilities + total_noncurrent_liabilities + financial_position["year 2021"]['liabilities of discontinued operations']
print(f"total liabilities {total_liabilities}")

total_equity = sum( financial_position["year 2021"]['equity'].values() )
print(total_equity)

total_liabilities_equity =  total_equity + total_liabilities 
print(f"...... TOTAL = {total_liabilities_equity}")

# -----
total_current_assets = sum(financial_position["year 2020"]['current assets'].values() )
print(total_current_assets)

total_noncurrent_assets = sum(financial_position["year 2020"]['non-current assets'].values() )
print(total_noncurrent_assets)

total_assets = total_current_assets + total_noncurrent_assets + financial_position["year 2020"]['assets held for sale (discont. ops)']
print(f"total assets = {total_assets}")

sum_liabilities = sum( financial_position["year 2020"]['current liabilities'].values() )
print(sum_liabilities)

total_noncurrent_liabilities = sum(financial_position["year 2020"]['non-current liabilities'].values() )
print(total_noncurrent_liabilities)

total_liabilities = sum_liabilities + total_noncurrent_liabilities + financial_position["year 2020"]['liabilities of discontinued operations']
print(f"total liabilities {total_liabilities}")

total_equity = sum( financial_position["year 2020"]['equity'].values() )
print(total_equity)

total_liabilities_equity =  total_equity + total_liabilities 
print(f"...... TOTAL = {total_liabilities_equity}")













