from platform import python_version

ages = [21, 73, 43, 76, 23, 78,90,15] #list
names = ["Jane", "Jack", "Moha", "Rick"]
# functions
ages.append(31)
print(ages)
ages.sort()
ages.reverse()
print(ages)

names.sort()
print(names)
jack_count= names.count("Jack")
print(jack_count)
print(len(names))
print(len(ages))
print(sum(ages))
print(sum(ages)/len(ages))

print(names[-1])
print(names[-2])
print(names[:2])
print(names)
print(names[0])

# SETS
scores = {88, 78, 88, 65, 77, 78}
print(scores)
scores.add(90)
print(scores)
scores.remove(65)
print(scores)
scores.clear()
print(scores)

# TUPLES immutable
weekdays=("mon","tue","wed","thur","fri")
print(weekdays[0])

# DICTIONARY
person = {"name": "vee", "age":32, "height":1.88, "weight": 53}
print(person["name"])
print(person["age"])
print(person["height"])
print(person["weight"])

people =[
                  {"name": "vee", "age":32},
                 { "name": "joe", "age":33},
                 {"name": "john", "age":37}
                 ]
print(people)
print(people[0]["age"])

# ALGORITHMS
