import boto3
from pprint import pprint
import Image_Reader
import json

client = boto3.client('rekognition')

imgfile = 'ImageTest/subaruwrc.jpg'

# Grabs the image locally
imgbytes = Image_Reader.get_image_from_file(imgfile)

rekresp = client.detect_labels(Image={'Bytes': imgbytes})

data = json.dumps(rekresp)
jfile = open("AWSJsonData.json", "w")
jfile.write(data)
jfile.close()

pprint(rekresp['Labels'])
# print('Here is what I detect in the image provided:')
# for label in rekresp['Labels']:
#     print(labezl['Name'])