# Week 6 – Privacy Test Report

**Objective:** Test a website for privacy/security risks using Mozilla Observatory.

**Website tested:** www.bol.com
**Test date:** 30 september 2025
**Observatory score:** 45/100

---

## Findings
1. Missing Content Security Policy (CSP)
2. Cookies
3. X-Content-Type-Options
4. X-Frame-Options

---

## Actionable Steps
- Implement missing security headers  
- Use secure flag
- X-Content-Type-Options header not implemented. - Set to nosniff.
- X-Frame-Options (XFO) header not implemented. - Implement frame-ancestors CSP

---

## Additional Exercise: Data Anonymization
- Python script (`fake_data_generator.py`) generates fake names, emails, and phone numbers for safe testing
- Helps avoid exposing real personal data in datasets or tests
