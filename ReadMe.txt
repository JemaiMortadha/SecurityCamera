# Security Camera

Thanks for downloading this project! Support me by following me on GitHub: [JemaiMortadha](https://github.com/JemaiMortadha)

## Requirements

- Python 3.x
- Required Python libraries:
  - `requests`
  - `PIL` (Pillow)
  - `cv2` (OpenCV)

## Installation

Follow the commands below to install the necessary modules.

### Linux

```sh
sudo pip3 install requests
sudo pip3 install pillow
sudo pip3 install opencv-python
```

### Windows

```sh
pip install requests
pip install pillow
pip install opencv-python
```

## Setup

1. Create a Telegram bot:
   - Contact [@BotFather](https://telegram.me/BotFather) on Telegram.
   - Follow the instructions to create a new bot and obtain the bot token (`"XXXXXXXXX:YYYYYYYYYYYYYYYYYY"`).
   
2. Create a new Telegram group:
   - Add your bot and [@myidbot](https://telegram.me/myidbot) to the group.
   - Use [@myidbot](https://telegram.me/myidbot) to get the chat ID of the group.

3. Update the script:
   - Paste your bot token in `RunMe.py` at `<token>`.
   - Paste the chat ID in `RunMe.py` at `<chatid>`.

## Running the Application

1. Run the Python script:
   ```sh
   python RunMe.py
   ```

### Usage

1. The script will prompt you to take a reference image or use an existing one.
2. Enter the waiting time before motion detection starts.
3. The script will start monitoring for motion. When motion is detected, an image will be captured and sent to the specified Telegram chat.
