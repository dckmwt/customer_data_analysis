import pandas as pd 
from sqlalchemy import create_engine
import urllib.parse
df = pd.read_csv("C:/Users/Hp/Desktop/customer_shopping/customer_shopping_behavior_missing.csv")

print(df.head(10))
print(df.info())
print(df.describe(include="all"))

# missing values 
missing_values = df.isnull().sum()
print("missing value witout data fill or cleaning :")
print(missing_values)

# Saare columns ke aage-peeche ke spaces (trim) hata dega
# df.columns = df.columns.str.strip()

mean_value_of_review = df["Review Rating"].mean()
print("mean value of review column : ")
print(mean_value_of_review)

# fill missing values 
# Iska asan matlab hai: "Har category ke khali review rating ko, usi category ke median (middle) rating se bhar do.

df["Review Rating"] = df.groupby("Category")["Review Rating"].transform(lambda x : x.fillna(x.median()))
missing_values_after_dataFill = df.isnull().sum()
print("missing value after fill data :")
print(missing_values_after_dataFill)

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" " , "_")
print(df.head(5))
# df.rename(columns={"purchase_amount_(usd)" : "purchase_amount"})  :- change the column name 
df=df.rename(columns={"purchase_amount_(usd)" : "purchase_amount"})
print(df.columns)

# create a column age_group 

lable = ["Young-Adult" , "Adult" , "Middle-aged" , "Senoir"]

"""
pd.qcut is a pandas function used for quantile-based discretization. 
It divides a 1D array or Series into equal-sized buckets based on rank or sample quantiles,
 meaning each bin will contain roughly the same number of data points (equal frequency).

"""
df["age_group"] = pd.qcut(df["age"] , q=4 , labels=lable)

# print(df[["age" , "age_group"]].head(10))

# create column purchase_frequency_days 

frequency_mapping = {
"Fortnightly" : 14 ,
"Weekly": 7 ,
"Monthly" : 30 ,
"Quarterly": 90 ,
"Bi-Weekly": 14 ,
"Annually":365 ,
"Every 3 months":90
}

df["purchase_frequency_days"] = df["frequency_of_purchases"].map(frequency_mapping)

# print(df[["frequency_of_purchases" ,"purchase_frequency_days" ]].head(10)) 

# drop promo_code_used column beacuse discount_applied column and both have same value 

df=df.drop("promo_code_used" , axis=1)


#  load data into mysql :- 

import pandas as pd
from sqlalchemy import create_engine

# --- इसके ऊपर आपका पुराना डेटा क्लीनिंग कोड होगा ---


# 1. अपने MySQL की डिटेल्स यहाँ सेट करें
USER = "root"
RAW_PASSWORD = "dp@2211"
HOST = "localhost"
PORT = "3306"
DATABASE = "customer_behavior"


PASSWORD = urllib.parse.quote_plus(RAW_PASSWORD)
# mysql.connector ड्राइवर का उपयोग करके कनेक्शन इंजन बनाएं
engine = create_engine(
    f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

# 2. जो टेबल का नाम आप MySQL में रखना चाहते हैं
table_name = "cleaned_shopping_data"

print("Uploading data to MySQL database... Please wait.")

# 3. DataFrame को सीधे MySQL में भेजें
df.to_sql(
    name=table_name,
    con=engine,
    if_exists="replace",  # अगर टेबल पहले से बनी है, तो उसे डिलीट करके नई टेबल बनाएगा
    index=False,  # Pandas के इंडेक्स (0, 1, 2...) को डेटाबेस में सेव नहीं करेगा
)

print(
    f"🎉 Success! {len(df)} rows loaded into the '{table_name}' table in MySQL."
)

"""
जब आप किसी string (टेक्स्ट) के आगे f या F लगा देते हैं, 
तो Python को समझ आ जाता है कि इस टेक्स्ट के अंदर करली ब्रैकेट्स { } के अंदर कुछ वेरिएबल्स या कोड लिखे हुए हैं, जिनकी वैल्यू निकाल कर वहाँ रखनी है।

"""