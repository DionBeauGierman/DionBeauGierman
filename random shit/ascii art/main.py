# Dion Beau Gierman

import asciiMaker as am

while True:
    
    #probeer dit
    try:
        choice = int(input('do you want to (1) upload a file or (2) use the camera? '))
        
        # als het geen 1 of 2 is maak exceptie
        if choice != 1 and choice != 2:
            raise Exception('please input either 1 or 2')
        
    # als er een exceptie is doe dit en ga opnieuw
    except Exception as e:
        print(f'error: {e}. try again')
        
    # anders ga er uit
    else:
        break

# als de keuze voor upload is start het dat
if choice == 1:
    am.fromUpload()
    
# als de keuze voor camera is start het dat
elif choice == 2:
    am.cam2ascii()