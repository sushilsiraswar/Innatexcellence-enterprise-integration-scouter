import os
import json
import requests
from openai import OpenAI

# 1. Initialize the client (Uses environment variables securely)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# 2. Simulate pulling live market/job data (Mocked for clean demonstration)
def fetch_raw_leads():
    # In a production environment, this would hit an RSS feed or API endpoint
    mock_market_data = [
        {
            "company": "Enterprise Logistics Corp",
            "trigger_event": "Job posting for 'Legacy Oracle DB Migration Consultant'",
            "description": "Looking for an expert to help move our 20-year-old on-premise inventory tracking DB to AWS Cloud PostgreSQL with zero downtime."
        },
        {
            "company": "QuickStart Mobile App Inc",
            "trigger_event": "Tech blog update: Launching a new feature",
            "description": "We are adding basic UI features using standard cloud wrappers."
        }
    ]
    return mock_market_data

# 3. Use an LLM to score the lead and generate an architectural hypothesis
def evaluate_and_scope_lead(lead):
    prompt = f"""
    You are a Lead Forward Deployed Engineer (FDE). Analyze this enterprise lead trigger:
    Company: {lead['company']}
    Trigger: {lead['trigger_event']}
    Details: {lead['description']}

    If this is a low-value, simple task, skip it. If it is a complex Integration or Migration project, provide:
    1. A 'Complexity Rating' (High/Medium/Low).
    2. 3 technical migration risks (e.g., data loss, schema mapping, legacy system down-time).
    3. A proposed high-level integration strategy (APIs, tools to consider).
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# 4. Main execution loop
if __name__ == "__main__":
    print("🚀 Initializing Integration Lead Generation System...")
    leads = fetch_raw_leads()
    
    for lead in leads:
        print(f"\nEvaluating {lead['company']}...")
        # Simple qualification logic based on your domain expertise rules
        if "Migration" in lead['trigger_event'] or "Legacy" in lead['description']:
            scoping_report = evaluate_and_scope_lead(lead)
            print("💎 High-Value Migration Lead Qualified! Scoping Report Generated:")
            print(scoping_report)
        else:
            print("⏩ Low technical complexity. Skipping lead.")
