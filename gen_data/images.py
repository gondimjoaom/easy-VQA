from PIL import Image, ImageDraw
from random import randint
from shape import Shape
import math

# We draw the image at a larger scale and then resize it down to get anti-aliasing
# This is necessary because PIL's draw methods don't anti-alias
IM_SIZE = 64
IM_DRAW_SCALE = 2
IM_DRAW_SIZE = IM_SIZE * IM_DRAW_SCALE

MIN_SHAPE_SIZE = IM_DRAW_SIZE / 8
MAX_SHAPE_SIZE = IM_DRAW_SIZE / 2

TRIANGLE_ANGLE_1 = 0
TRIANGLE_ANGLE_2 = -math.pi / 3

def create_image(filename, shape, color, location=None):
	r = randint(230, 255)
	g = randint(230, 255)
	b = randint(230, 255)
	im = Image.new('RGB', (IM_DRAW_SIZE, IM_DRAW_SIZE), (r, g, b))

	draw = ImageDraw.Draw(im)
	draw_shape(draw, shape, color, location)
	del draw

	im = im.resize((IM_SIZE, IM_SIZE), resample=Image.BILINEAR)

	im.save(filename, 'png')

def draw_shape(draw, shape, color, location = None):
	if shape is Shape.RECTANGLE:
		if location == "left":
			w = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE / 2) # lowering max shape size to ensure
			h = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE / 2) # it will fit in the image
			x = randint(0, IM_DRAW_SIZE // 2 - w)
			y = randint(0, IM_DRAW_SIZE - h)
			draw.rectangle([(x, y), (x + w, y + h)], fill=color.value)
		elif location == "right":
			w = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE / 2) # lowering max shape size to ensure
			h = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE / 2) # it will fit in the image
			x = randint(IM_DRAW_SIZE // 2 - w, IM_DRAW_SIZE)
			y = randint(0, IM_DRAW_SIZE - h)
			draw.rectangle([(x, y), (x + w, y + h)], fill=color.value)
		else:
			w = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
			h = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
			x = randint(0, IM_DRAW_SIZE - w)
			y = randint(0, IM_DRAW_SIZE - h)
			draw.rectangle([(x, y), (x + w, y + h)], fill=color.value)

	elif shape is Shape.CIRCLE:
		if location == "left":
			d = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE / 2) # lowering max shape size to ensure
															# it will fit in the image
			x = randint(0, IM_DRAW_SIZE // 2  - d)
			y = randint(0, IM_DRAW_SIZE - d)
			draw.ellipse([(x, y), (x + d, y + d)], fill=color.value)
		elif location == "right":
			d = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE / 2) # lowering max shape size to ensure
															# it will fit in the image
			x = randint(IM_DRAW_SIZE // 2  - d, IM_DRAW_SIZE)
			y = randint(0, IM_DRAW_SIZE - d)
			draw.ellipse([(x, y), (x + d, y + d)], fill=color.value)
		else:
			d = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
			x = randint(0, IM_DRAW_SIZE - d)
			y = randint(0, IM_DRAW_SIZE - d)
			draw.ellipse([(x, y), (x + d, y + d)], fill=color.value)

	elif shape is Shape.TRIANGLE:
		if location == "left":
			pass
		else:
			s = randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
			x = randint(0, IM_DRAW_SIZE - s)
			y = randint(math.ceil(s * math.sin(math.pi / 3)), IM_DRAW_SIZE)
			draw.polygon([
				(x, y),
				(x + s * math.cos(TRIANGLE_ANGLE_1), y + s * math.sin(TRIANGLE_ANGLE_1)),
				(x + s * math.cos(TRIANGLE_ANGLE_2), y + s * math.sin(TRIANGLE_ANGLE_2)),
			], fill=color.value)

	else:
		raise Exception('Invalid shape!')