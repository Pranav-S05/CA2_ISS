def find_cube_pairs(target):
    solutions = []                          # List to store valid pairs
    # The maximum number to check is the cube root of the target
    # This is because if a^3 + b^3 = target, then a and b must be less than or equal to the cube root of target
    max_num = round(target ** (1/3))  

    for a in range(1, max_num + 1):         # Looping through possible values of a
        for b in range(a, max_num + 1):     # Looping through possible values of b
            # Check if the sum of cubes of a and b equals the target
            if a**3 + b**3 == target:
                solutions.append((a, b))    # Adding the pair (a, b) to the solutions list if it is valid.
    return solutions

# The function returns all possible pairs of numbers such that a^3 + b^3 = target

pairs = find_cube_pairs(1729)       # All pairs of cubes that sum to 1729
print("Valid cube pairs for 1729:")
for a, b in pairs:                  # Iterating through the pairs a,b
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")
"""Submit your response here:  https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnlPbNUMFU2TjI1WjQyUlczSFNIOFBEWkxTQ0lFQS4u"""