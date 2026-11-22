import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_excel('data of gurugram real Estate-selected-columns.xlsx')
# print(df.info())

# data cleaning
df.columns=df.columns.str.strip().str.lower().str.replace(' ','_')
# print(df.columns.tolist())
df=df.drop_duplicates()

# df['price']=df['price'].astype(str).str.replace(',', '').astype(float)
df['rera_approval']=df['rera_approval'].str.strip().str.lower().map({'approved by rera':True,'not approved by rera':False})
df["flat_type"] = df["flat_type"].str.strip().str.lower()
# print(df['rera_approval'])

# print(df)
# print(df.info())

# QUESTION 1(Which is the costliest flat in the dataset)
costiest_flat = df.loc[df['price'].idxmax()]
# print(costiest_flat)

# QUESTION 2(Which locality has the highest average price?)
highest_average_price_locality=df.groupby('locality')['price'].mean().idxmax()
# print(f"The locality with the highest average price is:- {highest_average_price_locality}")

# QUESTION 3(Which locality has the highest rate per square foot?)
highest_rate_per_square=df.groupby('locality')['rate_per_sqft'].mean().idxmax()
# print(f"The locality with the highest rate per square foot is:- {highest_rate_per_square}")

# QUEATION 4(Do ready-to-move properties cost more than under-construction properties?)
ready_to_move_average_price=df[df['status']=='ready to move']['price'].mean()
under_construction_avg_price=df[df['status']=='under construction']['price'].mean()

# if ready_to_move_average_price>under_construction_avg_price:
#     print('ready to move properties cost more on average than under construction properties')
# else:
#     print('under cnstruction properties cost more on average than ready to move properties')

# QUESTION 5(Do RERA-approved properties command a price premium?)
rera_approved_avg_price=df[df['rera_approval']==True]['price'].mean()
not_rera_approved_avg_price=df[df['rera_approval']==False]['price'].mean()

if rera_approved_avg_price>not_rera_approved_avg_price:
    print('RERA-approved properties command the price premium')
else:
    print('RERA-approved properties do not command the price premium')

# QUESTION 6(How does area (sqft) impact property price?)
# sns.lineplot(data=df,x='area',y='price')
# plt.xlabel('area')
# plt.ylabel('price')
# # plt.show()

# Which BHK configuration is the most expensive on average?
most_expensivebhk=df.groupby("bhk_count")["rate_per_sqft"].mean().idxmax()
# print(f"The most expensive bhk configration on an average:- {most_expensivebhk} BHK")

# Which property type (Apartment, Floor, Plot) is the costliest?
most_expensive_property_type=df.groupby("flat_type")["rate_per_sqft"].mean().idxmax()
# print(f"The most expensive property type is:- {most_expensive_property_type}")

# Do certain builders or companies consistently price higher?
print(df.groupby("company_name")['rate_per_sqft'].mean().sort_values(ascending=False).head(5))