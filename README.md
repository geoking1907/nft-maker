[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com)

# nft-maker

## How to
If you're going to use this program, change the pictures in the "images" folder. All images must be of the same resolution and size.
Add backgrounds to folder "b", faces to folder "f", glasses to folder "g", accessories to folder "h", and clothes to folder "t".
After that, you need to add your images to the images.py file. 

## Rarity
If you don't need images with different rarity, in the creator.py file, remove the weights=(...) attribute from random.choices. 
If you need images with different rarity, in the creator.py file add the weights=(...) attribute to random.choices, in which you specify the frequency of receiving each image (you need to specify the frequency in the order in which you specified the images in the images.py file)
