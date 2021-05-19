from PIL  import Image
img=Image.open("img.jpg")
blackAndWhite=img.convert('l')
blackAndWhite.save('bw_img.jpg')
blackAndWhite.show()
