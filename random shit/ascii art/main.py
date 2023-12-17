import asciiMaker as am

while True:
    try:
        choice = int(input('do you want to (1) upload a file or (2) use the camera? '))
        
        if choice != 1 and choice != 2:
            raise Exception('please input either 1 or 2')
        
    except Exception as e:
        print(f'error: {e}. try again')
    else:
        break

if choice == 1:
    am.fromUpload()
elif choice == 2:
    am.cam2ascii()