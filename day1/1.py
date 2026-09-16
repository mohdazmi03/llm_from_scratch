# read and write text from local file

# Read text from a local file

with open("raw.txt","r") as f:
    raw_text = f.read()

print(f"This is the raw data :{raw_text}")


# Write data into file
sample_data = "This is a data to be saved to local file"

with open("write.txt","w") as f:
    f.write(sample_data)



# normalize and clean up data 

#raw.txt : This is a Simple Txt file which will be used to read, write           for llm data processing.

# Lowercase data
normalized_text = raw_text.lower()

#clean up data 
cleaned_text = normalized_text.replace("."," ").replace(","," ").replace("'"," ")

#remove extra white space
cleaned_text = " ".join(cleaned_text.split())

print(f"Cleaned Text : {cleaned_text}")

with open("cleanned.txt","w") as f:
    f.write(cleaned_text)


with open("cleanned.txt","r") as f:
    data = f.read()

print(f"sample cleaned and normalized data : {data}")
