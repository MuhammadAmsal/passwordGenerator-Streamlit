import streamlit as st
import random
import string
# import pyperclip

generated_passwords = set()

def generate_password(length, use_numbers, use_characters, use_alphabets):
    characters = ""
    if use_numbers:
        characters += string.digits
    if use_characters:
        characters += string.punctuation
    if use_alphabets:
        characters += string.ascii_letters
    
    if not characters:
        return "Please select at least one option"
    
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if password not in generated_passwords:
            generated_passwords.add(password)
            return password

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in "!@#$%^&*" for char in password):
        score += 1
    if len(password) >= 12:
        score += 1
    
    if score == 5:
        return "Strong"
    elif 3 <= score <= 4:
        return "Moderate"
    else:
        return "Weak"

def provide_feedback(password):
    strength = check_password_strength(password)
    if strength == "Weak":
        return "Try making your password at least 8 characters long, including uppercase letters, numbers, and special characters."
    elif strength == "Moderate":
        return "Good password! Consider adding more length or special characters for extra security."
    else:
        return "Your password is strong! Well done."

st.title("Password Generator")

length = st.slider("Select Password Length", min_value=4, max_value=20, value=8)
use_numbers = st.checkbox("Include Numbers", value=True)
use_characters = st.checkbox("Include Special Characters", value=True)
use_alphabets = st.checkbox("Include Alphabets", value=True)

generate = st.button("Generate Password")

if "password" not in st.session_state:
    st.session_state.password = ""
    st.session_state.previous_passwords = set()

if generate:
    new_password = generate_password(length, use_numbers, use_characters, use_alphabets)
    st.session_state.password = new_password
    st.session_state.previous_passwords.add(new_password)

password = st.text_input("Generated Password", st.session_state.password)
password_strength = check_password_strength(password)
st.write(f"Password Strength: **{password_strength}**")
st.write(provide_feedback(password))

# if st.button("Copy to Clipboard"):
 #   pyperclip.copy(password)
 #  st.success("Password copied to clipboard!")
