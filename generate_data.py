import pandas as pd
import numpy as np
import os

# Create product data
num_products = 50
products = pd.DataFrame({
    'product_id': range(1, num_products + 1),
    'name': [f'Premium Item {i}' for i in range(1, num_products + 1)],
    'category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Beauty', 'Sports', 'Lifestyle'], num_products),
    'price': np.random.randint(20, 2000, num_products)
})

# Create user purchase data
np.random.seed(42)
users = range(1, 21)
purchases = []
for user_id in users:
    num_purchases = np.random.randint(3, 10)
    for _ in range(num_purchases):
        product_id = np.random.randint(1, num_products + 1)
        purchases.append({'user_id': user_id, 'product_id': product_id, 'rating': np.random.randint(1, 6)})

purchase_data = pd.DataFrame(purchases)

# Save to CSV
os.makedirs('data', exist_ok=True)
products.to_csv('data/products.csv', index=False)
purchase_data.to_csv('data/purchases.csv', index=False)

print("Sample data generated successfully.")
