# This constructs a dictionary type, which is a key-value pair construct like a HashMap in java or C#
# The nice thing about these is that you can define them as json literals
tel = {'jack': 4098, 'sape': 4139}

print(tel)

tel['guido'] = 4127

print(tel)

del tel['sape']

print(tel)

tel['irv'] = 4127

print(tel)

# Tests for the existence of a key
print('guido' in tel)

print('jack' not in tel)

# Prints all the keys in the dictionary
print(tel.keys())

# Prints all the values in the dictionary
print(tel.values())

# Looping construct for dictionary
# The key will be stored in k, the value in v
for k, v in tel.items():
    print(k, v)



