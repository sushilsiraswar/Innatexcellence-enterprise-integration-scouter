# Enterprise Integration & Migration Scouter Agent

An automated pipeline designed to scout, qualify, and structurally scope high-value enterprise software migration opportunities. This agent shifts lead generation from generic email harvesting to technical discovery.

## 🧠 Why This Project Exists (The Scoping Perspective)
In complex enterprise environments, the hardest part of a Forward Deployed Engineer (FDE) engagement is the "Discovery Phase." Sales teams struggle to identify technical triggers, resulting in poorly scoped migration proposals. 

This script demonstrates an automated workflow that identifies structural tech-stack inflection points (e.g., migrating legacy Oracle databases to AWS) and uses generative AI to instantly execute a technical risk analysis.

## 🛠️ Architecture Overview
1. **Ingestion Layer:** Reads unstructured market indicators (simulated via `fetch_raw_leads`).
2. **Qualification Layer:** Applies rule-based parameters to filter out simple low-value projects.
3. **AI Evaluation Layer:** Executes a prompt-engineered risk scoring model via GPT-4o-mini.

## 🚀 Quickstart Guide
1. Clone the repository: `git clone https://github.com`
2. Install dependencies: `pip install -r requirements.txt`
3. Set your API access token: `export GROQ_API_KEY="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"`
4. Run the pipeline: `python agent.py`
