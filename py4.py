
students = ("Minal", "janhavi", "Pranita", "pragati", "bhavishya")

print("Second student:", students[1])

is_alice_present = "Minal" in students
print("Is 'Minal' in the tuple?", is_alice_present)

new_students = ("Minal", "janhavi", "Pranita")
all_students = students + new_students


print("Final list of students:", all_students)
print("Total number of students:", len(all_students))
