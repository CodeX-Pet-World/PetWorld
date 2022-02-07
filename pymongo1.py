import pymongo
from pymongo import MongoClient
import base64
import os
# def upload_image(text, filename, username, email):
#     from pymongo import MongoClient
#     from PIL import Image
#     import io
#     client = MongoClient("mongodb+srv://codex:1234@cluster0.hmhik.mongodb.net/codex?retryWrites=true&w=majority")
#     mydb=client["codex"]
#     mycol = mydb["user_posts"]
#     im = Image.open("./static/"+filename)
#     image_bytes = io.BytesIO()
#     im.save(image_bytes, format='JPEG')
#     image = {
#         "username": username,
#         "email" : email, 
#         'images': image_bytes.getvalue(),
#         "text": text,
#     }
#     mycol.insert_one(image)
#     os.remove("./static/"+filename)


# def get_image(email, filename):
#     from pymongo import MongoClient
#     from bson.binary import Binary
#     from PIL import Image
#     import io
#     import matplotlib.pyplot as plt
#     import shutil, os

#     client = MongoClient("mongodb+srv://codex:1234@cluster0.hmhik.mongodb.net/codex?retryWrites=true&w=majority")
#     mydb=client["codex"]
#     mycol = mydb["user_posts"]
#     image = mycol.find()
#     list_text = []
#     for i in image:
#         if email==i["email"]:
#             pil_img = Image.open(io.BytesIO(i['images']))
#             pil_img.save(filename)
#             shutil.move(filename, "static/")
#             os.remove("./"+filename)
#             list_text.append(i["text"])
#     return (email, i["username"], list_text)





def get_data(email, passwd): 
    client = MongoClient("mongodb+srv://testing:12345@cluster0.zzqka.mongodb.net/test?retryWrites=true&w=majority")
    mydb=client["test"]
    mycol = mydb["credentials"]
    y = mycol.find()
    for data in y:
        if data["email"] == email:
            if data["password"]==passwd:
                return True
            
def signup(username, email, password):
    client = MongoClient("mongodb+srv://testing:12345@cluster0.zzqka.mongodb.net/test?retryWrites=true&w=majority")
    mydb = client["test"]
    mycol = mydb["credentials"]
    user_data= {"username":username,"password":password,"email":email}
    mycol.insert_one(user_data)

