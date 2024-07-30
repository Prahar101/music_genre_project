import streamlit as st
import httpx

def call_api(file):
    # Use localhost for local testing
    url = "https://rythmradar.azurewebsites.net/predict"
    headers = {"accept": "application/json"}

    files = {"file": (file.name, file.read(), "application/json")}
    try:
        response = httpx.post(url, headers=headers, files=files, timeout=None)
        
        return response.json()
    
    except httpx.RequestError as e:
        st.error(f"Error calling API: {e}")
        return None

def main():
    st.title("File Uploader and API Caller")

    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        st.write("You uploaded:", uploaded_file.name)
        if st.button("Call API"):
            api_response = call_api(uploaded_file)
            if api_response:
                pred = api_response.get("prediction", "No prediction returned")
                st.write(f"Prediction : {pred}")
        
if __name__ == "__main__":
    main()
