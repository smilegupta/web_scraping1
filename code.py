from google_images_download import google_images_download   
​
response = google_images_download.googleimagesdownload()  
​
arguments = {"keywords":"Egg Curry","limit":200,"print_urls":True, "chromedriver":"C:\\Users\\DELL\\Downloads\\chromedriver.exe"}   
paths = response.download(arguments)   
print(paths)
