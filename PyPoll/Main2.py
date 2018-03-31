
from collections import defaultdict

names = ["mark", "john", "mark", "fred", "paul", "john"]

d = defaultdict(int)
for name in names:
	d[name] += 1
print(d)