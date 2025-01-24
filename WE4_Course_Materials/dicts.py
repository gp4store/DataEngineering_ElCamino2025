
"""Dictionary Comprehnsions"""

d = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

a = {k: v for k, v in d.items()}
print(a)

"""Dosen't matter what letter you use, it's a key variable in the dict"""
print({k for k in d})

print({v for v in d})
#
print({d for d in d})
#
"""Iterate over values in a dict"""
print({v for v in d.values()})

print({k for k in d.values()})

print({v for v in d.values()})

print({d for d in d.values()})