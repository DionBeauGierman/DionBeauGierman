import moviepy.editor as mp
from PIL import Image
import pygame
import cv2

# dit is voor het veranderen van pixels naar ascii
def pix2ascii(image, range_width=25, new_line_width=100):
    
    #alle ascii characters
    ASCII_CHARS = ' .,-~^*_:;<>+=|!1ilI/\()[]?%&8B@$MZ0OQLR#$'
    
    pixels = image.convert('L').getdata()
    ascii_str = ''
    
    # elke pixel word veranderd
    for i, pixel_value in enumerate(pixels):
        ascii_str += ASCII_CHARS[int(pixel_value * (len(ASCII_CHARS) - 1) / 256)]
        
        # als er een nieuwe lijn moet komen komt die
        if (i+1) % new_line_width == 0:
            ascii_str += '\n' 
            
    return ascii_str

# camera naar ascii
def cam2ascii(max_width=100, max_height=60):
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # maakt het grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized_gray = cv2.resize(gray, (max_width, max_height))
        image = Image.fromarray(resized_gray)

        # gebruikt de pix2ascii converter
        ascii_str = pix2ascii(image)

        print(ascii_str)

        # eigenlijk nutteloos maar laat me
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # camera gaat uit
    cap.release()
    cv2.destroyAllWindows()
    
# video naar ascii
def vid2ascii(file_path, FPS, max_width=100, max_height=100):
    
    # video
    video_clip = mp.VideoFileClip(file_path)
    audio_clip = video_clip.audio

    cap = cv2.VideoCapture(file_path)

    pygame.init()
    pygame.mixer.init()
    
    temp_audio_file = 'temp_audio.wav'
    audio_clip.write_audiofile(temp_audio_file)

    # audio start
    pygame.mixer.music.load(temp_audio_file)
    pygame.mixer.music.play()

    # elke frame word gegraysceled en geconvert
    for frame in video_clip.iter_frames(fps=FPS, dtype='uint8'):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized_gray = cv2.resize(gray, (max_width, max_height))
        image = Image.fromarray(resized_gray)

        ascii_str = pix2ascii(image)
        print(ascii_str)
        
    cap.release()
    cv2.destroyAllWindows()
    
# foto naar ascii
def img2ascii(file_path):
    
    # convert foto -> ascii
    image = Image.open(file_path)
    image = image.resize((100, 100), Image.LANCZOS)
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