# teams = ["giants","bills", "jets", "patriots"]

# for i in teams:
#     print(i.title())
# print("============================================")

# for team in teams:
#     print(team.title() + "!")
#     print("You're going to win the Super Bowl!\n")
# print("Go Football!!!")

# print("============================================")

# values = [1,2,3,4,5]
# total_sum = 0

# for value in values:
#     total_sum += value
# print(total_sum)

# print("============================================")

# triples = [["a","b","c","d"],["1","2","3","4"], ["do","re","mi","fa"]]

# for list_value in triples:
#     for element in list_value:
#         print(element, end=' ')
#     print("Just finished inner for loops")
# print("Now outside for loops")


values = range(1,10)
print(values)
print(type(values))

for i in range(1,11):
    print(i)

for num in range(5):
    print(num)
print("-----------------")
for i in range(2, 11, 2):
    print(i)

print("----------------")

numbers = list(range(10,101,10))
print(numbers)

for num in numbers:
    print(num)

squares = []
for num in numbers:
    square = num **2
    squares.append(square)
print("Populating squares")
for square in squares:
    print(square)
print("----------------")
cubes = [num**3 for num in numbers]
for cube in cubes:
    print(cube)
