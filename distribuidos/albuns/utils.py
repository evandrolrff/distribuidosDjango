import pylast


def util():
    # You have to have your own unique two values for API_KEY and API_SECRET
    # Obtain yours from https://www.last.fm/api/account/create for Last.fm
    API_KEY = "49fd609d03e8ad5b8c8d703e10364a70"  # this is a sample key
    API_SECRET = "8ca7a8be38efa82834cf82a598608512"

    # In order to perform a write operation you need to authenticate yourself
    username = "meu_usuario"
    password_hash = pylast.md5("django$$123")

    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

    # Now you can use that object everywhere
    artist = network.get_artist("System of a Down")
    #artist.shout("<3")


    track = network.get_track("Iron Maiden", "The Nomad")
    track.love()
    track.add_tags(("awesome", "favorite"))
    
    
    # Arrange
    album = network.get_album("Gary Moore", "Ballads and Blues")

    # Act
    image = album.get_cover_image()
    print(type(image))

    # Assert
    #network.assertTrue(image.startswith("https://"))
    #network.assertTrue(image.endswith(".png"))

    # Type help(pylast.LastFMNetwork) or help(pylast) in a Python interpreter
    # to get more help about anything and see examples of how it works
        