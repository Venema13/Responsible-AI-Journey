# Week 8 – Amazon Hiring Bias Case Study

## Background
In 2014–2015 Amazon experimented with an internal AI recruitment tool to rank résumés and recommend candidates.  
The system was trained on **10 years of past hiring data** from Amazon.

## Problem
- Historical hiring data reflected a **male-dominated tech industry**.  
- The AI learned patterns that favored **male applicants** over female applicants.  
- Words such as "women’s chess club" or universities with higher female representation caused candidates to be ranked lower.  
- Resumes containing certain male-related terms were favored.

## Key Insights
- **Garbage in, garbage out**: if training data is biased, the model learns and amplifies it.  
- **Sensitive attributes** (gender) don’t have to be explicitly included; proxies (words, schools, activities) still transfer bias.  
- Even anonymized résumés are not safe if text contains gendered signals.

## Ethical & Compliance Concerns
- **Fairness**: Violated equal opportunity principles.  
- **Transparency**: Candidates were unaware of algorithmic filtering.  
- **GDPR**: Would raise issues with automated decision-making (Art. 22 GDPR).  
- **Reputation**: A bias scandal damages trust in both the company and AI in general.

## Lessons Learned
1. **Bias detection is mandatory**: models must be tested for group fairness before deployment.  
2. **Data minimization**: avoid including features that may act as gender proxies.  
3. **Explainability**: techniques like SHAP/LIME can uncover why a model prefers certain terms.  
4. **Human-in-the-loop**: AI should support, not replace, human hiring decisions.  
5. **Governance**: Companies need compliance checks, fairness audits, and clear documentation before using AI in HR.

## References
- Reuters (2018): *Amazon scraps secret AI recruiting tool that showed bias against women*.  
- GDPR Article 22: *Automated individual decision-making, including profiling*.  
