# Week 7 – Transparency & GDPR

## 📖 Introduction
This week I worked on **transparency** in AI models and the basics of the **GDPR (General Data Protection Regulation)**.  
Goal: show how a model makes decisions, while ensuring that personal data is handled correctly and securely.

---

## 🧠 Model + Explainability
I trained a simple **machine learning model** on the Titanic dataset.  
- **Goal:** predict whether a passenger survived or not.  
- **Explainability methods used:**  
  - **LIME (Local Interpretable Model-agnostic Explanations):** shows which features influenced individual predictions.  
  - **SHAP (SHapley Additive exPlanations):** provides a global overview of which features contribute the most to model decisions.  

📂 Files:  
- `Week7_Notebook.ipynb` (model + explainability code)  
- `lime_example.png` (LIME visualization example)  
- `shap_summary.png` (SHAP summary of feature importance)  

**Key insights:**  
- LIME showed that **ticket class** and **gender** were often decisive for individual predictions.  
- SHAP confirmed that these features also had the strongest global impact on the model.  
- Transparency tools help build trust in AI models.

---

## ⚖️ GDPR Key Principles
The GDPR contains 7 core principles that are essential for AI projects:

1. **Lawfulness, fairness, and transparency**  
   → Always explain clearly how and why data is used.  

2. **Purpose limitation**  
   → Use data only for the purpose it was collected for.  

3. **Data minimization**  
   → Do not collect more data than necessary.  

4. **Accuracy**  
   → Keep data up to date and correct errors.  

5. **Storage limitation**  
   → Delete or anonymize data once it’s no longer needed.  

6. **Integrity and confidentiality**  
   → Protect data from unauthorized access or leaks.  

7. **Accountability**  
   → Be able to prove compliance with the rules.  

---

## 🔍 GDPR Applied to this Project
- Dataset: Titanic passenger data includes **sensitive fields** (like name, ticket number).  
- Step: removed or ignored PII (personally identifiable information).  
- Model and visualizations: worked only with **non-personal data** (age, gender, class, family members).  
- Documentation: explained LIME/SHAP to meet GDPR **transparency requirements**.  

---

## ✍️ Reflection
- AI models are often a "black box", but tools like LIME and SHAP add explainability.  
- GDPR forces us to treat data **ethically and carefully**.  
- Transparency + privacy = essential for trustworthy AI.  

---

## ✅ Next Step (Week 8)
- Continue with **case studies** (Amazon hiring bias).  
- Build a **Python script to automatically detect and anonymize PII**.  
- Publish code and notes in GitHub repo.
