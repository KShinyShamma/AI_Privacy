import os
from datetime import datetime

def generate_audit_report(system_name: str, audit_result: dict, save_dir: str ="docs/audit_reports") -> str:


    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{system_name.lower().replace('','_')}_audit_{timestamp}.md"
    file_path = os.path.join(save_dir, filename)

    with open(file_path, "w") as f:
        f.write(f"# Private Audit Report: {system_name}\n\n")
        f.write(f"**Audit Timestamp:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## Identified Risk Areas:\n")
        for risk in audit_result.get("risk_areas", []):
            f.write(f"- {risk}\n")
        
        f.write("Risk Level:")
        f.write(f"**{audit_result.get('risk_level', 'Unknown')}**\n")
        
        f.write("\n## Suggested Remediation Actions:\n")
        for action in audit_result.get("suggested_actions", []):
            f.write(f"- {action}\n")

    return file_path

if __name__ == "__main__":
    # Example for testing
    dummy_result = {
        "risk_areas": ["Over-collection", "Profiling"],
        "risk_level": "High",
        "suggested_actions": ["Collect minimal fields", "Provide clear user consent form"]
    }
    path = generate_audit_report("Employee Chatbot", dummy_result)

    print(f"Report generated at: {path}")
