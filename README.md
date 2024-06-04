# Zamutify

This command-line script allows you to download YouTube playlists using `yt-dlp` and save them as MP3 audio files on your computer. It can also update the metadata of the MP3 files using the MusicBrainz API to fetch information about the songs.

## Requirements

- Python 3.x installed on your system.
- `yt-dlp` installed and accessible from the command line.
- An account on [MusicBrainz](https://musicbrainz.org/) (optional, only if you want to update metadata).

## Usage

1. Clone this repository or download the files to your computer.
2. Install the dependencies by running `pip install -r requirements.txt`.
3. Place the URLs of the YouTube playlists you want to download in a text file named `playlist_urls.txt`, one per line.
4. Run the script `download_playlists.bat` to download the playlists.
5. Run the script `update_metadata.bat` to update the metadata of the MP3 files (optional, requires internet access).

## Configuration

- You can adjust the base download folder by modifying the `BASE_DOWNLOAD_PATH` variable in the scripts.
- If you want to update metadata, make sure to set up an account on MusicBrainz and provide your credentials in the `metadatos.py` script.

## Contributions

Contributions are welcome. If you have ideas for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
Downloads youtube playlists, create folders with the name of the playlist and updates the mp3 metatada
