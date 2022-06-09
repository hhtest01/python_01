dct1 = {}
dct2 = {"a":1,"b":4,}
print(dct1)
print(dct2)

print(dct2["b"])

dct2["b"] = 31
print(dct2)

dct3 = {"r":33,"t":45}
dct2.update(dct3)
print(dct2)