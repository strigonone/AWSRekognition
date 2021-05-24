import boto3
from pprint import pprint
import Image_Reader

client = boto3.client('rekognition')

imgfile = 'ImageTest/GRB.jpg'

# grab the image from online
imgbytes = Image_Reader.get_image_from_file(imgfile)

rekresp = client.detect_labels(Image={'Bytes': imgbytes})

pprint(rekresp['Labels'])
# print('Here is what I detect in the image provided:')
# for label in rekresp['Labels']:
#     print(labezl['Name'])