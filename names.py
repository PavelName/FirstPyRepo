from tests import formated_name
print("Enter'q' at any time to quit")
while True:
    first = input("\nPleas give me s first name:")
    if first == 'q':
        break
    last = input("\nPleas give me a last name")
    if last == 'q':
        break
    
    total_name = formated_name(first, last)
    print(f"\tNeatly formated name:{total_name}")