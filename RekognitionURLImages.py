import boto3
from pprint import pprint
import Image_Reader
import simplejson as json


client = boto3.client('rekognition')

imgurl = 'http://speedhunters-wp-production.s3.amazonaws.com/wp-content/uploads/2008/12/25090000/504img3.jpg'

# grab the image from online
imgbytes = Image_Reader.get_image_from_url(imgurl)

rekresp = client.detect_labels(Image={'Bytes': imgbytes})

data = json.dumps(rekresp)
jfile = open("AWSJsonData.json", "w")
jfile.write(data)
jfile.close()

pprint(rekresp['Labels'])
# print('Here is what I detect in the image provided:')
# for label in rekresp['Labels']:
#     print(label['Name'])