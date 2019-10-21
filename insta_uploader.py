from InstagramAPI import InstagramAPI
from os import getcwd

api = InstagramAPI('USERNAME','PASSWORD')
api.login()

image_path = getcwd()+'/image.jpg'
caption = 'test'

api.uploadPhoto(image_path,caption=caption)
print('my upload done')