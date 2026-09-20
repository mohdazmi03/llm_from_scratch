
#read file from local txt

with open("raw.txt","r") as f:
    raw_data = f.read()

normalize_raw = raw_data.lower()

unwanted = {",",".","'","`"}

for item in unwanted:
    normalize_raw = normalize_raw.replace(item," ")

clean_data = " ".join(normalize_raw.split())

split_data = list(clean_data)

i = 0
pairs = {}
while i < len(split_data)-1:
    pair = split_data[i]+split_data[i+1]
    if pair in pairs :
        pairs[pair] += 1
        i += 1

    else:
        pairs[pair] = 1
        i += 1

#find best pair and max count of it 
print(pairs)

max_count = 0
best_pairs = {}
for item in pairs:
    if pairs[item] > max_count:
        best_pairs = item
        max_count = pairs[item]

print(f"Best Pairs : {best_pairs}")
print(f"Max Count : {max_count}")

new_tokens = []
i = 0

while i < len(split_data):

    if i < len(split_data)-1:
        new_pair = split_data[i]+ split_data[i+1]
    else:
        new_pair = split_data[i]
    if new_pair == best_pairs and i < len(split_data) - 1:
        new_tokens.append(best_pairs)
        i += 2
    else: 
        new_tokens.append(split_data[i])
        i += 1

print(f"New Tokens: {new_tokens}")