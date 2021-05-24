import requests


# Get Raw image data via url
def get_image_from_url(imgurl):
    resp = requests.get(imgurl)
    imgbytes = resp.content
    return imgbytes

# Grabbing a image file directly
def get_image_from_file(filename):

    with open(filename, 'rb') as imgfile:
        return imgfile.read()