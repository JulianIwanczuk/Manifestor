import streamlit as st
import streamlit_authenticator as stauth

# Load the configuration file containing user credentials
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create the authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Render the login form
name, authentication_status, username = authenticator.login('Login', 'sidebar')

# Check the authentication status
if authentication_status:
    # User is logged in
    st.write(f'Welcome, {name}!')
else:
    # User is not logged in
    st.error('Authentication failed.')
