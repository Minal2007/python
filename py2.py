
A = frozenset([10, 20, 30, 40])
B = frozenset([30, 40, 50, 60])

# Union
union_set = A.union(B)
print("Union:", union_set)

# Intersection
intersection_set = A.intersection(B)
print("Intersection:", intersection_set)

# Difference (A - B)
difference_set = A.difference(B)
print("Difference (A - B):", difference_set)

# Symmetric Difference (A ^ B)
symmetric_diff_set = A.symmetric_difference(B)
print("Symmetric Difference:", symmetric_diff_set)

# Superset check
is_superset = A.issuperset({10, 20})
print("Is A a superset of {10, 20}?", is_superset)

try:
    A.add(70)
except AttributeError as e:
    print("Error while trying to add to frozenset A:", e)

# Length of A and B
print("Length of A:", len(A))
print("Length of B:", len(B)) 