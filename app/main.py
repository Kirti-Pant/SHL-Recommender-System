import streamlit as st
import requests

st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")

st.title("🧠 SHL Assessment Recommendation System")
st.write("Enter a job description or natural language query below to get suitable SHL assessments:")

query = st.text_area("💬 Job Description or Query", height=200)

if st.button("🔍 Get Recommendations"):
    if not query.strip():
        st.warning("Please enter a valid job description or query.")
    else:
        try:
            
            api_url = "https://shl-fastapi-efc6.onrender.com/recommend"


            
            response = requests.post(api_url, json={"query": query})

            if response.status_code == 200:
                results = response.json()
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
            else:
                st.error("Something went wrong with the API.")
        except Exception as e:
            st.error(f"Error contacting backend: {e}")


