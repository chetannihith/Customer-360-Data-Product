import streamlit as st
import sqlite3
import yaml
from agents.use_case_analyst import UseCaseAnalyst
from agents.data_product_designer import DataProductDesigner
from agents.source_identifier import SourceIdentifier
from agents.mapping_generator import MappingGenerator
from agents.certification_agent import CertificationAgent

# Initialize model
MODEL_NAME = "phi3:mini"

# Set up SQLite database
conn = sqlite3.connect("customer360_memory.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS use_cases
             (use_case TEXT, data_product_structure TEXT, mapping TEXT)''')
conn.commit()

# Initialize agents
use_case_analyst = UseCaseAnalyst(MODEL_NAME)
data_product_designer = DataProductDesigner(MODEL_NAME)
source_identifier = SourceIdentifier(MODEL_NAME)
mapping_generator = MappingGenerator(MODEL_NAME)
certification_agent = CertificationAgent(MODEL_NAME)

def check_memory(use_case):
    """Check if a similar use case exists in memory."""
    c.execute("SELECT data_product_structure, mapping FROM use_cases WHERE use_case=?", (use_case,))
    result = c.fetchone()
    return (result[0], result[1]) if result else (None, None)

def save_to_memory(use_case, data_product_structure, mapping):
    """Save use case results to memory."""
    c.execute("INSERT INTO use_cases VALUES (?, ?, ?)", 
              (use_case, data_product_structure, mapping))
    conn.commit()

def main():
    st.title("Customer 360 Data Product Designer for Retail Banking")

    # Input section
    st.markdown("### Enter Your Business Use Case")
    use_case = st.text_area("Describe the business use case for the Customer 360 data product:")

    if st.button("Generate Data Product Design"):
        progress = st.progress(0)

        # Check memory
        st.markdown("### Checking Past Use Cases")
        with st.spinner("Searching memory..."):
            past_structure, past_mapping = check_memory(use_case)
            progress.progress(20)
            if past_structure and past_mapping:
                st.success("Similar use case found in memory. Using past insights.")
                data_product_structure, mapping = past_structure, past_mapping
            else:
                st.info("No similar use case found. Designing anew.")

                # Step 1: Analyze use case
                st.markdown("### Step 1: Use Case Requirements")
                with st.spinner("Analyzing use case..."):
                    requirements = use_case_analyst.analyze(use_case)
                st.write(requirements)
                progress.progress(40)

                # Step 2: Design data product
                st.markdown("### Step 2: Data Product Structure")
                with st.spinner("Designing data product..."):
                    data_product_structure = data_product_designer.design(requirements)
                st.code(data_product_structure, language="yaml")
                progress.progress(60)

                # Step 3: Identify sources
                st.markdown("### Step 3: Source Systems and Attributes")
                with st.spinner("Identifying sources..."):
                    source_info = source_identifier.identify(data_product_structure)
                st.code(source_info, language="yaml")
                progress.progress(80)

                # Step 4: Generate mapping
                st.markdown("### Step 4: Attribute Mapping")
                with st.spinner("Generating mapping..."):
                    mapping = mapping_generator.generate(source_info, data_product_structure)
                st.code(mapping, language="yaml")
                progress.progress(90)

                # Save to memory
                save_to_memory(use_case, data_product_structure, mapping)

        # Step 5: Certify data product
        st.markdown("### Step 5: Certification")
        with st.spinner("Certifying data product..."):
            certification_details = certification_agent.certify(data_product_structure)
        st.write(certification_details)
        progress.progress(100)

        # Export option
        if st.button("Export Results as YAML"):
            results = f"""use_case: {use_case}
data_product_structure:
{data_product_structure}
mapping:
{mapping}
certification: {certification_details}"""
            st.download_button("Download YAML", data=results, file_name="customer360_results.yaml")

if __name__ == "__main__":
    main()
