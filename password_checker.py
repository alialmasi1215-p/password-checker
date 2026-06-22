def check_password(password:str):
    with open("passwords.text","r") as file:
        common_pass: list[str] =  file.read().splitlines()
    for i, common in enumerate(common_pass,start=1):
        if common == password:
            print(f"{password}  : (# {i})")
            return
    print("Ok")

if __name__ == "__main__":
    user_pass:str = input("enter your password")
    check_password(user_pass)