

def who_is_next(names, r):
    # your code
    if (r - 1) <= len(names):
        return names[r - 1]
    else:
        return names[( r - 1 ) % len(names)]


names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
print(who_is_next(names, 5554))
print(len(names))
print(names[1])