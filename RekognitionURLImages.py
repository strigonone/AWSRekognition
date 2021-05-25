import boto3
from pprint import pprint
import Image_Reader
import simplejson as json


client = boto3.client('rekognition')

imgurl = 'https://media.wired.com/photos/59371bdcbef1fc4e58f947fc/master/w_2560%2Cc_limit/walmart-advanced-vehicle-experience-wave-concept-truck.jpg'

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