import streamlit as st

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    st.title("Prime Number Finder")
    st.write("This app finds prime numbers within a specified range.")

    start_num = st.number_input("Enter the start of the range:", min_value=1, max_value=100, step=1, value=1)
    end_num = st.number_input("Enter the end of the range:", min_value=start_num, max_value=100, step=1, value=10)

    prime_numbers = [num for num in range(start_num, end_num + 1) if is_prime(num)]

    st.write("Prime numbers within the specified range:")
    st.write(prime_numbers)

if __name__ == "__main__":
    main()
