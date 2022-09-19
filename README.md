

# Stable Diffusion in Tensorflow / Keras

> Now supports Older Tensorflow Versions (< 2.8)

#### Original [repo](https://github.com/divamgupta/stable-diffusion-tensorflow) by [Divam Gupta](https://github.com/divamgupta/)
#### Backward [compatibility fixes](https://github.com/ypeleg/stable-diffusion-tensorflow) by [Yam Peleg](https://github.com/ypeleg) 


A Keras / Tensorflow implementation of Stable Diffusion Models for Image Generation. This is a fork of the original repo, that now supports past versions of Tensorflow and Keras.
This implementation is easy to understand and have a minimal code footprint.
The weights had been converted from the original Pytorch implementation, and are available for download. (Automaticly downloaded when running the code) 


## Usage

_____

#### Command Line 

```
python text2image.py --prompt = "An astronaut riding a horse."
```

_____

#### Python

```
from stable_diffusion_tf.stable_diffusion import get_model, text2image
text_encoder, diffusion_model, decoder = get_model(512, 512, download_weights=True)

img = text2image("An astronaut riding a hourse" , 
	img_height=512, 
	img_width=512,  
	text_encoder=text_encoder, 
	diffusion_model=diffusion_model, 
	decoder=decoder
)

cv2.imwrite("/tmp/a.png" , img[0][... , ::-1])

```
_____

## Example Outputs 

The following outputs have been generated using the Tensorflow/Keras of stable diffusion:

1) *An epic and beautiful rococo werewolf drinking coffee, in a burning coffee shop. ultra-detailed. anime, pixiv, uhd 8k cryengine, octane render*

![a](https://user-images.githubusercontent.com/1890549/190841598-3d0b9bd1-d679-4c8d-bd5e-b1e24397b5c8.png)


2) *Spider-Gwen Gwen-Stacy Skyscraper Pink White Pink-White Spiderman Photo-realistic 4K*

![a](https://user-images.githubusercontent.com/1890549/190841999-689c9c38-ece4-46a0-ad85-f459ec64c5b8.png)


3) *A vision of paradise, Unreal Engine*

![a](https://user-images.githubusercontent.com/1890549/190841886-239406ea-72cb-4570-8f4c-fcd074a7ad7f.png)

_____

References:

- https://github.com/divamgupta/stable-diffusion-tensorflow
- https://github.com/CompVis/stable-diffusion
- https://github.com/geohot/tinygrad/blob/master/examples/stable_diffusion.py
