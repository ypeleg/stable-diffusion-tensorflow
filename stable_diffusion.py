

import cv2
from stable_diffusion_tf.stable_diffusion import get_model, text2image

text_encoder, diffusion_model, decoder = get_model(512, 512, download_weights=True)

imgs = text2image("An astronaut riding a horse",
	img_height=512,
	img_width=512,
	text_encoder=text_encoder,
	diffusion_model=diffusion_model,
	decoder=decoder,
    batch_size = 1,
    n_steps = 50,
    unconditional_guidance_scale = 7,
    temperature = 0.0
)

for idx, img in enumerate(imgs):
    cv2.imwrite("out_%s.png" % idx , img[... , ::-1])

