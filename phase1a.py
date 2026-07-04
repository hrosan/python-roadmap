a = "hello"
b = "hel" + "lo"    # constructed at runtime
print(a is b)       # may be False

print(int("10.5"))
print(int(float("10.5")))