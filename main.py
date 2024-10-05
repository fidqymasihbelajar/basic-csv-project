from datetime import datetime

name_input = str(input("Enter your full name: "))
idnumber_input = int(input("Enter your badge number: "))
job_function_input = str(input("Enter your Job Function: "))

record = {
    'Name': name_input,
    'Badge Number': idnumber_input,
    'Job Function': job_function_input,
    'Timestamp': datetime.now()
}

print(record)