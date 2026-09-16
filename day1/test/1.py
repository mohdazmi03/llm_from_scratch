

with open("raw.txt","r") as f:
    raw_data = f.read()

normalized_data = raw_data.lower()

cleaned_text = normalized_data.replace(","," ").replace("."," ").replace("'"," ")

cleaned_text = " ".join(cleaned_text.split())

with open("clean_data.txt","w") as f:
    f.write(cleaned_text)