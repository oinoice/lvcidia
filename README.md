# 🍆 LVCIDIA NFT Yield Optimizer
**Important Update**: The previous version of this tool assigned crystals and avatars to resource fields based on the **resource field emission MATCH COUNT**, weighted by ERA1 PPM cost. The **newly enhanced version** of the script goes a step further; it actually calculates the amount of resources earned at each field and selects the one with the most yield. This significant upgrade ensures you get the best value from your NFT staking.

Optimize your NFT staking for the best yield with LVCIDIA NFT Yield Optimizer. This tool is designed to find the highest yielding resource field for your NFTs, considering their unique capabilities and token associations. Beyond just matching resource fields, it evaluates potential earnings across multiple fields, ensuring the optimal choice for your NFTs.
## 🍆 Features
- Determine the optimal staking field for given NFT IDs.
- Weigh resources based on their value hierarchy.
- Detailed yield breakdown for each NFT.
- Batch scripts for convenient execution across different platforms.
## 🍆 How to Download
1. Visit the **LVCIDIA NFT Yield Optimizer** GitHub repository (CONGRATS YOU'RE ALREADY HERE).
2. Look for the green `Code` button.
3. Click on `Download ZIP`.
4. Once the ZIP file is downloaded, extract its contents to your desired location on your computer.
## 🍆 Prerequisites
- **Terminal/Command Line Interface**:
  - **macOS/Linux/Unix**: Default terminal.
  - **Windows**: Command Prompt, PowerShell, or [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/).
    - NOTE: When installing python on Windows, be sure to select the option to
      "Add python.exe to PATH".
- **Python**:
  - **macOS/Linux/Unix**: Typically comes preinstalled.
  - **Windows**: Download and install Python from [python.org](https://www.python.org/downloads/).
- **LVCIDIA_TOKEN**: (Not a FVCK TOKEN - an authorization token) Essential for fetching NFT staking details. Refer to the "Getting Started" section below for instructions on obtaining and setting this up.
**Note**: You don't need to manually install any Python packages. The provided
setup scripts will automatically set up a virtual environment and install the
necessary packages (`requests` and `python-dotenv`) for you.
## 🍆 Getting Started
1. **Obtain the LVCIDIA_TOKEN**:
   - Visit `https://staking.lvcidia.xyz/`.
   - Right-click on the fully loaded page and choose `Inspect` or `Inspect Element` (wording may vary with the browser).
   - Go to the `Network` tab in the developer tools.
   - Refresh the page or perform another action to trigger a network request.
   - In the `Network` tab, locate a request with a URL that begins with `https://backend.prd.lvcidia.web3.uken.com/`.
   - Click the request, then in the right pane, under the `Headers` section, look for `Authorization`. The value will follow the format `Bearer YOUR_LVCIDIA_TOKEN`. Copy the `YOUR_LVCIDIA_TOKEN` section.
2. **Save the LVCIDIA_TOKEN**:
   - Run the script once. When prompted, enter your `LVCIDIA_TOKEN` and confirm. This action saves the token to a `.env` file for subsequent uses.
   - NOTE: The prompt asking for your ``LVCIDIA_TOKEN`` is triggered by the absence of a `.env` file, accordingly if you need to re-enter or update your ``LVCIDIA_TOKEN`` simply delete your ``.env`` file and it will ask for your ``LVCIDIA_TOKEN`` the next time you call the command.
## 🍆 Quick Start
### For macOS/Linux/Unix users:

1. Navigate to the project directory:
```bash
cd /mnt/mag/lab/lvcidia/
```
1. Grant execute permissions to the script:
```bash
chmod +x fieldfvcker.sh
```
1. Run the script, providing NFT IDs for crystals and avatars:
```bash
./fieldfvcker.sh --crystals [CRYSTAL_IDS] --avatars [AVATAR_IDS]
```
### For Windows users:
1. Navigate to the project directory using Command Prompt or PowerShell:
```bash
cd C:\path\to\directory\lvcidia
```
1. Run the batch script, providing NFT IDs for crystals and avatars:
```bash
fieldfvcker.bat --crystals [CRYSTAL_IDS] --avatars [AVATAR_IDS]
```
> **Note**: These scripts automatically check for a `venv` in the project directory and set it up if it doesn't exist. They will also install necessary dependencies in this virtual environment.
## 🍆 Example Use and Output

**Command**:
```
./fieldfvcker.sh --crystals 2231 91 --avatars 3559
```
**Expected Result**:
```
HIGHEST YIELDING FIELD:

    #   URL                                                                                     Resource Field
    -   ---                                                                                     --------------
    1   https://opensea.io/assets/ethereum/0x10cdcb5a80e888ec9e9154439e86b911f684da7b/3559      7-Intercore
    2   https://opensea.io/assets/ethereum/0x7afeda4c714e1c0a2a1248332c100924506ac8e6/91        9-Infected
    3   https://opensea.io/assets/ethereum/0x7afeda4c714e1c0a2a1248332c100924506ac8e6/2231      12-Prism

RESOURCE EARNING SUMMARY:

|---------------------------------------------------------------------------------------------------------------------------|
| # COLLECTION//NFT# @ FIELD# | tit      | bro     | cer     | chm      | gld      | hel     | hyd      | obs     | sil     |
|---------------------------------------------------------------------------------------------------------------------------|
| 01    CRYSTAL//2231 @ 12    |          |         |         | 0.056    |          |         |          |         |         |
| 02    CRYSTAL//91 @ 09      | 0.014    |         |         | 0.013    |          |         | 0.010    |         |         |
| 03    AVATAR//3559 @ 07     | 0.006    |         |         |          | 0.007    |         |          |         |         |
|---------------------------------------------------------------------------------------------------------------------------|
| TOTAL                       | 0.020    |         |         | 0.069    | 0.007    |         | 0.010    |         |         |
|---------------------------------------------------------------------------------------------------------------------------|
```
## 🍆 Safety Notes
- Keep your `LVCIDIA_TOKEN` confidential. Refrain from sharing your `.env` file or disclosing your token in public forums.
- Tokens might expire or become void over time. If you encounter authorization
  errors, you may need to retrieve a new token from the browser, as explained in the "Getting Started" section. The prompt asking for your ``LVCIDIA_TOKEN`` is triggered by the absence of a `.env` file, accordingly if you need to re-enter or update your ``LVCIDIA_TOKEN`` simply delete your ``.env`` file and it will ask for your ``LVCIDIA_TOKEN`` the next time you call the command.
- Always utilize the script responsibly to avoid overwhelming the backend server.
## 🍆 Feedback and Support

For feedback, issues, or any other queries, please contact @andyd_andrea in the LVCIDIA discord using the message:
> "its a good day to put the top down on the lebaron. don't you think @andyd_andrea?"  

...I'll know what it means.
