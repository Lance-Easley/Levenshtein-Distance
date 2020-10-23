import pprint

# Levenshtein Distance
word1 = 'abcdef'
word2 = 'azc3uf'

word1_count = len(word1) + 1
word2_count = len(word2) + 1
mem = []

# Set memoize list length
for i in range(0, word1_count):
    mem.append([])
    for j in range(0, word2_count):
        mem[i].append(None)

# Assign empty string numbers to memoize chart
#   Row
for r in range(0, word1_count):
    mem[r][0] = r
#   Column
for c in range(0, word2_count):
    mem[0][c] = c

# Fill in rest of chart
for r in range(word1_count - 1):
    for c in range(word2_count - 1):
        str1 = word1[r]
        str2 = word2[c]
        if str1 == str2:
            mem[r + 1][c + 1] = mem[r][c]
        else:
            mem[r + 1][c + 1] = min(
                mem[r][c] + 1,
                mem[r + 1][c] + 1,
                mem[r][c + 1] + 1
            )

# Get last number in chart
Leven_dist = mem[-1][-1]

# Pretty Print
pprint.pprint(mem, indent= 4)
print(Leven_dist)