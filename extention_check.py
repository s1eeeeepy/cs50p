filename = input("File name: ").lower().strip()
ext = filename.split(".")[-1]
exts = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

if ext in exts:
    print(exts[ext])
else:
    print("application/octet-stream")
