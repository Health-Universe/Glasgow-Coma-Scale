import streamlit as st

def calculate_gcs(eye_response, verbal_response, motor_response):
    return eye_response + verbal_response + motor_response

st.title('Glasgow Coma Scale (GCS) Calculator')

st.header('Please select the scores for each component:')

# GCS Component Options
eye_response_options = {
    'No eye opening': 1,
    'Eye opening to pain': 2,
    'Eye opening to verbal command': 3,
    'Spontaneous eye opening': 4
}

verbal_response_options = {
    'No verbal response': 1,
    'Incomprehensible sounds': 2,
    'Inappropriate words': 3,
    'Confused': 4,
    'Oriented': 5
}

motor_response_options = {
    'No motor response': 1,
    'Extension to pain': 2,
    'Flexion to pain': 3,
    'Withdrawal from pain': 4,
    'Localizes pain': 5,
    'Obeys commands': 6
}

# Streamlit SelectBox for each component
eye_response = st.selectbox('Eye Response', options=list(eye_response_options.keys()))
verbal_response = st.selectbox('Verbal Response', options=list(verbal_response_options.keys()))
motor_response = st.selectbox('Motor Response', options=list(motor_response_options.keys()))

# Calculate GCS score
if st.button('Calculate GCS Score'):
    total_gcs = calculate_gcs(
        eye_response_options[eye_response],
        verbal_response_options[verbal_response],
        motor_response_options[motor_response]
    )
    st.success(f'The total GCS score is: {total_gcs}')

# Display Interpretation
if st.button('Interpret GCS Score'):
    if total_gcs <= 8:
        st.warning('Severe brain injury (GCS ≤ 8)')
    elif total_gcs <= 12:
        st.warning('Moderate brain injury (9 ≤ GCS ≤ 12)')
    else:
        st.success('Mild brain injury (GCS ≥ 13)')
