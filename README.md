# Customer 360 Data Product Designer

![Accenture Hackathon Banner](hackathon-v2-1741259267-png.jpg)  
*Submission for Accenture's "Hack the Future: A Gen AI Sprint Powered by Data"*

---

## Overview

**Customer 360 Data Product Designer** is an innovative multi-agent AI system designed to automate the creation of Customer 360 data products for retail banking customers. Built as part of the Accenture hackathon, this solution addresses **Problem Statement 6** by streamlining the process of understanding business use cases, designing data product structures, identifying source systems, generating attribute mappings, and certifying the final product—all with efficiency and accuracy.

Our system leverages local AI execution with **Ollama** and the **Phi-3 Mini** model, uses **YAML** for structured outputs to avoid JSON parsing issues, and incorporates **SQLite** for long-term memory to enhance performance over time. For the hackathon demo, we’ve deployed the Streamlit app on Streamlit Community Cloud, using **ngrok** to expose the local Ollama instance.

---

## Problem Statement

**Problem Statement 6: Recommendation and Design of Customer 360 Data Product for Retail Banking Customers with Agentic Solution**  
- **Challenge**: Create a multi-agent solution to:  
  - Understand specific business use cases.  
  - Recommend target data product structures.  
  - Identify source systems and attributes.  
  - Map source-to-target attributes.  
  - Define ingress/egress processes and certify the data product against standards.  
- **Goal**: Automate a traditionally manual, error-prone process to deliver a unified customer view for retail banking, enabling personalized services.

---

## Features

- **Multi-Agent Architecture**: Five specialized agents collaborate seamlessly:  
  - **Use Case Analyst**: Extracts key requirements from business use cases.  
  - **Data Product Designer**: Designs the target data product structure in YAML.  
  - **Source Identifier**: Identifies source systems and attributes.  
  - **Mapping Generator**: Creates source-to-target attribute mappings.  
  - **Certification Agent**: Certifies the data product with ingress/egress details.  
- **Local AI Execution**: Uses Ollama with Phi-3 Mini for fast, private processing.  
- **YAML-Based Outputs**: Ensures consistent, error-free data representation.  
- **Memory System**: SQLite database stores past use cases for reuse and learning.  
- **Interactive UI**: Streamlit app provides a user-friendly interface, deployed on Streamlit Community Cloud with ngrok for remote access to local Ollama.

---

## Tech Stack

| **Category**         | **Tool**         | **Purpose**                          |
|-----------------------|------------------|--------------------------------------|
| **Programming**       | Python           | Core development language           |
| **AI Model**          | Ollama (Phi-3 Mini) | Local LLM for reasoning tasks    |
| **Web Framework**     | Streamlit        | Interactive UI for demo             |
| **Data Format**       | YAML             | Structured output representation    |
| **Database**          | SQLite           | Long-term memory for use cases      |
| **Exposure Tool**     | ngrok            | Exposes local Ollama to the internet|
| **Containerization**  | Docker           | Used locally for running Ollama     |

---

## Hackathon Deployment

For the hackathon demo, we’ve deployed the Streamlit app on Streamlit Community Cloud, with Ollama running locally and exposed via ngrok. This allows the cloud-deployed app to access the local Ollama instance securely.

### Prerequisites
- **Python 3.8+**
- **Docker**: For running Ollama locally (optional, if not using direct installation)
- **ngrok**: To expose local Ollama to the internet
- **GitHub Account**: For deploying the Streamlit app from your repository

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/chetannihith/customer360-data-product-designer.git
   cd customer360-data-product-designer
   ```

2. **Install Dependencies**:
   ```bash
   pip install streamlit requests pyyaml
   ```

3. **Set Up Ollama Locally**:
   - Option 1: Run Ollama directly:
     ```bash
     ollama pull phi3:mini
     ollama serve
     ```
   - Option 2: Use Docker (if you’ve pushed your image to Docker Hub):
     ```bash
     docker run -d -p 11434:11434 yourusername/yourimage:tag
     ```

4. **Expose Ollama with ngrok**:
   - Download and install ngrok from [ngrok.com](https://ngrok.com).
   - Run:
     ```bash
     ngrok http 11434
     ```
   - Copy the ngrok URL (e.g., `https://abc123.ngrok.io`).

5. **Update the Streamlit App**:
   - In `app.py`, set `OLLAMA_URL` to your ngrok URL:
     ```python
     OLLAMA_URL = "https://abc123.ngrok.io/api/chat"
     ```

6. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Configured for ngrok and Streamlit Cloud"
   git push origin main
   ```

7. **Deploy to Streamlit Community Cloud**:
   - Sign in to [streamlit.io/cloud](https://streamlit.io/cloud).
   - Create a new app from your GitHub repository (`chetannihith/customer360-data-product-designer`).
   - Set `app.py` as the entry point and deploy.

8. **Run the Demo**:
   - Keep Ollama and ngrok running locally.
   - Share the Streamlit Cloud URL with the judges.

---

## Usage

1. **Access the App**: Visit the Streamlit Cloud URL (e.g., `https://your-app-name.streamlit.app`).
2. **Enter a Use Case**: Input a business use case (e.g., "Integrate customer demographics and transaction history to identify high-value customers").
3. **Generate Design**: Click "Generate Data Product Design" to see the system process the use case step-by-step.
4. **View Results**: The app will display requirements, data product structure, source systems, attribute mappings, and certification details.

### Sample Use Case
**Input**:  
"Integrate customer demographics (name, age) and transaction history (date, amount) to identify high-value customers."

**Output**:  
- **Requirements**: "Integrate customer demographics (name, age) and transaction history (date, amount) for high-value customer identification."
- **Data Product Structure** (YAML):  
  ```yaml
  Customer360:
    tables:
      - name: Customer_Demographics
        attributes:
          - name: customer_id
            type: string
          - name: name
            type: string
          - name: age
            type: integer
      - name: Transaction_History
        attributes:
          - name: customer_id
            type: string
          - name: transaction_date
            type: date
          - name: amount
            type: float
  ```
- **Source Systems** (YAML): *See full code output for details.*
- **Mappings** (YAML): *See full code output for details.*
- **Certification**: "Ingress: Daily ETL at 2 AM UTC. Egress: REST API with RBAC. GDPR-compliant."

---

## Project Structure

```
customer360-data-product-designer/
├── app.py                  # Main Streamlit application
├── agents/                 # Agent modules
│   ├── __init__.py         # Empty init file
│   ├── use_case_analyst.py # Analyzes use cases
│   ├── data_product_designer.py # Designs data product structure
│   ├── source_identifier.py # Identifies source systems
│   ├── mapping_generator.py # Generates attribute mappings
│   └── certification_agent.py # Certifies the data product
├── customer360_memory.db   # SQLite database for memory
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Hackathon Context

This project was developed for **Accenture's "Hack the Future: A Gen AI Sprint Powered by Data"** during Data and AI Week 2025. It aligns with Accenture’s emphasis on innovative AI solutions, leveraging their recommended tools (Ollama) and delivering a practical, scalable solution for retail banking.

**Team**: BMLians  
**Idea Title**: "Agentic Customer 360: AI-Powered Data Product Design for Retail Banking"

---

## Why We Stand Out

- **Efficiency**: Local Ollama execution with ngrok ensures fast, private processing while enabling cloud deployment.  
- **Accuracy**: Phi-3 Mini’s reasoning capabilities and memory system ensure precise designs.  
- **Innovation**: YAML-based approach avoids JSON parsing errors, enhancing reliability.  
- **Impact**: Automates a critical banking process, saving time and enabling personalization.

---

## Acknowledgments

- **Accenture**: For hosting the hackathon and providing the problem statement.  
- **Ollama Team**: For enabling local AI model execution.  
- **Streamlit Community**: For an amazing UI framework.  
- **ngrok**: For seamless exposure of local services to the cloud.

---

*Thank you for exploring our solution! We hope it transforms how retail banks design Customer 360 data products.*
