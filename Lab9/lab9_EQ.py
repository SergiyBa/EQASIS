import os

class YTLoad:
    def __init__(self, file, APIkey, *args) :

        filename, file_extension = os.path.splitext(file)

        match file_extension :
            case 'avi':
                pass
            case 'mp4':
                file=converter.mp4_to_avi(file)
            case '3gp':
                file = converter.3gp_to_avi(file)
            case 'mov':
                file = converter.mov_to_avi(file)

            #...etc
            case _:
                print("Unknown file type")
                return

        try:
            youtube.upload(APIkey, file, args)
        except Exception:
            print ('Something wrong')

#main

YTLoad('qqqq.mov', 3443434334343)






