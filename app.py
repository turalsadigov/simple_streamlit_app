import streamlit as st

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    st.title("Prime Number Checker")
    number = st.number_input("Enter a number:")
    
    if st.button("Check"):
        if is_prime(number):
            st.success(f"{number} is a prime number!")
        else:
            st.error(f"{number} is not a prime number.")

if __name__ == "__main__":
    main()
