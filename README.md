# LVCIDIA NFT Yield Optimizer
## Table of Contents
- [LVCIDIA NFT Yield Optimizer](#lvcidia-nft-yield-optimizer)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [How to Download](#how-to-download)
  - [Prerequisites](#prerequisites)
  - [Getting Started](#getting-started)
  - [Quick Start](#quick-start)
    - [For macOS/Linux/Unix users:](#for-macoslinuxunix-users)
    - [For Windows users:](#for-windows-users)
  - [Example Use and Output](#example-use-and-output)
  - [Explanation for `resource_weights` and `value_hierarchy` in `config.py`](#explanation-for-resource_weights-and-value_hierarchy-in-configpy)
    - [Location](#location)
    - [Purpose](#purpose)
    - [How to modify `resource_weights`:](#how-to-modify-resource_weights)
    - [How to rearrange `value_hierarchy`:](#how-to-rearrange-value_hierarchy)
  - [Safety Notes](#safety-notes)
  - [Feedback and Support](#feedback-and-support)

## Features
- Determine the optimal staking field for given NFT IDs.
- Weigh resources based on their value hierarchy.
- Detailed yield breakdown for each NFT.
- Batch scripts for convenient execution across different platforms.
## How to Download
1. Visit the **LVCIDIA NFT Yield Optimizer** GitHub repository (CONGRATS YOU'RE ALREADY HERE).
2. Look for the green `Code` button.
3. Click on `Download ZIP`.
4. Once the ZIP file is downloaded, extract its contents to your desired location on your computer.
## Prerequisites
- **Terminal/Command Line Interface**:
  - **macOS/Linux/Unix**: Default terminal.
  - **Windows**: Command Prompt, PowerShell, or [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/).
  - ***NOTE***: When installing python on ***Windows***, be sure to select
    the option to ***"Add python.exe to PATH [X]***".
- **Python**:
  - **macOS/Linux/Unix**: Typically comes preinstalled.
  - **Windows**: Download and install Python from [python.org](https://www.python.org/downloads/).
- **LVCIDIA_TOKEN**: (Not a FVCK TOKEN - an authorization token) Essential for fetching NFT staking details. Refer to the "Getting Started" section below for instructions on obtaining and setting this up.
**Note**: You don't need to manually install any Python packages. The provided
setup scripts will automatically set up a virtual environment and install the
necessary packages (`requests` and `python-dotenv`) for you.
## Getting Started
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
## Quick Start
### For macOS/Linux/Unix users:

1. Navigate to the project directory:
```bash
cd /path/to/lvcidia/
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
1. Run the batch script, providing NFT IDs for crystals and avatars (separated by a single space):
```bash
fieldfvcker.bat --crystals [CRYSTAL_IDS] --avatars [AVATAR_IDS]
```
> **Note**: These scripts automatically check for a `venv` in the project directory and set it up if it doesn't exist. They will also install necessary dependencies in this virtual environment.
## Example Use and Output

**Command**:
```
./fieldfvcker.sh --crystals 2231 91 --avatars 3559
```
**Expected Result**:
```
[#################################################>] 100%

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
| 01    CRYSTAL//2231 @ 12    |          |         |         | 1.489    |          |         |          |         |         |
| 02    CRYSTAL//91 @ 09      | 0.355    |         |         | 0.341    |          |         | 0.248    |         |         |
| 03    AVATAR//3559 @ 07     | 0.166    |         |         |          | 0.169    |         |          |         |         |
|---------------------------------------------------------------------------------------------------------------------------|
| TOTAL                       | 0.522    |         |         | 1.830    | 0.169    |         | 0.248    |         |         |
|---------------------------------------------------------------------------------------------------------------------------|

```

## Explanation for `resource_weights` and `value_hierarchy` in `config.py`

### Location
Both `resource_weights` and `value_hierarchy` can be located in the `config.py` file within the LVCIDIA NFT Yield Optimizer's main directory. This file serves as the central configuration hub for the tool, ensuring easy adjustments as required.

### Purpose

The `resource_weights` and `value_hierarchy` play important roles in the LVCIDIA NFT Yield Optimizer.

1. **`resource_weights`**: Dictates the significance of each resource field. In the `total_earn_rate(data)` function, the code computes a weighted earning rate by associating each resource's `intervalEarnRate` with its defined weight. Fields with elevated weights bear more influence on the total earning rate.

2. **`value_hierarchy`**: This list is really only important when there are resources that share the same weight. This list dictates which resource takes precedence over  others (with the same weight). Fields positioned earlier in the list are deemed superior.

### How to modify `resource_weights`:
Represented as a dictionary, each key-value pair in `resource_weights` aligns with a resource field's ID and its respective weight. Adjusting a field's weight involves:

1. Identifying the resource ID within the dictionary.
2. Tweaking the connected value to your preferred weight.

NOTE: Weights are all relative to one another (i.e. if you add a 0 to the digits they will result in the same hierarchy). Also, weights have only been tested with integers - I am not sure if it will accept floats (decimals). 


Example:
```python
resource_weights = {
    8: 5,  # Obsidian
    5: 4,  # Gold
    3: 3,  # Ceramic
    4: 3,  # Chameleon
    1: 2,  # Black Titanium
    2: 2,  # Bronze
    9: 2,  # Silver
    7: 1,  # Hydrogen
    6: 1,  # Helium
}
```
Say you want to prioritize hydrogen as much as Ceramic and Chameleon, you can simply tweak the second number of the hydrogen line as follows:

```python
    7: 3,  # Hydrogen
```
With a new value of 3, the script would rank hydrogen emission with the same value weigh of Ceramic and Chameleon.
  
### How to rearrange `value_hierarchy`:
The `value_hierarchy` list uses the field ID's index to represent its hierarchical position and is used to settle ties. To shuffle priorities just reorder the field IDs within the list in line with your new hierarchy.

NOTE: This really only matters or will only affect resources with the same value weights in the resource_weights table.

Example:
```python
value_hierarchy = [
    8,  # Obsidian
    5,  # Gold
    3,  # Ceramic
    4,  # Chameleon
    1,  # Black Titanium
    2,  # Bronze
    9,  # Silver
    7,  # Hydrogen
    6,  # Helium
]
```
If you want to change the priority that gets applied to Black Titanium, Bronze, and Silver (All resource_weight values of 2) just switch up their position:
 ```python
value_hierarchy = [
    8,  # Obsidian
    5,  # Gold
    3,  # Ceramic
    4,  # Chameleon
    9,  # Silver (New priority)
    2,  # Bronze (New priority)
    1,  # Black Titanium (New priority)
    7,  # Hydrogen
    6,  # Helium
]
```


## Safety Notes
- Keep your `LVCIDIA_TOKEN` confidential. Refrain from sharing your `.env` file or disclosing your token in public forums.
- Tokens might expire or become void over time. If you encounter authorization
  errors, you may need to retrieve a new token from the browser, as explained in the "Getting Started" section. The prompt asking for your ``LVCIDIA_TOKEN`` is triggered by the absence of a `.env` file, accordingly if you need to re-enter or update your ``LVCIDIA_TOKEN`` simply delete your ``.env`` file and it will ask for your ``LVCIDIA_TOKEN`` the next time you call the command.
- Always utilize the script responsibly to avoid overwhelming the backend server.
## Feedback and Support

For feedback, issues, or any other queries, please contact @andyd_andrea in the LVCIDIA discord using the message:
> "its a good day to put the top down on the lebaron. don't you think @andyd_andrea?"  

...I'll know what it means.
