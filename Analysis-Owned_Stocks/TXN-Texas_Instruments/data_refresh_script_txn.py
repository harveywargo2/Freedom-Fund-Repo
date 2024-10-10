import aesoppy.gurufocus as gf
from dotenv import load_dotenv
import os
import datetime


load_dotenv()
gt = os.getenv('guru_token')
ticker = 'txn'
today = datetime.date.today()
div_df = gf.DivYieldAnalysis(token=gt, ticker=ticker)
fy_df = gf.AnnualFinAnalysis(token=gt, ticker=ticker)
div_pay = gf.DividendHistory(token=gt, ticker=ticker)

# Dividend Yield Analysis
dya_df = div_df.div_yield_analysis_cy
dya_df.to_csv('Data_Div_Yield_Cy-' + ticker.upper() + '.csv')

with open('data_refresh_audit_log_txn.text', 'a') as file:
    file.write('\n' + 'Data_Div_Yield_Cy-' + ticker.upper() + ',Data Dump,' + str(today) + ',eol')

# Cash Flow Analysis
cash_flow_df = fy_df.analysis_fy_cash_flow
cash_flow_df.to_csv('Data_Cash_Flow_Fy-' + ticker.upper() + '.csv')

with open('data_refresh_audit_log_txn.text', 'a') as file:
    file.write('\n' + 'Data_Cash_Flow_Fy-' + ticker.upper() + ',Data Dump,' + str(today) + ',eol')

# Cost Flow Analysis
cost_flow_df = fy_df.analysis_fy_cost_flow
cost_flow_df.to_csv('Data_Cost_Fy-' + ticker.upper() + '.csv')

with open('data_refresh_audit_log_txn.text', 'a') as file:
    file.write('\n' + 'Data_Cost_Fy-' + ticker.upper() + ',Data Dump,' + str(today) + ',eol')

# Debt Analysis
debt_df = fy_df.analysis_fy_debt
debt_df.to_csv('Data_Debt_Fy-' + ticker.upper() + '.csv')

with open('data_refresh_audit_log_txn.text', 'a') as file:
    file.write('\n' + 'Data_Debt_Fy-' + ticker.upper() + ',Data Dump,' + str(today) + ',eol')

# Owner Analysis
owner_df = fy_df.analysis_fy_owner
owner_df.to_csv('Data_Owner_Fy-' + ticker.upper() + '.csv')

with open('data_refresh_audit_log_txn.text', 'a') as file:
    file.write('\n' + 'Data_Owner_Fy-' + ticker.upper() + ',Data Dump,' + str(today) + ',eol')

# Growth Analysis
growth_df = fy_df.analysis_fy_growth
growth_df.to_csv('Data_Growth_Fy-' + ticker.upper() + '.csv')

with open('data_refresh_audit_log_txn.text', 'a') as file:
    file.write('\n' + 'Data_Growth_Fy-' + ticker.upper() + ',Data Dump,' + str(today) + ',eol')

# Per Share Analysis
ps_df = fy_df.analysis_per_share
ps_df.to_csv('Data_Per_Share_Fy-' + ticker.upper() + '.csv')

with open('data_refresh_audit_log_txn.text', 'a') as file:
    file.write('\n' + 'Data_Per_Share_Fy-' + ticker.upper() + ',Data Dump,' + str(today) + ',eol')


# Dividends Payouts
divpay_df = div_pay.div_df()
divpay_df.to_csv('Data_Dividends_Pay_Fy-' + ticker.upper() + '.csv')

with open('data_refresh_audit_log_txn.text', 'a') as file:
    file.write('\n' + 'Data_Dividend_Pay_Fy-' + ticker.upper() + ',Data Dump,' + str(today) + ',eol')