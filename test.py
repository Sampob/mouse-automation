from file_interpeting.readfile import *
from image_matching.image_functions import *
from image_matching.pixel_functions import *
from util.save_to_file import *

readfile("test.data")
print(compare_rgb([60, 63, 65], rgb_at_mouse(), 10))

