watermark
=========

给图片添加文字水印，支持设置文字内容、大小、透明度、颜色、旋转等

效果图
~~~~~~

|image0|

安装配置
~~~~~~~~

安装 Pillow:

``pip install Pillow``

使用
~~~~

例子：

``python3 watermark.py -m '测试水印ABC123' -f weixiaobao.jpg``

具体使用参数介绍：

运行 ``python3 watermark.py -h``

::

   usage: watermark.py [-h] [-f FILE] [-m MARK] [-o OUT] [-c COLOR] [-s SPACE]
                       [-a ANGLE] [--size SIZE] [--opacity OPACITY]

   optional arguments:
     -h, --help               show this help message and exit
     -f FILE, --file FILE     image file path or directory
     -m MARK, --mark MARK     watermark content
     -o OUT, --out OUT        image output directory, default is ./output
     -c COLOR, --color COLOR  font color like '#000000', default is #F4F4F4
     -s SPACE, --space SPACE  space between watermarks, default is 60
     -a ANGLE, --angle ANGLE  rotate angle of watermarks, default is 30
     --size SIZE              font size of text, default is 25
     --opacity OPACITY        opacity of watermarks, default is 0.4

.. |image0| image:: https://raw.githubusercontent.com/jingle1267/watermark/master/output/weixiaobao.jpg

