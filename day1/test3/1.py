

with open("raw.txt","r") as f:
    raw_data = f.read()

normalize_data = raw_data.lower()




unwanted = {",",".",";","'"}
for char in unwanted:
    normalize_data = normalize_data.replace(char," ")

clean_data = " ".join(normalize_data.split())

print(clean_data)

split_data = list(clean_data)


pairs= {}
for i in range(len(split_data)-1):
    pair = split_data[i]+split_data[i+1]
    if pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1

print(pairs)

max_count = 0 
for item in pairs:
    count = pairs[item]
    if count >= max_count:
        max_count = count
        best_pairs = item

print(f"Best Pair : {best_pairs}")
print(f"Max count : {max_count}")

new_tokens = []
i = 0
while i < (len(split_data)):
    if i < len(split_data)-1 and split_data[i]+split_data[i+1] == best_pairs:
        new_tokens.append(best_pairs)
        i = i + 2
    else:
        new_tokens.append(split_data[i])
        i += 1

print(f"New Tokens :{new_tokens}")