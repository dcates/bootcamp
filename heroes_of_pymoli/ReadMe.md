

```python
# Observed Trends
# 1 More Males make purchases and have a sugnifigantly higher purchase volume, but only a 10 cent increase on the amount they spend
# 2 age group 20-24 are making the most purchases, but age group 40+ are spending the most on each purchase
# 3 Betrayal, Whisper of Grieving Widows and Arcane Gem are the most popular items to purchase
```


```python
# Import Dependencies
import pandas as pd
import numpy as np
```


```python
# Reference the file where the json is located
heroes_of_pymoli = "purchase_data.json"

# Import the data into a Pandas DataFrame
heroes_df = pd.read_json(heroes_of_pymoli)
#display top 5 lines
heroes_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Player Count

#finds amount of rows for unique SN (aka players)
pcount = len(heroes_df['SN'].unique())
#creates new dataframe for displaying data
totalplayers_df = pd.DataFrame({"Total Players": [pcount]})
totalplayers_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Purchasing Analysis (Total)

#count is used for total count of rows
count = heroes_df['SN'].count()

#Number of Unique Items
#finds number of rows for unique Items ID's
unique_items = len(heroes_df['Item ID'].unique())

#average price
# Averages all of Price column
num_of_pur_df = heroes_df["Price"].mean()

#Number of Purchases
#finds amount of rows for unique SN (aka players)
plyr = heroes_df["SN"].unique()

#Total Revenue
#adds all data in Price Column
ref = heroes_df["Price"].sum()

#creates new dataframe to store data calculated above
purch_analysis_df = pd.DataFrame({"Number of Unique Items": [unique_items],
                           "Average Purchase Price": [num_of_pur_df],
                           "Total Number of Purchases": [count],
                           "Total Revenue": [ref]})

#re arranges columns to match homework 
purch_analysis_reorder_df = purch_analysis_df[["Number of Unique Items","Average Purchase Price","Total Number of Purchases","Total Revenue"]]

#formats pricing into $ format
purch_analysis_reorder_df["Average Purchase Price"] = purch_analysis_reorder_df["Average Purchase Price"].map("${:.2f}".format)
purch_analysis_reorder_df["Total Revenue"] = purch_analysis_reorder_df["Total Revenue"].map("${:.2f}".format)

#displays data
purch_analysis_reorder_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Purchase Price</th>
      <th>Total Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Gender Demographics
#count is used for total count of rows
count = heroes_df['SN'].count()
#Counts total rows of data for each gender
gen_count = heroes_df["Gender"].value_counts()
#calculates percentages of each Gender Type
gen_perc = (heroes_df["Gender"].value_counts()) / count *100
#Puts data in dataframe
gen_dem_df = pd.DataFrame({"Percentage of Players": gen_perc, "Total Count": gen_count})
#formats Percent
gen_dem_df["Percentage of Players"] = gen_dem_df["Percentage of Players"].map("{:.2f}".format)
#Displays Data                                                         
gen_dem_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15</td>
      <td>633</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.44</td>
      <td>136</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.41</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Purchasing Analysis (Gender)

#Purchase Count
#Groups by Gender to calculate math
heroes_group = heroes_df.groupby(["Gender"])
#counts total purchases
purchase_count_df = heroes_group["Age"].count()

#Average Purchase Price
#Finds average purchase amount
avg_purch_price_df = heroes_group["Price"].mean()

#Total Purchase Value
#Calculates total purchase value
ttl_purch_val_df = heroes_group["Price"].sum()

#Normalized Totals
#Finds norm values
norm_totals_df = ttl_purch_val_df/purchase_count_df
#create new dataframe to display results
purch_analysis_gen_df = pd.DataFrame({"Purchase Count": purchase_count_df, "Average Purchase Price": avg_purch_price_df, "Total Purchase Value": ttl_purch_val_df, "Normalized Totals": norm_totals_df })
purch_analysis_gen_df
#Organize Table to match example
reorder_purch_analysis_gen_df = purch_analysis_gen_df[["Purchase Count","Average Purchase Price","Total Purchase Value", "Normalized Totals"]]
#Format Dollar Values
reorder_purch_analysis_gen_df["Average Purchase Price"] = reorder_purch_analysis_gen_df["Average Purchase Price"].map("${:.2f}".format)
reorder_purch_analysis_gen_df["Total Purchase Value"] = reorder_purch_analysis_gen_df["Total Purchase Value"].map("${:.2f}".format)
reorder_purch_analysis_gen_df["Normalized Totals"] = reorder_purch_analysis_gen_df["Normalized Totals"].map("${:.2f}".format)
#Display Results
reorder_purch_analysis_gen_df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$2.82</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1867.68</td>
      <td>$2.95</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$3.25</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Age Demographics

#Create Bins
bins = [0, 9, 14, 19, 24, 29, 34, 39, 100]
#Create Names for bins
group_names = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']

# Place the data series into a new column inside of the DataFrame
heroes_df["Age Dem"] = pd.cut(heroes_df["Age"], bins, labels=group_names)
heroes_df.head()

#Purchase Count
#Group By to start calculate math
age_dem_heroes_group = heroes_df.groupby(["Age Dem"])
#Count total purchases
age_dem_purchase_count_df = age_dem_heroes_group["Age"].count()

#Average Purchase Price
#Calculate Average
age_dem_avg_purch_df = age_dem_heroes_group["Price"].mean()

#Total Purchase Value
#Calculate total value
age_dem_ttl_purch_val_df = age_dem_heroes_group["Price"].sum()

#Normalized Totals
#Calculate normalized Values
age_dem_norm_totals_df = age_dem_ttl_purch_val_df/age_dem_purchase_count_df

#create new dataframe to display results
purch_analysis_gen_df = pd.DataFrame({"Purchase Count": age_dem_purchase_count_df, "Average Purchase Price": age_dem_avg_purch_df, "Total Purchase Value": age_dem_ttl_purch_val_df, "Normalized Totals": age_dem_norm_totals_df })

#Organize Table to match example
age_dem_reorder_purch_analysis_gen_df = purch_analysis_gen_df[["Purchase Count","Average Purchase Price","Total Purchase Value", "Normalized Totals"]]

#Format Dollar Values
age_dem_reorder_purch_analysis_gen_df["Average Purchase Price"] = age_dem_reorder_purch_analysis_gen_df["Average Purchase Price"].map("${:.2f}".format)
age_dem_reorder_purch_analysis_gen_df["Total Purchase Value"] = age_dem_reorder_purch_analysis_gen_df["Total Purchase Value"].map("${:.2f}".format)
age_dem_reorder_purch_analysis_gen_df["Normalized Totals"] = age_dem_reorder_purch_analysis_gen_df["Normalized Totals"].map("${:.2f}".format)
#Display Results
age_dem_reorder_purch_analysis_gen_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age Dem</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>28</td>
      <td>$2.98</td>
      <td>$83.46</td>
      <td>$2.98</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>35</td>
      <td>$2.77</td>
      <td>$96.95</td>
      <td>$2.77</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>$2.91</td>
      <td>$386.42</td>
      <td>$2.91</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>$2.91</td>
      <td>$978.77</td>
      <td>$2.91</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>$2.96</td>
      <td>$370.33</td>
      <td>$2.96</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>$3.08</td>
      <td>$197.25</td>
      <td>$3.08</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42</td>
      <td>$2.84</td>
      <td>$119.40</td>
      <td>$2.84</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>$3.16</td>
      <td>$53.75</td>
      <td>$3.16</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Top Spenders
#Purchase Count
#group by SN to calculate math
top_spenders = heroes_df.groupby(["SN"])
#count total purchases by player
top_pcount_df = top_spenders["SN"].count()

#Average Purchase Price
#Calculate average price of purchase by user
top_ave_pprice_df = top_spenders["Price"].mean()

#Total Purchase Value
#Calculate total purchased by user
top_total_value_df = top_spenders["Price"].sum()

#create new dataframe to display results
top_spenders_df = pd.DataFrame({"Purchase Count": top_pcount_df, "Average Purchase Price": top_ave_pprice_df, "Total Purchase Value": top_total_value_df})

#Organize Table to match example
reorder_top_spenders_df = top_spenders_df[["Purchase Count","Average Purchase Price","Total Purchase Value"]]
#Format Dollar Values
reorder_top_spenders_df["Average Purchase Price"] = reorder_top_spenders_df["Average Purchase Price"].map("${:.2f}".format)
reorder_top_spenders_df["Total Purchase Value"] = reorder_top_spenders_df["Total Purchase Value"].map("${:.2f}".format)

# To sort from highest to lowest, ascending=False must be passed in
top_spenders_sorted_df = reorder_top_spenders_df.sort_values("Purchase Count", ascending=False)
top_spenders_sorted_df.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Qarwen67</th>
      <td>4</td>
      <td>$2.49</td>
      <td>$9.97</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Sondastan54</th>
      <td>4</td>
      <td>$2.56</td>
      <td>$10.24</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Popular Items
#Item grouping
pop_item_id = heroes_df.groupby(["Item ID", "Item Name"])
#Purchasing Count
#Count by Item ID
pop_pcount_df = pop_item_id["Item Name"].count()

#Item Price
#setting column to review for item price
pop_itemprice_df = heroes_df["Price"]
#looking at first item in array to display item price
first_pop_itemprice_df = pop_itemprice_df[0]
#Total Purchase Value
#Multiply Item Count by Item Price to get total value
pop_totalvalue_df = pop_pcount_df * first_pop_itemprice_df

#create new dataframe to display results
pop_items_df = pd.DataFrame({"Purchase Count": pop_pcount_df, "Item Price": first_pop_itemprice_df, "Total Purchase Value": pop_totalvalue_df})

#Organize Table to match example
reorder_pop_items_df = pop_items_df[["Purchase Count","Item Price","Total Purchase Value"]]
# To sort from highest to lowest for Purchase Count
most_pop_pop_items_df = reorder_pop_items_df.sort_values("Purchase Count", ascending=False)

#Format Dollar Values
most_pop_pop_items_df["Item Price"] = most_pop_pop_items_df["Item Price"].map("${:.2f}".format)
most_pop_pop_items_df["Total Purchase Value"] = most_pop_pop_items_df["Total Purchase Value"].map("${:.2f}".format)

# Reviewing top 5 results
most_pop_pop_items_df.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>$3.37</td>
      <td>$37.07</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>$3.37</td>
      <td>$37.07</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>$3.37</td>
      <td>$30.33</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>9</td>
      <td>$3.37</td>
      <td>$30.33</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>$3.37</td>
      <td>$30.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Profitable Items
#Item grouping
prpop_item_id = heroes_df.groupby(["Item ID", "Item Name"])
#Purchasing Count
#Count by Item ID
prpop_pcount_df = prpop_item_id["Item Name"].count()

#Item Price
#setting column to review for item price
prpop_itemprice_df = heroes_df["Price"]
#looking at first item in array to display item price
prfirst_pop_itemprice_df = prpop_itemprice_df[0]
#Total Purchase Value
#Multiply Item Count by Item Price to get total value
prpop_totalvalue_df = prpop_pcount_df * prfirst_pop_itemprice_df

#create new dataframe to display results
prpop_items_df = pd.DataFrame({"Purchase Count": prpop_pcount_df, "Item Price": prfirst_pop_itemprice_df, "Total Purchase Value": prpop_totalvalue_df})

#Organize Table to match example
prreorder_pop_items_df = prpop_items_df[["Purchase Count","Item Price","Total Purchase Value"]]
# To sort from highest to lowest for Purchase Count
prmost_pop_pop_items_df = prreorder_pop_items_df.sort_values("Purchase Count", ascending=False)

#Format Dollar Values
prmost_pop_pop_items_df["Item Price"] = prmost_pop_pop_items_df["Item Price"].map("${:.2f}".format)
prmost_pop_pop_items_df["Total Purchase Value"] = prmost_pop_pop_items_df["Total Purchase Value"].map("${:.2f}".format)

# Reviewing top 5 results
prmost_pop_pop_items_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>$3.37</td>
      <td>$37.07</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>$3.37</td>
      <td>$37.07</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>$3.37</td>
      <td>$30.33</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>9</td>
      <td>$3.37</td>
      <td>$30.33</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>$3.37</td>
      <td>$30.33</td>
    </tr>
  </tbody>
</table>
</div>


