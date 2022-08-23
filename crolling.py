from google_images_download import google_images_download   #importing the library

def googleimagecrawling(keyword,list):
    response = google_images_download.googleimagesdownload()   #class instantiation

    arguments = {"keywords":"handsome",
    "limit":20,"print_urls":True}   
    paths = response.download(arguments)   
    print(paths)  