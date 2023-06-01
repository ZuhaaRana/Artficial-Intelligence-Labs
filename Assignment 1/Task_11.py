


marks = {'AI':74,'CN':76,'DS':42,'PS':54}
sum = 0
for k, v in marks.items():
    sum += v

print(f"Sum of values: {sum}")

for k, v in marks.items():
    print(f"Key: {k} value: {v}")

maxx = max(marks.values())
sub = list(marks.keys())[list(marks.values()).index(maxx)]
print(f"Max Marks: {maxx} in Subject: {sub}")

minn = min(marks.values())
sub = list(marks.keys())[list(marks.values()).index(minn)]
print(f"Min Marks: {minn} in Subject: {sub}")
