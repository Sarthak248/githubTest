# TLE '17 Contest 7 P1 - Stargazing

n = int(input())
no_of_planets = n
i = 0

AllPlanets = [[1, 0, 0, 0]]

while i < (n-1):
    AllPlanets.append([])
    p, x, y = input().split()
    # AllPlanets[i + 1].append(i+2)
    AllPlanets[i + 1].append(int(p))
    AllPlanets[i + 1].append(int(x))
    AllPlanets[i + 1].append(int(y))
    i = i + 1

list_of_tuples = [(0, 0)]

j = 1 # starting from the third planet because planets 1 and 2 are already defined
while j < n:
    temp = AllPlanets[j][0] - 1    # first column "P" starting from planet 3 --- 2 - 1 = 1

    AllPlanets[j][1] = AllPlanets[j][1] + AllPlanets[temp][1]  # X coordinate of 3rd planet = 3 + 7 = 10
    AllPlanets[j][2] = AllPlanets[j][2] + AllPlanets[temp][2]  # Y coordinate of 3rd planet = 2 + 8 =10

    list_of_tuples.append((AllPlanets[j][1], AllPlanets[j][2]))
    j = j + 1

# print("List of tuples is ", list_of_tuples)
# print("SET  of tuples is ", set(list_of_tuples))
print(len(set(list_of_tuples)))
# print(no_of_planets)
