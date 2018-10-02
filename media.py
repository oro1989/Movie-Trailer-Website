class Movie(object):
    '''class Movie stores tilte, poster image url and Youtube trailer url'''
    def __init__(self, title, posterImgUrl, youtubeTrailerUrl):
        self.title = title
        self.poster_image_url = posterImgUrl
        self.trailer_youtube_url = youtubeTrailerUrl
