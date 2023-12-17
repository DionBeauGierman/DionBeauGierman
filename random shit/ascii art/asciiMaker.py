from tkinter import filedialog as fd
import moviepy.editor as mp
from PIL import Image
import pygame
import cv2

def pix2ascii(image, range_width=25, new_line_width=100):
    ASCII_CHARS = ' .,-~^*_:;<>+=|!1ilI/\()[]?%&8B@$MZ0OQLR#$'
    pixels = image.convert('L').getdata()
    ascii_str = ''
    for i, pixel_value in enumerate(pixels):
        # Use int() instead of type casting
        ascii_str += ASCII_CHARS[int(pixel_value * (len(ASCII_CHARS) - 1) / 256)]
        if (i+1) % new_line_width == 0:
            ascii_str += '\n'  # Insert a newline after a certain number of characters
    return ascii_str

def cam2ascii(max_width=100, max_height=60):
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized_gray = cv2.resize(gray, (max_width, max_height))  # Use the user-defined size
        image = Image.fromarray(resized_gray)

        ascii_str = pix2ascii(image)  # Assuming you have the map_pixels_to_ascii function from previous examples

        print(ascii_str)  # Display the ASCII art in the console

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
def vid2ascii(file_path, FPS, max_width=100, max_height=100):
    video_clip = mp.VideoFileClip(file_path)
    audio_clip = video_clip.audio

    cap = cv2.VideoCapture(file_path)
    fps = cap.get(cv2.CAP_PROP_FPS)

    pygame.init()
    pygame.mixer.init()
    
    temp_audio_file = 'temp_audio.wav'
    audio_clip.write_audiofile(temp_audio_file)

    pygame.mixer.music.load(temp_audio_file)
    pygame.mixer.music.play()

    for frame in video_clip.iter_frames(fps=FPS, dtype='uint8'):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized_gray = cv2.resize(gray, (max_width, max_height))
        image = Image.fromarray(resized_gray)

        ascii_str = pix2ascii(image)
        print(ascii_str)

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    cap.release()
    cv2.destroyAllWindows()
    
def img2ascii(file_path):
    image = Image.open(file_path)
    image = image.resize((100, 100), Image.LANCZOS)  # Use Image.LANCZOS as the resampling filter
    ascii_str = pix2ascii(image)

    return ascii_str

def fromUpload():
    file_path = input('please input file path: ')
    
    if '"' in file_path:
        file_path = file_path.replace('"', '')
    
    extension = ''.join(file_path.split('.')[-1:])

    print(extension)
    
    if extension == 'png' or extension == 'jpg' or extension == 'jpeg' or extension == 'webp':
        ascii_str = img2ascii(file_path)
        
        print(ascii_str)
        
    elif extension == 'mp4':
        fps = float(input('how much fps does this video run at? '))
        
        ascii_str = vid2ascii(file_path, fps)
        
    else:
        print('for image only png, jpg, jpeg or webp files are possible\nfor video only mp4. ')