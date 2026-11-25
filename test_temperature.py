from temperature import Temperature

c = Temperature(1.0, "c")
k = Temperature(0.0, "K")
f = Temperature(0.0, "f")

print(c)
print(c.convert_to("k"))
print(c.convert_to("F"))
print(c.convert_to("c"))

print(c < k)

