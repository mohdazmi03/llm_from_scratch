
with open("raw.txt","r") as f:
    raw_text= f.read()

normal_text = raw_text.lower()

# replace manual 1 by 1
#clean_text = normal_text.replace(","," ").replace("."," ").replace("'"," ").replace("-"," ").replace("#"," ").replace(":"," ")
unwanted = ",.;:'/!#'"

for char in unwanted:
    normal_text = normal_text.replace(char," ")


clean_text = " ".join(normal_text.split())

with open("clean_data.txt","w") as f:
    f.write(clean_text)

with open("clean_data.txt","r") as f: 
    text = f.read()

split_text = list(text)


pairs = {}

print(split_text)


for i in range(len(split_text) - 1):
    pair = split_text[i] + split_text[i+1]

    if pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1

print(pairs)

# find max pair

max_count = 0
best_pair ={}
for item in pairs : 
    count = pairs[item]
    if count >= max_count:
        best_pair = item
        max_count = count

print(f"Best Pairs: {best_pair}")
print(f"Max Count: {max_count}")