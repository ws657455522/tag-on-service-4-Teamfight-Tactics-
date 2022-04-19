import time

from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order.
print(time.time())
ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # need to run only once to download and load model into memory
img_path = 'da0.png'
result = ocr.ocr(img_path, cls=True)
print(result)
for line in result:
    print(line)
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores)
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')
print(time.time())
