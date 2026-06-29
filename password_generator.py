import random as rd
import string as st
characters = st.ascii_letters + st.digits + st.punctuation
generated_psd = []
def generate_password(no_of_psd,psd_length,):
    for i in range(no_of_psd):
        password = ""
        for j in range(psd_length):
            password += rd.choice(characters)
        generated_psd.append(password)
    return generated_psd
def main():
    count=1
    while True:
        try:
            no_of_psd = int(input("How many passwords do you want to generate? "))
            psd_length = int(input("How many characters per password? "))
            if no_of_psd <= 0 or psd_length <= 0:
                print('Both values should be  greater than Zero')
                continue
            break
        except ValueError:
            if count >=3:
                print('You have exceeded the number of trials')
                exit()
            print("Please enter a valid numbers only.")
            print('-'*30)
            count+=1
            
    generated_passwords = generate_password(no_of_psd, psd_length)

    print(f"\nGenerated {len(generated_passwords)} password(s):")
    for password in generated_passwords:
        print(f"[{password}]")
if __name__ ==  "__main__":
    main()
    

