Meeple Save Editor

A Python-based save editor for Meeple Incremental that allows you to decode, modify, and re-encode your game save data.

Save Location

Your save file is located in the following directory:

%USERPROFILE%\AppData\LocalLow\Simply Artizan\Meeple Incremental


Inside this directory, you'll find a folder named with a string of numbers. Open that folder, then navigate to the cloud folder. This is where your save file is stored.

Save File

The file you want to edit is:

gameSaveData.json

Usage
1. Back Up Your Save

Before making any changes, create a backup of your original save file in case something goes wrong.

2. Set Up Your Workspace

Copy your save file to a new folder of your choice. For example:

Documents/MeepleSave


Place both Python scripts, decode_save.py and encode_save.py, in the same directory.

3. Decode Your Save

Open a terminal in your workspace directory and run:

python decode_save.py


This will generate a file named gameSaveData.decoded.json, which you can open in a text editor to modify your save data.

4. Edit Your Save

Open gameSaveData.decoded.json and modify the values to your liking.

Note: Setting GlobalIncomeUpgradeData1_p significantly higher than 50000 may cause the game to crash when loading your save. Edit values carefully.

5. Encode Your Save

After making your changes, run:

python encode_save.py


This will generate your edited save file:

gameSaveData.edited

6. Replace Your Original Save
Navigate back to your original save location.
Make sure you have a backup of the original gameSaveData.json.
Copy gameSaveData.edited into the save directory.
Delete or move the original gameSaveData.json.
Rename gameSaveData.edited to gameSaveData.json.

Launch the game and load your save to verify that your changes were applied successfully.

Disclaimer

Always back up your save data before making changes. Incorrect or excessive values may cause crashes or corrupt your save file. Use this tool at your own risk.

Requirements
Python 3
A text editor for modifying JSON files
License

See the repository's license file for licensing information.
