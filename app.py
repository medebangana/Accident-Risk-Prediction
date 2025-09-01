
ngrok.kill()

# Run Streamlit in background
get_ipython().system_raw('streamlit run app.py --server.port 8501 &')

# Expose public URL
public_url = ngrok.connect(8501)
print("Your app is live here:", public_url)
