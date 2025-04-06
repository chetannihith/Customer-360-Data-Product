# Customer 360 Data Product Designer

![Accenture Hackathon Banner](hackathon-v2-1741259267-png.jpg)  
*Submission for Accenture's "Hack the Future: A Gen AI Sprint Powered by Data"*

---

## Overview

**Customer 360 Data Product Designer** is an innovative multi-agent AI system designed to automate the creation of Customer 360 data products for retail banking customers. Built as part of the Accenture hackathon, this solution addresses **Problem Statement 6** by streamlining the process of understanding business use cases, designing data product structures, identifying source systems, generating attribute mappings, and certifying the final product—all with efficiency and accuracy.

Our system leverages local AI execution with **Ollama** and the **Phi-3 Mini** model, uses **YAML** for structured outputs to avoid JSON parsing issues, and incorporates **SQLite** for long-term memory to enhance performance over time.

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
- **Interactive UI**: Streamlit app provides a user-friendly interface.

---

## Tech Stack

| **Category**         | **Tool**         | **Purpose**                          |
|-----------------------|------------------|--------------------------------------|
| **Programming**       | Python           | Core development language           |
| **AI Model**          | Ollama (Phi-3 Mini) | Local LLM for reasoning tasks    |
| **Web Framework**     | Streamlit        | Interactive UI for demo             |
| **Data Format**       | YAML             | Structured output representation    |
| **Database**          | SQLite           | Long-term memory for use cases      |

---

## Installation

### Prerequisites
- **Python 3.8+**
- **Ollama**: Installed and running locally
- **System Requirements**: 8GB RAM (16GB recommended), 10GB free storage

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/chetannihith/customer360-data-product-designer.git
   cd customer360-data-product-designer
   ```

2. **Install Dependencies**:
   ```bash
   pip install streamlit ollama pyyaml
   ```

3. **Set Up Ollama**:
   ```bash
   ollama pull phi3:mini
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. **Launch the App**: Open your browser at `http://localhost:8501` after running the command above.
2. **Enter a Use Case**: Input a business use case (e.g., "Integrate customer demographics and transaction history to identify high-value customers").
3. **Generate Design**: Click "Generate Data Product Design" to see the system process the use case step-by-step.
4. **Export Results**: Download the YAML output for further use.

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
└── README.md               # Project documentation
```

---

## Hackathon Context

This project was developed for **Accenture's "Hack the Future: A Gen AI Sprint Powered by Data"** during Data and AI Week 2025. It aligns with Accenture’s emphasis on innovative AI solutions, leveraging their recommended tools (Ollama) and delivering a practical, scalable solution for retail banking.

**Team**: BMLians 
**Idea Title**: "Agentic Customer 360: AI-Powered Data Product Design for Retail Banking"

---

## Why We Stand Out

- **Efficiency**: Local execution with Ollama and lightweight YAML outputs reduce latency.  
- **Accuracy**: Phi-3 Mini’s reasoning capabilities and memory system ensure precise designs.  
- **Innovation**: YAML-based approach avoids JSON parsing errors, enhancing reliability.  
- **Impact**: Automates a critical banking process, saving time and enabling personalization.

---

## Acknowledgments

- **Accenture**: For hosting the hackathon and providing the problem statement.  
- **Ollama Team**: For enabling local AI model execution.  
- **Streamlit Community**: For an amazing UI framework.

---

*Thank you for exploring our solution! We hope it transforms how retail banks design Customer 360 data products.*
