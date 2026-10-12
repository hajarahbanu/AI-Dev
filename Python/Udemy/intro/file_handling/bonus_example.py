content = ["ulgo shipgi ana, svt right here", 
           "want to get more stamps on my passport", 
           "smooth like butter, like a criminal undercover"]

files = ["svt.txt", "cortis.txt", "bts.txt"]

for content, file in zip(content, files):
    with open(file, "w") as f:
        f.write(content)

