import streamlit as st
import sqlite3
import yaml
import ollama  # Original local execution used the ollama client
from agents.use_case_analyst import UseCaseAnalyst
from agents.data_product_designer import DataProductDesigner
from agents.source_identifier import SourceIdentifier
from agents.mapping_generator import MappingGenerator
from agents.certification_agent import CertificationAgent

# ngrok URL for cloud run compatibility
OLLAMA_URL = "https://d9c7-103-139-190-234.ngrok-free.app/"

# SQLite setup (unchanged from original)
conn = sqlite3.connect("customer360_memory.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS use_cases
             (use_case TEXT, data_product_structure TEXT, mapping TEXT)''')
conn.commit()

# Initialize agents with the ngrok URL
use_case_analyst = UseCaseAnalyst(OLLAMA_URL)
data_product_designer = DataProductDesigner(OLLAMA_URL)
source_identifier = SourceIdentifier(OLLAMA_URL)
mapping_generator = MappingGenerator(OLLAMA_URL)
certification_agent = CertificationAgent(OLLAMA_URL)

def check_memory(use_case):
    c.execute("SELECT data_product_structure, mapping FROM use_cases WHERE use_case=?", (use_case,))
    result = c.fetchone()
    return (result[0], result[1]) if result else (None, None)

def save_to_memory(use_case, data_product_structure, mapping):
    c.execute("INSERT INTO use_cases VALUES (?, ?, ?)", 
              (use_case, data_product_structure, mapping))
    conn.commit()

def main():
    st.title("Customer 360 Data Product Designer for Retail Banking")
    use_case = st.text_area("Enter Your Business Use Case:")
    if st.button("Generate Data Product Design"):
        progress = st.progress(0)
        past_structure, past_mapping = check_memory(use_case)
        if past_structure and past_mapping:
            st.success("Found in memory!")
            data_product_structure, mapping = past_structure, past_mapping
        else:
            st.write("Designing anew...")
            requirements = use_case_analyst.analyze(use_case)
            st.markdown("### Requirements")
            st.write(requirements)
            progress.progress(20)

            data_product_structure = data_product_designer.design(requirements)
            st.markdown("### Data Product Structure")
            st.code(data_product_structure, language="yaml")
            progress.progress(40)

            source_info = source_identifier.identify(data_product_structure)
            st.markdown("### Source Systems")
            st.code(source_info, language="yaml")
            progress.progress(60)

            mapping = mapping_generator.generate(source_info, data_product_structure)
            st.markdown("### Attribute Mapping")
            st.code(mapping, language="yaml")
            progress.progress(80)

            save_to_memory(use_case, data_product_structure, mapping)

        certification_details = certification_agent.certify(data_product_structure)
        st.markdown("### Certification")
        st.write(certification_details)
        progress.progress(100)

if __name__ == "__main__":
    main()