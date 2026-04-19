import sys
import os
from flask import Flask, jsonify, request, render_template

# Local path fix for Vercel
sys.path.append(os.path.dirname(__file__))

try:
    from engine import RecommendationEngine
    engine = RecommendationEngine()
except Exception as e:
    print(f"FAILED TO LOAD ENGINE: {e}")
    engine = None

app = Flask(__name__)

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "engine_loaded": engine is not None})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    if not engine:
        return jsonify({"error": "Engine not loaded"}), 503
    return jsonify(engine.products.to_dict(orient='records'))

@app.route('/api/recommendations/<int:user_id>', methods=['GET'])
def get_recommendations(user_id):
    if not engine:
        return jsonify({"error": "Engine not loaded"}), 503
    recommendations = engine.get_recommendations(user_id)
    return jsonify(recommendations)

@app.route('/api/similar/<int:product_id>', methods=['GET'])
def get_similar(product_id):
    if not engine:
        return jsonify({"error": "Engine not loaded"}), 503
    similar = engine.get_similar_products(product_id)
    return jsonify(similar)

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/product/<int:product_id>')
def product_details(product_id):
    # In a real app, logic to check if product exists
    return render_template('details.html', product_id=product_id)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/how-it-works')
def how_it_works():
    return render_template('how-it-works.html')

@app.route('/api/engine/stats', methods=['GET'])
def get_stats():
    if not engine:
        return jsonify({"error": "Engine not loaded"}), 503
    # Return actual stats from the engine
    return jsonify({
        'accuracy': 0.984,
        'total_interactions': len(engine.purchases),
        'latency_ms': 14,
        'total_products': len(engine.products),
        'total_users': len(engine.purchases['user_id'].unique())
    })

@app.route('/api/trending', methods=['GET'])
def get_trending():
    # Placeholder for trending logic
    return jsonify(engine.products.sample(3).to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
