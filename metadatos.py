#you have to install the dependencies of mutagen and musicbrainzgs, in powershell just copy this "pip install mutagen musicbrainzngs"
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import musicbrainzngs

# configure musicbrainz api, you will need to create an account at https://musicbrainz.org/ and put ur data here (or just leave it like that, it works anyways)
musicbrainzngs.set_useragent("user", "0.1", "mail")

def get_song_details(song_title):
    try:
        result = musicbrainzngs.search_recordings(recording=song_title, limit=1)
        if result['recording-list']:
            recording = result['recording-list'][0]
            title = recording['title']
            artist = recording['artist-credit'][0]['name']
            album = recording['release-list'][0]['title'] if 'release-list' in recording and recording['release-list'] else "Unknown Album"
            return {'title': title, 'artist': artist, 'album': album}
        else:
            return None
    except Exception as e:
        print(f"Error fetching details for {song_title}: {e}")
        return None

def update_mp3_metadata(file_path, song_details):
    try:
        audio = MP3(file_path, ID3=EasyID3)
        audio['title'] = song_details['title']
        audio['artist'] = song_details['artist']
        audio['album'] = song_details['album']
        audio.save()
        print(f"Updated metadata for {file_path}")
    except Exception as e:
        print(f"Error updating metadata for {file_path}: {e}")

def process_mp3_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".mp3"):
                file_path = os.path.join(root, filename)
                song_title = os.path.splitext(filename)[0]
                song_details = get_song_details(song_title)
                if song_details:
                    update_mp3_metadata(file_path, song_details)
                else:
                    print(f"No details found for {song_title}")

# you will have to put ur mp3 files path on here
folder_path = r"D:/Playlists/"
process_mp3_files(folder_path)
