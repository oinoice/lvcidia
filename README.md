# Resource Field Assignment Script

This script assigns crystals and avatars to resource fields based on resource field emission match count weighted by ERA1 PPM cost. The assignment helps identify the best resource field for each NFT by evaluating the resources it emits.

## Prerequisites
- Terminal:
  - **macOS/Linux/Unix**: Default terminal.
  - **Windows**: Use Command Prompt or PowerShell, or consider using [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/).
- Python installed:
  - **macOS/Linux/Unix**: Often comes preinstalled.
  - **Windows**: Download and install Python from [python.org](https://www.python.org/downloads/).
- A token from the staking website. This token can either be embedded directly within the script or set as an environment variable `LVCIDIA_TOKEN`.

#### Dependencies:
- Python 3
- Libraries used: `json`, `subprocess`, and `os`

## Steps

### 1. Obtaining the Token:
1. Open your preferred browser and navigate to [https://staking.lvcidia.xyz/](https://staking.lvcidia.xyz/).
2. Log in to the website using your credentials.
3. Once logged in, right-click anywhere on the page and select "Inspect" or "Inspect Element" to open Developer Tools.
4. Navigate to the "Network" tab in the Developer Tools panel. You might need to refresh the webpage to see network activity.
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
    2. **Set as an Environment Variable:**
       - Instead of modifying the script, you can set the `LVCIDIA_TOKEN` environment variable with the value of your token. 
       - **macOS/Linux/Unix**: Open your terminal and run the following command:
         ```bash
         export LVCIDIA_TOKEN=YOUR_TOKEN_HERE
         ```
       - **Windows (Command Prompt)**:
         ```bash
         set LVCIDIA_TOKEN=YOUR_TOKEN_HERE
         ```
       - **Windows (PowerShell)**:
         ```bash
         $env:LVCIDIA_TOKEN="YOUR_TOKEN_HERE"
         ```

4. Save the file and close the text editor.

### 3. Running the Script:

1. Open Terminal/Command Prompt/PowerShell.
2. Navigate to the directory where you saved the script.
   - **macOS/Linux/Unix**:
     ```bash
     cd /path/to/script/
     ```
   - **Windows**:
     ```bash
     cd \path\to\script\
     ```
3. Make the script executable (macOS/Linux/Unix only):
   ```bash
   chmod +x fieldfvcker.py
   ```
4. Run the script:
   - **macOS/Linux/Unix**:
     ```bash
     ./fieldfvcker.py
     ```
   - **Windows**:
     ```bash
     python fieldfvcker.py
     ```

5. The script will now execute, and you'll see output related to the NFTs and the resource field assignment.

*NOTES:*
- *Resource field ID# aligns with resource field order of appearance on the staking dashboard*.
- *Earn rate is disregarded - this might be incorporated later if there's a need*.
- *Make sure to handle the `LVCIDIA_TOKEN` with care, as it's sensitive data.*
- *This script assumes you have `curl` available in your command-line interface (commonly preinstalled on macOS/Linux, but Windows users may need to install it separately or use an alternative method).*

```
Remember, these are generalized steps and may need further tailoring depending on specific setups or unique requirements of a project or environment.
