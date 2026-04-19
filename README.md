# 🌌 Ethereal Vault: AI-Powered Artifact Discovery

A premium, production-grade recommendation engine built to curate aesthetic artifacts through high-dimensional user-product interaction mapping. This project transforms raw purchase data into a stunning, glassmorphic visual experience.

---

## 🧠 Backend Engine Architecture

The core of the Ethereal Vault is a custom-built recommendation pipeline that utilizes Collaborative Filtering and Vector Space Modeling.

### 1. Data Orchestration (Pandas)

- **Sparse Matrix Generation**: Interaction data is transformed into a high-dimensional pivot table mapping `user_id` to `product_id`.
- **Normalization**: User interaction weights are scaled to prevent bias from high-frequency collectors.

### 2. Neural Mapping (Scikit-Learn)

- **Cosine Similarity**: The engine calculates the angular distance between user vectors in product space.
- **Algorithm**: `similarity = cos(θ) = (A · B) / (||A|| ||B||)`
- **Dynamic Retrieval**: Recommendations are recalculated in real-time based on the current active user profile, ensuring an evolving discovery stream.

### 3. API Layer (Flask)

- **RESTful Endpoints**: Provides granular access to product metadata, similar items, trending collections, and engine system health.
- **Real-time Stats**: A dedicated `/api/engine/stats` endpoint monitors inference latency and database integrity.

---

## 🛠️ The Tech Stack

### Frontend: Aesthetic Excellence

- **Tailwind CSS**: Utility-first styling for high-performance responsive layouts.
- **GSAP (GreenSock)**: Industry-standard animation engine for fluid entrance transitions and staggered grid effects.
- **Google Fonts**: Custom pairing of _Manrope_ (Headlines) and _Inter_ (UI Labels) for a premium typographic feel.
- **Glassmorphism**: Advanced CSS blur filters and translucent layering for a depth-rich interface.

### Backend: Intelligence & Performance

- **Python 3.12+**: High-level logic and data processing.
- **Flask**: Lightweight WSGI micro-framework for API orchestration.
- **Pandas**: Efficient data manipulation and matrix operations.
- **Scikit-Learn**: Mathematical core for similarity calculations and cluster discovery.

---

## 🚀 Deployment & Operations

### Prerequisites

- Python installed on your local environment.
- PIP (Python Package Installer).

### Installation

```bash
# Clone the repository
git clone https://github.com/your-repo/ethereal-vault.git

# Navigate to project root
cd ethereal-vault

# Install core dependencies
pip install flask pandas scikit-learn
```

### Execution

```bash
# Launch the discovery engine
python app.py
```

Access the vault at: `http://127.0.0.1:5000`

---

## 🗺️ Visual Ecosystem

- **Dashboard**: Global recommendation feed.
- **Catalog**: Comprehensive staggered artifact discovery.
- **Logic View**: Architecture visualization and engine performance.
- **Pulse Profile**: User analytics and acquisition history.

---

_Developed with precision by Antigravity._
