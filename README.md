# Github to Google Drive Sync

Helpful tutorial on how to start:   
Getting started: https://www.youtube.com/watch?v=I5ili_1G0Vk  
How to intagrate drive API: https://www.youtube.com/watch?v=9K2P2bWEd90&list=PL3JVwFmb_BnTamTxXbmlwpspYdpmaHdbz   
Google API reference: https://developers.google.com/workspace/drive/api/reference/rest  
Google Cloude Console: https://console.cloud.google.com/welcome  

## Setup 
1. go to https://console.cloud.google.com/welcome
2. **Create project:** near GoogleCloud logo -> Create Project -> New Project
3. **enable OAuth Consent Screen:** navigation menu -> APIs & Services -> OAuth consent screen - set external + provide app name and email + add scope (/auth/drive)
4. **enable drive integration:** navigation menu -> APIs & Services -> Library -> Google Drive API -> Enable
5. **generate credentials:** navigation menu -> APIs & Services -> Credentials -> DesktopApp -> Download JSON credentials file
6. **generate authentication token:** Run the `./update_drive.py` script for the first time. It will ask you to open link to authorize with Google account. This will generate `*.pickle` file
7. **encode the token file in base-64**: `base64 -w 0 token_drive_v3.pickle > token_b64.txt` command
8. **encode the credentials file in base-64**: `base64 -w 0 credentials.json > credentials_b64.txt`
9. **set secrects in GitHub repo**: GitHub -> Settings -> Security | Serets and variables -> Actions -> New Repository Secret -> GDRIVE_TOKEN_B64 and GDRIVE_CREDENTIALS_B64
10. **get google drive folder id**: Google Drive -> Share -> Copy Link. Copy part after `/folders/` 
11. **set google drive folder id**: in [update_drive.py](.github/workflows/update_drive.py) change `YOUR_FOLDER_ID` to your destination google drive folder ID extracted in the previous step
12. **voila!**: any file you put in [shared](shared/) folder and commit will be automatically uploaded to Google Drive 

## Important
- Empty folders on github are not commited. In order to commit empty folder, you need to create ".gitkeep" file. It will be removed automatically befor upload to Google Drive.
- For shared repo usage instruction read [HowToUse.md](HowToUse.md)