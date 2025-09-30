# Privacy & Security Basics – Week 6

As part of my AI Ethics and Security journey, I tested a website using **Mozilla Observatory** to identify potential privacy risks.

**Findings:**  
- Missing Content Security Policy  
- Cookies set without using the Secure flag, but transmission over HTTP prevented by HSTS.
- X-Content-Type-Options header not implemented.
- X-Frame-Options (XFO) header not implemented.

  
I also created a **Python script** to generate anonymized test data using the Faker library. This ensures that no real personal information is used in testing AI or datasets.

**Key takeaway:** Small steps like website testing and anonymized test data already improve security and privacy, forming the foundation of responsible AI.
