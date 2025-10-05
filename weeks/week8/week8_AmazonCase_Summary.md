# Week 8 – Amazon Hiring Bias Case Study

## 📌 Case Overview
In 2014, Amazon started developing an **AI recruiting system** to automatically screen CVs.  
The goal was to make the hiring process faster and more efficient by using machine learning.  

However, the system was trained on **historical data** dominated by male applicants in the tech sector.  
As a result, the model **learned patterns of gender bias** and systematically downgraded CVs from women.

---

## ⚠️ What Went Wrong
- The model **penalized resumes that contained the word "women"**, such as “women’s chess club captain.”  
- Male-dominated data → algorithm concluded that **male candidates were preferable**.  
- Attempts to fix the model by removing gender-related keywords were not successful.  
- In the end, Amazon **abandoned the project** in 2018.

---

## 🎯 Key Lessons

### Ethics
- Fairness must be built into the system design.  
- AI should **not replicate existing human biases**.  

### Security
- Training data must be **audited and monitored** not only for accuracy, but also for bias.  
- Continuous testing is required to detect hidden patterns.  

### Privacy
- Anonymization of personal identifiers (gender, name, school clubs, etc.) can reduce bias.  
- Protecting Personally Identifiable Information (PII) is also a GDPR requirement.  

### Compliance
- In the EU, such a system would directly **violate GDPR** and **anti-discrimination laws**.  
- Regulatory frameworks increasingly demand **transparency and explainability** of AI models.  

---

## 🔍 Reflection
If I were designing such a system today:  
1. I would implement **bias detection audits** during the training process.  
2. I would use **diverse and balanced datasets** to prevent one group from being overrepresented.  
3. I would apply **data anonymization techniques** to remove gender-linked signals.  
4. I would ensure full **compliance with GDPR** and labor anti-discrimination regulations.  

---

📂 *File path in repo:*  
`/weeks/week8/ethics_security_privacy/Week8_Amazon_CaseStudy.md`
