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

# Dividend Yield Analysis
dya_df = div_df.div_yield_analysis_cy
dya_df.to_csv('Div_Yield_Analysis_Cy-' + ticker.upper() + '.csv')

with open('txn_audit_log.text', 'a') as file:
    file.write('\n' + 'Div_Yield_Analysis_Cy-' + ticker.upper() + ',Data Dump,' + str(today) + ',eol')

# Cash Flow Analysis
cash_flow_df = fy_df.analysis_fy_cash_flow
cash_flow_df.to_csv('Cash_Flow_Analysis_Fy-' + ticker.upper() + '.csv')

with open('txn_audit_log.text', 'a') as file:
    file.write('\n' + 'Cash_Flow_Analysis_Fy-' + ticker.upper() + ',Data Dump,' + str(today) + ',eol')

# Cost Flow Analysis
cost_flow_df = fy_df.analysis_fy_cost_flow
cost_flow_df.to_csv('Cost_Flow_Analysis_Fy-' + ticker.upper() + '.csv')

with open('txn_audit_log.text', 'a') as file:
    file.write('\n' + 'Cost_Flow_Analysis_Fy-' + ticker.upper() + ',Data Dump,' + str(today) + ',eol')

# Debt Analysis
debt_df = fy_df.analysis_fy_debt
debt_df.to_csv('Debt_Analysis_Fy-' + ticker.upper() + '.csv')

with open('txn_audit_log.text', 'a') as file:
    file.write('\n' + 'Debt_Analysis_Fy-' + ticker.upper() + ',Data Dump,' + str(today) + ',eol')

# Owner Analysis
owner_df = fy_df.analysis_fy_debt
owner_df.to_csv('Owner_Analysis_Fy-' + ticker.upper() + '.csv')

with open('txn_audit_log.text', 'a') as file:
    file.write('\n' + 'Owner_Analysis_Fy-' + ticker.upper() + ',Data Dump,' + str(today) + ',eol')

# Growth Analysis
growth_df = fy_df.analysis_fy_growth
growth_df.to_csv('Growth_Analysis_Fy-' + ticker.upper() + '.csv')

with open('txn_audit_log.text', 'a') as file:
    file.write('\n' + 'Growth_Analysis_Fy-' + ticker.upper() + ',Data Dump,' + str(today) + ',eol')

# Per Share Analysis
ps_df = fy_df.analysis_per_share
ps_df.to_csv('Growth_Analysis_Fy-' + ticker.upper() + '.csv')

with open('txn_audit_log.text', 'a') as file:
    file.write('\n' + 'Per_Share_Analysis_Fy-' + ticker.upper() + ',Data Dump,' + str(today) + ',eol')