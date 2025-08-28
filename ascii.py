import string
def lower():
    lower_case = string.ascii_lowercase
    for i in lower_case:
         print(f"{i} --> {ord(i)}")
def upper():
    upper_case = string.ascii_uppercase
    for i in upper_case:
         print(f"{i} --> {ord(i)}")

user_choice = int(input("""
Please choose an option to display alphabets with their ASCII values:
0 → UPPERCASE letters (A–Z with ASCII codes)
1 → lowercase letters (a–z with ASCII codes)
Your choice: 
"""))
if user_choice == 1:
    lower()
elif user_choice == 0:
    upper()
else:
    print("Please choose correct option")