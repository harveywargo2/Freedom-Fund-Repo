import pandas as pd
from datetime import date


class DividendYieldTheory:

    def __init__(self, **kwargs):
        self.div_df = kwargs.get('div_df', 'error')
        self.div_frequency = kwargs.get('div_frequency', 4)
        self.price_df = kwargs.get('price_df', 'error')
        self.lookback = kwargs.get('lookback', 21)
        self.dyt_df = self._dyt_df()
        self.dyt_aggr_df = self._dyt_aggr_df()


    def _dyt_df(self):
        div_df1 = self.div_df
        price_df1 = self.price_df
        div_var = 0.0
        current_year = date.today().year
        cutoff = self.lookback

        # Trim out special dividend
        div_df2 = div_df1.loc[div_df1['dividend_type'] == 'regular']

        # Drop Unused Columns
        div_df3 = div_df2.drop(['record_date', 'pay_date'], axis=1)

        # Join Price and Dividend Data
        dyt_df1 = price_df1.join(div_df3)

        # Remove NaN values
        dyt_df1['dividend_pay'] = dyt_df1['dividend_amount'].fillna(0)

        for index, row in dyt_df1.iterrows():
            if row['dividend_pay'] > 0:
                div_var = row['dividend_pay']

            else:
                dyt_df1.at[index, 'dividend_pay'] = div_var

        dyt_df1['dividend_fwd'] = dyt_df1['dividend_pay'] * self.div_frequency
        dyt_df1['dividend_yield_fwd'] = (dyt_df1['dividend_pay'] * self.div_frequency) / dyt_df1['share_price']

        # Convert DYT Dataframe to Pandas DateTime Index
        dyt_df1.index = pd.to_datetime(dyt_df1.index)

        # Reduce Dataframe Index By year
        for index, row in dyt_df1.iterrows():
            if current_year - index.year >= cutoff:
                dyt_df1.drop(index, inplace=True)

        return dyt_df1


    def _dyt_aggr_df(self):

        dyt_df1 = self.dyt_df

        dyt_df2 = dyt_df1.groupby(dyt_df1.index.year).agg(
            price_min=pd.NamedAgg(column='share_price', aggfunc='min'),
            price_max=pd.NamedAgg(column='share_price', aggfunc='max'),
            price_mean=pd.NamedAgg(column='share_price', aggfunc='mean'),
            price_median=pd.NamedAgg(column='share_price', aggfunc='median'),
            div_yield_min=pd.NamedAgg(column='dividend_yield_fwd', aggfunc='min'),
            div_yield_max=pd.NamedAgg(column='dividend_yield_fwd', aggfunc='max'),
            div_yield_mean=pd.NamedAgg(column='dividend_yield_fwd', aggfunc='mean'),
            div_yield_median=pd.NamedAgg(column='dividend_yield_fwd', aggfunc='median'),
            div_amount_cy=pd.NamedAgg('dividend_amount', aggfunc='sum')

        )

        dyt_df3 = dyt_df2
        dyt_df3['price_mean'] = round(dyt_df2['price_mean'], 2)
        dyt_df3['price_median'] = round(dyt_df2['price_median'], 2)
        dyt_df3['div_yield_min'] = round(dyt_df2['div_yield_min'] * 100, 2)
        dyt_df3['div_yield_max'] = round(dyt_df2['div_yield_max'] * 100, 2)
        dyt_df3['div_yield_mean'] = round(dyt_df2['div_yield_mean'] * 100, 2)
        dyt_df3['div_yield_median'] = round(dyt_df2['div_yield_median'] * 100, 2)
        dyt_df3['div_amount_cy'] = round(dyt_df2['div_amount_cy'], 2)
        dyt_df3['price_spread'] = round(dyt_df3['price_max'] - dyt_df3['price_min'], 2)
        dyt_df3['yield_spread'] = round(dyt_df3['div_yield_max'] - dyt_df3['div_yield_min'], 2)

        return dyt_df3




class DytFwdProjections:

    def __init__(self, div_start_year=date.today().year, div_growth_rate=.04, projection_yrs=10, buy_yield=0,
                 pivot=.03, div_start=0):
        self.div_start_year = div_start_year
        self.div_growth_rate = div_growth_rate
        self.projection_yrs = projection_yrs
        self.buy_yield = buy_yield
        self.pivot = pivot
        self.div_start = div_start
        self.current_year = date.today().year
        self.buy_price = round(self.div_start/self.buy_yield, 2)
        self.proj_df = self._proj_df()


    def _proj_df(self):
        start = self.div_start_year
        proj_yrs = self.projection_yrs
        div_amount = self.div_start
        div_growth_rate = self.div_growth_rate
        pivot = self.pivot
        buy_price = self.buy_price


        date_list = []
        div_list = []


        for index in range(proj_yrs):
            year = start + index
            date_list.append(year)

        for index in range(proj_yrs):
            div_list.append(div_amount)
            div_amount = round((div_amount * div_growth_rate) + div_amount, 2)


        proj_df = pd.DataFrame(div_list, index=date_list, columns=['dividend'])
        proj_df['ivp'] = round(proj_df['dividend'] / pivot, 2)
        proj_df['yoc'] = round((proj_df['dividend'] / buy_price) * 100, 2)

        tot_div_calc = div_list
        tot_div_calc[0] = 0
        tot_div_list = []
        tot_amt = 0

        for item in tot_div_calc:
            tot_amt += item
            tot_div_list.append(tot_amt)


        proj_df['total_div'] = tot_div_list
        proj_df['total_div'] = proj_df['total_div'].round(2)

        proj_df['cagr'] = pow((proj_df['ivp'] + proj_df['total_div']) / buy_price, 1 / (proj_df.index - start)) - 1
        proj_df['cagr'] = round(proj_df['cagr'] * 100, 2)

        proj_df.drop(2025, inplace=True)

        return proj_df

