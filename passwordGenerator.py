import streamlit as st
import random
import string
# import pyperclip

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
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    length = len(password)
    has_digit = any(char.isdigit() for char in password)
    has_letter = any(char.isalpha() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    if length >= 10 and has_digit and has_letter and has_special:
        return "Strong"
    elif length >= 6 and has_digit and has_letter:
        return "Good"
    else:
        return "Weak"

st.title("Password Generator")

length = st.slider("Select Password Length", min_value=4, max_value=20, value=8)
use_numbers = st.checkbox("Include Numbers", value=True)
use_characters = st.checkbox("Include Special Characters", value=True)
use_alphabets = st.checkbox("Include Alphabets", value=True)

generate = st.button("Generate Password")

if "password" not in st.session_state:
    st.session_state.password = ""

if generate:
    st.session_state.password = generate_password(length, use_numbers, use_characters, use_alphabets)

password = st.text_input("Generated Password", st.session_state.password)
password_strength = check_password_strength(password)
st.write(f"Password Strength: **{password_strength}**")

# if st.button("Copy to Clipboard"):
 #   pyperclip.copy(password)
 #  st.success("Password copied to clipboard!")
