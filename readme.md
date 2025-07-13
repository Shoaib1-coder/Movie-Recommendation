
# 🎬 Movie Recommendation System

This is a simple Movie Recommendation System built using **Streamlit** and **K-Means Clustering**. The app suggests movies similar to a selected movie based on cluster grouping from preprocessed features.

---

## 🚀 Features

- Recommend similar movies using K-Means clustering
- Interactive UI built with Streamlit
- Easy deployment and customization

---

## 🛠️ Installation

### 1. 📥 Download Project
Clone the repository or download it as a ZIP:
```bash
git clone https://github.com/your-username/movie-recommendation-app.git
cd movie-recommendation-app
```

### 2. 💾 Install Anaconda (if not installed)
Download and install Anaconda from:  
🔗 https://www.anaconda.com/products/distribution

### 3. 🐍 Create a Virtual Environment
Open **Anaconda Prompt** and run:
```bash
conda create -n movie-recommender python=3.10 -y
conda activate movie-recommender
```

### 4. 📦 Install Dependencies
Make sure you're inside the project folder, then install required packages:
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

> Ensure `preprocess.csv` (clustered movie dataset) is in the same directory as `app.py`.

---

## 📁 Project Structure

```
movie-recommendation-app/
│
├── app.py                 # Streamlit app script
├── preprocess.csv         # Movie dataset with cluster labels
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 👨‍💻 Author

**Muhammad Shoaib Sattar**  
📧 mshoaib3393@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/shoaib-0b64a2204)

---

## 📝 License

This project is licensed under the MIT License - feel free to use and modify it.