from take_picture import take_picture
from compare_faces import compare_faces
from lock_screen import lock_screen

while True:
    target_image_path = take_picture()
    matches = compare_faces('images/me.png', target_image_path)
    if not matches:
        lock_screen()
        break
