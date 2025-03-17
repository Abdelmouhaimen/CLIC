import numpy as np

def get_random_mask(width=64,height=64,sampling_ratio=0.1):
    mask = np.random.choice([0,255],size=(height,width), p=[1-sampling_ratio,sampling_ratio]).astype(np.uint8)
    return mask
