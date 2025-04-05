# Video DRM Downloader Bot

A Telegram bot that can download and process DRM-protected videos, split large files, and handle various video formats.

## Features

- Download DRM-protected videos from various sources
- Support for m3u8, mpd, and other streaming formats
- Automatic video splitting for files larger than 2GB
- Custom watermark overlay support
- Thumbnail generation
- Progress tracking during uploads
- Premium user system
- Admin controls

## Requirements

- Python 3.8+
- FFmpeg
- N_m3u8DL-RE
- aria2c
- yt-dlp

## Installation

1. Clone the repository:

```

2. Install dependencies:

```

3. Configure environment variables in `config.py`:


## Deploy to Heroku

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?button-url=https://github.com/&template=https://github.com/navedmohammad/New-DRM-Dl)

## Usage

1. Start the bot:

2. Send video URLs to the bot in any of these formats:
- Direct video links
- m3u8 links
- MPD streams
- Encrypted URLs (m3u8://:encrypted_url)

3. For files larger than 2GB, the bot will automatically:
- Split the video into 1GB parts
- Upload each part separately
- Add part numbers to captions
- Clean up temporary files

## Supported Platforms

- Regular video hosting sites
- DRM-protected streams
- M3U8 streams
- DASH/MPD streams
- Zoom recordings
- Custom platforms with encryption

## Commands

- `/start` - Start the bot
- `/help` - Show help message
- `/premium` - Check premium status
- `/admin` - Admin commands (admin only)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
```

This README provides:

1. A clear description of what the bot does
2. Key features list
3. Installation instructions
4. Deployment options
5. Usage instructions
6. Supported platforms
7. Available commands
8. Contributing guidelines
9. License information

You can customize this further by:
- Adding specific setup instructions for your environment
- Including screenshots or examples
- Adding troubleshooting guides
- Listing any specific dependencies or requirements
- Adding contact information or support channels

Let me know if you'd like me to modify any section or add more details!
```

</rewritten_file>
```

