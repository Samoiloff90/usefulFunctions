import os
images_path = r"./renameFiles"
image_list = os.listdir(images_path)
for i, image in enumerate(image_list):
    ext = os.path.splitext(image)[1]
    if ext == '.jpg':
        src = images_path + '/' + image
        dst = images_path + '/' + 'name-id_' + str(i) + '.jpg'
        os.rename(src, dst)