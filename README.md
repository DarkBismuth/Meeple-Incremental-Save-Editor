Meeple Save Editor
📁 Save Location

Your save file is located in the following directory:

%USERPROFILE%\AppData\LocalLow\Simply Artizan\Meeple Incremental


Inside this directory, you'll find a folder named with a string of numbers. Open that folder, then navigate to the cloud folder. This is where your save file is stored.

📄 Save File

The save file you want to edit is:

gameSaveData.json

🛠️ Usage
1. Back Up Your Save

Before making any changes, create a backup of your original save file in case anything goes wrong.

2. Set Up Your Workspace

Copy your save file to a new folder of your choice. For example:

Documents/MeepleSave


Place both Python scripts (decode_save.py and encode_save.py) in this same folder.

3. Decode Your Save

Open a terminal in your workspace directory and run:

python decode_save.py


This will decode your save file into gameSaveData.decoded.json, which you can open in a text editor to make changes.

4. Edit Your Save

Open gameSaveData.decoded.json and modify the values to your liking.

⚠️ Warning: Be careful when changing upgrade values. Setting GlobalIncomeUpgradeData1_p much higher than 50000 may cause the game to crash when loading your save.

5. Encode Your Save

Once you've finished editing, run:

python encode_save.py


This will generate your edited save file: gameSaveData.edited.

6. Replace Your Original Save
Navigate back to your original save location.
Keep a backup of your original gameSaveData.json.
Replace the original save with gameSaveData.edited.
Rename gameSaveData.edited to gameSaveData.json.

Launch the game and load your save to see your changes.

⚠️ Disclaimer

Always back up your save before editing. Incorrect or excessive values may cause crashes or corrupt your save data.

Happy editing!
