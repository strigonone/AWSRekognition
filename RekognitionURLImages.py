import boto3
from pprint import pprint
import Image_Reader

client = boto3.client('rekognition')

imgurl = 'http://speedhunters-wp-production.s3.amazonaws.com/wp-content/uploads/2008/12/25090000/504img3.jpg'

# grab the image from online
imgbytes = Image_Reader.get_image_from_url(imgurl)

rekresp = client.detect_labels(Image={'Bytes': imgbytes})

pprint(rekresp['Labels'])
# print('Here is what I detect in the image provided:')
# for label in rekresp['Labels']:
#     print(labezl['Name'])