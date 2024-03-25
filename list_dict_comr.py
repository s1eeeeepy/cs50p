text = input(">>> ")
faces = {":)": "smile", ":(": "sad"}
keys = [key for key in faces.keys()]

for key in keys:
    if key in text:
        text = text.replace(key, faces[key])

print(text)
