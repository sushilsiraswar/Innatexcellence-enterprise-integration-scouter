import os
import streamlit as st
from groq import Groq  # Switched from openai to groq

# 1. Page Configuration
st.set_page_config(page_title="FDE Integration Scouter", page_icon="💎", layout="wide")

# 2. Check for API Key securely (Now looks for GROQ_API_KEY)
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    st.error("🔑 Groq API Key not found. Please set the GROQ_API_KEY environment variable.")
    st.stop()

client = Groq(api_key=api_key)

# 3. AI Evaluation Function
def evaluate_and_scope_lead(company, trigger, description):
    prompt = f"""
    You are a Lead Forward Deployed Engineer (FDE). Analyze this enterprise lead:
    Company: {company}
    Trigger Event: {trigger}
    Details: {description}

    Provide a highly professional technical evaluation:
    1. COMPLEXITY RATING: (High, Medium, or Low with brief justification)
    2. CORE SYSTEM INFRASTRUCTURE RISKS: (List 3 critical migration/integration risks)
    3. TARGET ARCHITECTURE INFRASTRUCTURE MITIGATION STRATEGY: (Propose tools, API strategies, or patterns)
    """
    
    with st.spinner("🧠 Free Groq AI Agent analyzing architectural risks... Please wait."):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # An incredibly powerful, free alternative to GPT-4o
            messages=[{"role": "user", "content": prompt}]
        )
    return response.choices.message.content

# 4. Dashboard Visual Layout
st.title("💎 Enterprise Integration & Migration Discovery Agent")
st.markdown("### A Forward Deployed Engineering Pre-Sales & Scoping Dashboard")
st.write("Leverage 20+ years of functional scoping logic combined with agentic LLM analysis to instantly discover architectural data migration risks.")

st.divider()

col1, col2 = st.columns()

with col1:
    st.subheader("📋 Lead Input Parameters")
    company_input = st.text_input("Company Name", value="Global Finance Corp")
    trigger_input = st.text_input("Trigger Event / Indicator", value="Migrating on-prem Core Banking to Cloud")
    desc_input = st.text_area(
        "Detailed System Context", 
        value="Looking to shift a 25-year-old legacy IBM DB2 database containing over 5TB of customer financial records to AWS Aurora PostgreSQL with zero regulatory downtime."
    )
    submit_button = st.button("🚀 Analyze Integration & Generate Report", type="primary")

with col2:
    st.subheader("📊 Generated FDE Scoping Report")
    if submit_button:
        report = evaluate_and_scope_lead(company_input, trigger_input, desc_input)
        st.success("✅ Technical Discovery Analysis Complete!")
        st.markdown(report)
    else:
        st.info("👈 Enter details on the left panel and click 'Analyze' to spin up the automated architectural evaluation report.")
