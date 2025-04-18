
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.query_enhancer import enhance_query
import streamlit as st
from utils.recommender import recommend_assessments

st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")

st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")
st.title("🧠 SHL Assessment Recommendation System")
st.write("Enter a job description or natural language query below to get suitable SHL assessments:")
query = st.text_area("💬 Job Description or Query", height=200)


if st.button("🔍 Get Recommendations"):
    if not query.strip():
        st.warning("Please enter a valid job description or query.")
    else:
        
        enhanced_query = enhance_query(query)
        st.info(f"🔎 Enhanced Query (Gemini): *{enhanced_query}*")

       
        results = recommend_assessments(enhanced_query)
        st.success(f"Found {len(results)} relevant assessments:")

        for i, item in enumerate(results, 1):
            st.markdown(f"""
            ### 🔹 Recommendation {i}
            - **Name:** [{item['name']}]({item['url']})
            - **Type:** {item['test_type']}
            - **Duration:** {item['duration']}
            - **Remote Testing:** {item['remote_testing']}
            - **Adaptive/IRT Support:** {item['adaptive_support']}
            """)


