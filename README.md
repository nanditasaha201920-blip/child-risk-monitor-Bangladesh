# 🇧🇩 Child Risk Monitor – Bangladesh

## 📌 Project Overview

Child Risk Monitor is a data-driven dashboard that identifies vulnerable regions in Bangladesh based on key child protection indicators such as school dropout, child labor, and early marriage.

The project combines multiple indicators into a **risk score**, helping visualize which regions require urgent attention.

---

## 🎯 Objectives

* Analyze child protection indicators in Bangladesh
* Identify high-risk regions using a composite risk score
* Provide an interactive dashboard for exploration
* Support data-driven decision-making

---

## 📊 Features

* 📈 Risk score calculation (dropout + labor + early marriage)
* 📍 Division-wise comparison
* 📅 Year-wise trends
* 📊 Interactive charts
* 📥 Downloadable dataset

---

## 🧮 Risk Score Formula

Risk Score is calculated as:

Risk Score = (Dropout Rate + Child Labor Rate + Child Marriage Rate) / 3

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas

---

## 📁 Project Structure

```
child-risk-monitor/
│
├── app.py
├── data.csv
└── requirements.txt
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/your-username/child-risk-monitor-bangladesh.git
cd child-risk-monitor-bangladesh
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the app

```
streamlit run app.py
```

---

## 📊 Dataset

The dataset contains:

* Division
* Year
* Dropout Rate (%)
* Child Labor Rate (%)
* Child Marriage Rate (%)

---

## 💡 Key Insights

* Regions with higher dropout rates tend to have higher child labor
* Early marriage sig


Author
Nandita Saha
