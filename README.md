# Resource Field Assignment Script

This script assigns crystals and avatars to resource fields based on resource field emission match count weighted by ERA1 PPM cost. The assignment helps identify the best resource field for each NFT by evaluating the resources it emits.

## Prerequisites
- macOS Terminal (on Windows, you'll need to install python).
- A token from the staking website. This token can either be embedded directly within the script or set as an environment variable `LVCIDIA_TOKEN`.
#### Dependencies:
- Python 3
- Libraries used: `json`, `subprocess`, and `os`

## Steps

### 1. Obtaining the Token:
1. Open the Safari browser (or Chrome/Firefox) and navigate to [https://staking.lvcidia.xyz/](https://staking.lvcidia.xyz/).
2. Log in to the website using your credentials.
3. Once logged in, right-click anywhere on the page and select "Inspect" or "Inspect Element" to open Developer Tools.
4. Navigate to the "Network" tab in the Developer Tools panel. You might need to refresh the webpage (press `Cmd + R`) to see network activity.
5. Look for a network call named `earn-rate`. It should have a URL starting with `https://backend.prd.lvcidia.web3.uken.com/api/tokens/staking-progress/`.
6. Click on this `earn-rate` call, and in the right pane, navigate to the "Headers" section.
7. Scroll down until you see an entry labeled "Authorization". It will look something like:
   ```
   Authorization: Bearer YOUR_TOKEN_HERE
   ```
8. Copy the `YOUR_TOKEN_HERE` part.

### 2. Setting Up the Script:

1. Download the script and save it to a convenient location on your machine.
2. Open the script using any text editor.
3. You have two options to set your token:
    1. **Directly within the Script:**
       - Find the line with the default `"YOUR_TOKEN_HERE"` value and replace it with the token you copied in the previous section.
       - For example:
         ```python
         ...
         6  # Get the environment variable LVCIDIA_TOKEN or default to YOUR_TOKEN_HERE
         7  token = os.environ.get("LVCIDIA_TOKEN", "YOUR_TOKEN_HERE")
         ...
         ```
    2. **Set as an Environment Variable:**
       - Instead of modifying the script, you can set the `LVCIDIA_TOKEN` environment variable with the value of your token. This method is more secure as it avoids potential risks associated with hardcoding the token in the script.
       - To set the environment variable, you can open your terminal and run the following command (replace `YOUR_TOKEN_HERE` with your actual token):
         ```bash
         export LVCIDIA_TOKEN=YOUR_TOKEN_HERE
         ```
       - Alternatively, you can add the above line to your shell's startup configuration file (e.g., `.bashrc`, `.zshrc`) to make the environment variable persistent.

4. Save the file and close the text editor.

### 3. Running the Script:

1. Open Terminal (you can find it using Spotlight with `Cmd + Space` and then typing "Terminal").
2. Navigate to the directory where you saved the script using the `cd` command. For instance, if you saved it to your Desktop, you'd type:
   ```bash
   cd ~/Desktop
   ```
3. Make the script executable:
   ```bash
   chmod +x fieldfvcker.py
   ```
4. Run the script:
   ```bash
   ./fieldfvcker.py
   ```

5. The script will now execute, and you'll see output related to the NFTs and the resource field assignment in the following format:
   ```
   #   NFT                                                                                     Resource Field
   -   ---                                                                                     --------------
   0   https://opensea.io/assets/ethereum/0x10cdcb5a80e888ec9e9154439e86b911f684da7b/801       1-Release
   1   https://opensea.io/assets/ethereum/0x10cdcb5a80e888ec9e9154439e86b911f684da7b/7399      1-Release
   2   https://opensea.io/assets/ethereum/0x10cdcb5a80e888ec9e9154439e86b911f684da7b/2988      1-Release
   ...
   ```

*NOTES:*
- *Resource field ID# aligns with resource field order of appearance on the staking dashboard (e.g., #1==Release, #2==Tentacula, etc.)*.
- *Earn rate is disregarded - this might be incorporated later if there's a need*.
- *Make sure to handle the `LVCIDIA_TOKEN` with care, as it's sensitive data.*
- *This script assumes you have `curl` available in your command-line interface.*
