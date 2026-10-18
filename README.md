# Save Location

Navigate to the following directory:
%USERPROFILE%\AppData\LocalLow\Simply Artizan\Meeple Incremental

Open the folder named with a string of numbers, then open the cloud folder. This is where your save file is stored.

Save File: gameSaveData.json

# Usage
Copy your save file to a folder of your choice, such as Documents/MeepleSave.
Move both Python scripts into the same folder.
Run python decode_save.py and edit gameSaveData.decoded.json to your liking.

Note: Setting GlobalIncomeUpgradeData1_p much higher than 50000 may cause the game to crash on load.

Run python encode_save.py.
Move gameSaveData.edited back to your save folder, delete or back up the original save, and rename the edited file to gameSaveData.json.

Enjoy!
