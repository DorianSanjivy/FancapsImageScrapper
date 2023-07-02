import requests

#Incrementation
x=0
count = 0

#Variable a setup
FormatType = "anime"

#numero de debut
dbnumero = 19151958

#espacement entre le numero des photos
nbspace = 2

nbloop = 10

folder_path = 'imagescap/'

#loop
while x < nbloop:

    # Specify the URL of the image to download

    #movie
    if (FormatType == "movie") :
        url = "https://cdni.fancaps.net/file/fancaps-movieimages/" + str(dbnumero) + ".jpg"

    #anime
    if (FormatType == "anime"):
        url = "https://cdni.fancaps.net/file/fancaps-animeimages/" + str(dbnumero) + ".jpg"

    # Send a GET request to the server and receive the response
    response = requests.get(url)

    # Check if the response was successful (HTTP status code 200)
    if response.status_code == 200:
        # Save the image file to disk
        with open(folder_path+ str(dbnumero)+".jpg", "wb") as f:
            f.write(response.content)
        print('Download: ' + str(dbnumero) + ".jpg")
        count = count + 1
    else:
        print(f'Erreur {response.status_code} lors du téléchargement de {url}')

    x = x+1
    dbnumero = dbnumero + nbspace

#finish
print('\nDownload is finished \nYou have download ' + str(count) + ' picture !')