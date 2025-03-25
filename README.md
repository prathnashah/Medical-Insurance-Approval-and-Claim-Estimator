# Medical-Insurance-Approval-and-Claim-Estimator

This Streamlit app predicts whether a medical insurance claim will be approved and estimates the claim amount based on user input.

## 🚀 Features
- **Step 1:** Check if your insurance claim is approved.
- **Step 2:** If approved, estimate the claim amount.
- Uses **Logistic Regression** for claim approval classification.
- Applies **custom deduction logic** for claim estimation.
- Hosted on **Render**.

## 📌 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

## 📊 How It Works
1. **User Inputs:** Enter age, medical charges, smoking status, health conditions, exercise habits, and policy type.
2. **Approval Prediction:** Logistic regression predicts if the claim is approved.
3. **Claim Estimation:** If approved, a formula calculates the estimated amount.

## 🌍 Deployment on Render
1. **Push Code to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```
2. **Deploy on Render:**
   - Go to [Render](https://render.com/) and create a **New Web Service**.
   - Connect your GitHub repo.
   - Set **Build Command:**
     ```bash
     pip install -r requirements.txt
     ```
   - Set **Start Command:**
     ```bash
     streamlit run app.py --server.port $PORT --server.address 0.0.0.0
     ```
   - Deploy and get your app's **public URL**!

## 📂 Project Structure
```
/your-streamlit-app  
│── app.py  # Streamlit script  
│── requirements.txt  # Dependencies  
│── models/  # ML models (logistic_model.pkl, scaler_clf.pkl, etc.)  
│── README.md  # Project details  
```

## 🛠 Technologies Used
- **Python**
- **Streamlit**
- **Pandas, NumPy**
- **Scikit-learn**
- **Joblib**
- **Render** (for deployment)

## 🤖 Future Enhancements
- Improve model accuracy with advanced ML techniques.
- Add a more interactive UI for better user experience.

## 📞 Contact
For any issues or suggestions, feel free to open an issue or reach out!

---
**🔗 Live App:** [Your Render App URL]
