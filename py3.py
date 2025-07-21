from datetime import datetime
first_name = "Minal"
last_name = "Suryawanshi"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

item = "Headphones"
price = 49.99
formatted_string = f"The price of {item} is ${price}"
print(formatted_string)

text = "hello world"
upper_text = text.upper()
print("Uppercase Text:", upper_text)

words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)
print("Joined Sentence:", sentence)

today = datetime.today()
formatted_date = today.strftime("%d-%m-%Y")
print("Today's Date:", formatted_date)
