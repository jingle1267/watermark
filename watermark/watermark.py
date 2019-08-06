# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author  : jingle1267
@Time    : 2019-08-05 13:45
@desc：  : 
"""
import argparse
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageChops


# 生成水印图片，返回添加水印的函数
def generate_watermark_image(args):
	# 字体宽度
	width = len(args.mark) * args.size

	# 创建水印图片(宽度、高度)
	mark = Image.new(mode='RGBA', size=(width, args.size))

	# 生成文字
	draw_table = ImageDraw.Draw(im=mark)
	draw_table.text(xy=(0, 0),
									text=args.mark,
									fill=args.color,
									font=ImageFont.truetype('fzhtjt.ttf',
																					size=args.size))
	del draw_table

	# 裁剪空白
	mark = crop_image(mark)

	# 透明度
	set_opacity(mark, args.opacity)

	# 在im图片上添加水印 im为打开的原图
	def mark_im(im):

		# 计算斜边长度
		c = int(math.sqrt(im.size[0] * im.size[0] + im.size[1] * im.size[1]))

		# 以斜边长度为宽高创建大图（旋转后大图才足以覆盖原图）
		mark2 = Image.new(mode='RGBA', size=(c, c))

		# 在大图上生成水印文字，此处mark为上面生成的水印图片
		y, idx = 0, 0
		while y < c:
			# 制造x坐标错位
			x = -int((mark.size[0] + args.space) * 0.5 * idx)
			idx = (idx + 1) % 2

			while x < c:
				# 在该位置粘贴mark水印图片
				mark2.paste(mark, (x, y))
				x = x + mark.size[0] + args.space
			y = y + mark.size[1] + args.space

		# 将大图旋转一定角度
		mark2 = mark2.rotate(args.angle)

		# 在原图上添加大图水印
		if im.mode != 'RGBA':
			im = im.convert('RGBA')
		im.paste(mark2,  # 大图
						 (int((im.size[0] - c) / 2), int((im.size[1] - c) / 2)),  # 坐标
						 mask=mark2.split()[3])
		del mark2
		return im

	return mark_im


# 添加水印，然后保存图片
def add_mark(image_path, mark, args):
	im = Image.open(image_path)

	image = mark(im)
	name = ''
	if image:
		name = os.path.basename(image_path)
		if not os.path.exists(args.out):
			os.mkdir(args.out)

		new_name = os.path.join(args.out, name)
		if os.path.splitext(new_name)[1] != '.png':
			image = image.convert('RGB')
		image.save(new_name)

		print("Picture {0} add watermark Success.".format(name))
	else:
		print("Picture {0} add watermark Failed.".format(name))


# 设置水印透明度
def set_opacity(im, opacity):
	assert opacity >= 0 and opacity <= 1

	alpha = im.split()[3]
	alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
	im.putalpha(alpha)
	return im


# 裁剪图片边缘空白
def crop_image(im):
	bg = Image.new(mode='RGBA', size=im.size)
	diff = ImageChops.difference(im, bg)
	del bg
	bbox = diff.getbbox()
	if bbox:
		return im.crop(bbox)
	return im


def main():
	parser = argparse.ArgumentParser()
	parser.description = '给图片添加文字水印，支持设置文字内容、大小、透明度、颜色、旋转等'
	parser.add_argument("-f", "--file", type=str, help="image file path or directory")
	parser.add_argument("-m", "--mark", type=str, help="watermark content")
	parser.add_argument("-o", "--out", default="./output", help="image output directory, default is ./output")
	parser.add_argument("-c", "--color", default="#F4EEF1", type=str,
											help="font color like '#000000', default is #F4F4F4")
	parser.add_argument("-s", "--space", default=60, type=int, help="space between watermarks, default is 60")
	parser.add_argument("-a", "--angle", default=30, type=int, help="rotate angle of watermarks, default is 30")
	parser.add_argument("--size", default=25, type=int, help="font size of text, default is 25")
	parser.add_argument("--opacity", default=0.4, type=float, help="opacity of watermarks, default is 0.4")

	args = parser.parse_args()

	if isinstance(args.mark, str) and sys.version_info[0] < 3:
		args.mark = args.mark.decode("utf-8")

	mark = generate_watermark_image(args)

	if os.path.isdir(args.file):
		names = os.listdir(args.file)
		for name in names:
			image_file = os.path.join(args.file, name)
			add_mark(image_file, mark, args)
	else:
		add_mark(args.file, mark, args)


if __name__ == '__main__':
	main()
