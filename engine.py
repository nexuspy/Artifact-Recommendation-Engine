import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class RecommendationEngine:
    def __init__(self):
        self.products = pd.read_csv('data/products.csv')
        self.purchases = pd.read_csv('data/purchases.csv')
        # Aggregate ratings in case of multiple purchases of the same product by the same user
        self.purchases_agg = self.purchases.groupby(['user_id', 'product_id'])['rating'].mean().reset_index()
        self.user_product_matrix = self.purchases_agg.pivot(index='user_id', columns='product_id', values='rating').fillna(0)
        self.item_similarity = cosine_similarity(self.user_product_matrix.T)
        self.item_similarity_df = pd.DataFrame(self.item_similarity, index=self.user_product_matrix.columns, columns=self.user_product_matrix.columns)

    def get_recommendations(self, user_id, num_recommendations=3):
        if user_id not in self.user_product_matrix.index:
            # Return trending products if user is new
            return self.products.head(num_recommendations).to_dict(orient='records')

        user_ratings = self.user_product_matrix.loc[user_id]
        scores = self.item_similarity_df.dot(user_ratings).sort_values(ascending=False)
        
        # Remove already purchased products
        purchased_products = self.purchases[self.purchases['user_id'] == user_id]['product_id'].tolist()
        recommendations = scores.drop(purchased_products).head(num_recommendations)
        
        recommended_products = self.products[self.products['product_id'].isin(recommendations.index)]
        return recommended_products.to_dict(orient='records')

    def get_similar_products(self, product_id, num_similar=3):
        if product_id not in self.item_similarity_df.index:
            return []
        
        similar_scores = self.item_similarity_df[product_id].sort_values(ascending=False)
        similar_ids = similar_scores.iloc[1:num_similar+1].index
        
        similar_products = self.products[self.products['product_id'].isin(similar_ids)]
        return similar_products.to_dict(orient='records')

if __name__ == "__main__":
    engine = RecommendationEngine()
    print("Recommendations for User 1:", engine.get_recommendations(1))
    print("Similar to Product 1:", engine.get_similar_products(1))
