# AI_Privacy
A GPT-powered CLI tool to audit AI systems for GDPR &amp; EU AI Act compliance.
# AI Privacy Compliance Auditor

A command-line tool that audits AI systems for privacy and data protection risks under **GDPR** and the **EU AI Act**, powered by OpenAI's GPT models.

## Features

- Evaluates AI system data usage and purpose using OpenAI GPT-3.5
- Generates structured Markdown reports highlighting:
  - Risk areas
  - Risk level (High/Medium/Low)
  - Suggested remediation actions
- Uses environment variables for secure API key handling
- Modular architecture for easy extension and maintenance
- Runs in local terminal or Colab (via cloudflared for UI testing)

---

## Example Use Case

**System:** SmartHire AI  
**Data Fields:** name, email, phone number, resume, photo  
**Purpose:** Automate candidate screening for job applications  

**Sample Output:**
- Risk Level: `Medium`
- Risk Areas: data minimization, consent, AI bias, security
- Report saved as: `docs/audit_reports/smarthire_audit_YYYYMMDD_HHMM.md`

---


