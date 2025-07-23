import pandas as pd
import numpy as np

# Step 1: Load the dataset from the correct location
file_path = "C:/Users/anany/OneDrive/Documents/Social media campaign Performance/Advertising_Data.csv"
df = pd.read_csv(file_path)

# Step 2: Rename columns if necessary (optional)
df.columns = ['TV', 'Billboards', 'Google_Ads', 'Social_Media',
              'Influencer_Marketing', 'Affiliate_Marketing', 'Product_Sold']

# Step 3: Handle missing values
df.fillna(0, inplace=True)

# Step 4: Feature Engineering – Create new metrics
df['Total_Ad_Spend'] = df[['TV', 'Billboards', 'Google_Ads',
                           'Social_Media', 'Influencer_Marketing',
                           'Affiliate_Marketing']].sum(axis=1)

df['Cost_per_Sale'] = df['Total_Ad_Spend'] / df['Product_Sold']
df['ROI'] = (df['Product_Sold'] * 1.0 - df['Total_Ad_Spend']) / df['Total_Ad_Spend']

# Optional: Efficiency by channel
channels = ['TV', 'Billboards', 'Google_Ads', 'Social_Media',
            'Influencer_Marketing', 'Affiliate_Marketing']
for ch in channels:
    df[f'{ch}_Efficiency'] = df[ch] / df['Product_Sold']

# Step 5: Export cleaned dataset
output_path = "C:/Users/anany/OneDrive/Documents/Social media campaign Performance/Cleaned_AdCampaign.csv"
df.to_csv(output_path, index=False)

print("✅ Data processed and saved successfully for Power BI!")

