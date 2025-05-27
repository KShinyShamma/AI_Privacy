# src/main.py

from auditor import evaluate_privacy_risks
from report_generator import generate_audit_report

def main():
    print("Privacy-Aware Generative AI Compliance Auditor")
    print("---------------------------------------------------")

    # Get system information from user
    system_name = input("Enter the name of the system you want to audit: ").strip()
    data_fields_input = input("Enter the data fields collected (comma separated): ").strip()
    purpose = input("Enter the purpose of the system: ").strip()

    # Process data fields into a list
    data_fields = [field.strip() for field in data_fields_input.split(",")]

    print("\n Evaluating Privacy Risks...\n")
    audit_result = evaluate_privacy_risks(system_name, data_fields, purpose)

    print("Evaluation Complete! Generating Audit Report...\n")
    report_path = generate_audit_report(system_name, audit_result)

    print(f"Audit Report Saved at: {report_path}")
    print("\n All Done!")

if __name__ == "__main__":
    main()
