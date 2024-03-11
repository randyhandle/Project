''' used to download images '''

# from simple_image_download import simple_image_download as simp

# response = simp.simple_image_download

# keywords = ["shoes"]

# for k in keywords:
#     response().download(k,200)

""" used to train """

from ultralytics import YOLO

model = YOLO('yolov8m.pt')

output = model.train(data = "custom_data.yaml",epochs = 50 , imgsz = 640)

# print(output)
# print(output[0].numpy())



