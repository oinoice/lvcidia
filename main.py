import requests
import json
import argparse
import os
import dotenv


dotenv.load_dotenv()  # Load environment variables from .env file

# Check if the token exists in environment variables
token = os.environ.get("LVCIDIA_TOKEN")

# If the token doesn't exist, prompt the user and save to .env file
if not token:
    token = input("Please paste your LVCIDIA_TOKEN: ")
    with open(".env", "a") as env_file:
        env_file.write(f"LVCIDIA_TOKEN={token}\n")

# Progress bar related variables
total_requests = 0  # This will be updated once we know the number of tokens and resource fields
completed_requests = 0


def print_progress_bar():
    bar_length = 50
    progress = min((completed_requests / total_requests), 1)  # Cap progress at 1 (or 100%)
    arrow = '#' * int(round(progress * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    print('\r[{0}] {1}%'.format(arrow + spaces, int(round(progress * 100))), end='')


# # Get the environment variable LVCIDIA_TOKEN or default to YOUR_TOKEN_HERE
# token = os.environ.get("LVCIDIA_TOKEN", "YOUR_TOKEN_HERE")

BASE_URL = "https://backend.prd.lvcidia.web3.uken.com/api/tokens/staking-details"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://staking.lvcidia.xyz/",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}",
    "Origin": "https://staking.lvcidia.xyz",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "TE": "trailers",
}

resource_field_labels = {
    1: "Release",
    2: "Tentacula",
    3: "Mandelbulb",
    4: "After Life",
    5: "Galactic Lightfield",
    6: "Dragon Heart",
    7: "Intercore",
    8: "Cybernetic Core",
    9: "Infected",
    10: "Temporal Shifter",
    11: "Baeige",
    12: "Prism",
    13: "Chromatic Aberation",
    14: "Antiphysic",
}

resource_codes = {
    1: "tit",
    2: "bro",
    3: "cer",
    4: "chm",
    5: "gld",
    6: "hel",
    7: "hyd",
    8: "obs",
    9: "sil",
}

resource_weights = {8: 5, 5: 4, 3: 3, 4: 3, 1: 2, 2: 2, 9: 2, 6: 1, 7: 1}
value_hierarchy = [8, 5, 3, 4, 1, 2, 9, 6, 7]

def fetch_earning_potential(resource_field_id, tokens):
    global completed_requests
    payload = {"resourceFieldId": resource_field_id, "tokens": tokens}
    response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(payload))
    completed_requests += 1
    print_progress_bar()
    if not response.json():
        print(f"\nError with resource field {resource_field_id}: {response.text}")
    return response.json()


def total_earn_rate(data):
    weighted_earning = sum(
        [
            res["intervalEarnRate"] * resource_weights.get(res["id"], 0)
            for res in data["resources"]
        ]
    )
    return weighted_earning


def best_field_for_nfts(tokens):
    earning_potentials = {}
    all_response_data = {}  # Store the detailed earning data for all NFTs

    for resource_field_id in range(1, 15):  # Looping through 14 resource fields
        response_data = fetch_earning_potential(resource_field_id, tokens)
        all_response_data[resource_field_id] = response_data  # Store the data
        total_earning_for_field = sum(
            [total_earn_rate(token_data) for token_data in response_data]
        )
        earning_potentials[resource_field_id] = total_earning_for_field

    # Find the resource field ID with the maximum earning potential considering value hierarchy for ties
    max_earning = max(earning_potentials.values())
    best_fields = [
        field_id
        for field_id, earning in earning_potentials.items()
        if earning == max_earning
    ]

    # If there's a tie, use the value hierarchy to decide
    best_field = best_fields[0]  # Default choice
    if len(best_fields) > 1:
        best_fields.sort(key=lambda x: value_hierarchy.index(x))
        best_field = best_fields[0]

    # Extract detailed earning data for the NFTs based on the best resource field
    best_response_data = all_response_data[best_field]
    nft_details = []
    for token_data in best_response_data:
        token_earning_details = {
            resource_codes[res["id"]]: res["intervalEarnRate"]
            for res in token_data["resources"]
        }
        nft_details.append(
            (
                token_data["address"],
                token_data["id"],
                token_data["resourceFieldId"],
                token_earning_details,
            )
        )

    return best_field, nft_details


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find the best resource field for NFTs."
    )
    parser.add_argument(
        "--crystals",
        nargs="*",
        default=[3859],
        type=int,
        help="List of NFT ids for crystals",
    )
    parser.add_argument(
        "--avatars", nargs="*", type=int, help="List of NFT ids for avatars"
    )

    args = parser.parse_args()

    tokens = []
    if args.crystals:
        tokens.extend(
            [
                {"id": id, "address": "0x7afeda4c714e1c0a2a1248332c100924506ac8e6"}
                for id in args.crystals
            ]
        )
    if args.avatars:
        tokens.extend(
            [
                {"id": id, "address": "0x10cdcb5a80e888ec9e9154439e86b911f684da7b"}
                for id in args.avatars
            ]
        )

    # Updating total requests based on number of tokens and resource fields
    total_requests = 14 * len(tokens)  # There are 14 resource fields

    """    # Printing headers
    print("\n\nHIGHEST YIELDING FIELD:\n")
    print("    #   URL" + (" " * 79) + "\tResource Field")
    print("    -   ---" + (" " * 79) + "\t--------------")
    """
    # Instead of directly printing, save the formatted string for printing at the end
    nft_results = []  
    # Define resource headers (assuming you have these)
    resources = ["tit", "bro", "cer", "chm", "gld", "hel", "hyd", "obs", "sil"]

    # This will hold a list of (label, resource_field_id, resource_rates)
    nft_resource_data = []
    
    # The first loop for printing OpenSea URLs and collecting earn rate data
    for nft in tokens:
        best_field, nft_details = best_field_for_nfts([nft])
        resource_field_name = resource_field_labels.get(best_field, "Unknown")

        opensea_url = f"https://opensea.io/assets/ethereum/{nft['address']}/{nft['id']}"
        nft_results.append((opensea_url, f"{best_field}-{resource_field_name}"))  # Note that we store the results as a tuple without the index

        response_data = fetch_earning_potential(best_field, [nft])
        resource_rates = {
            resource_codes.get(res["id"], "unknown"): res["intervalEarnRate"]
            for res in response_data[0]["resources"]
        }
        label = (
            "CRYSTAL"
            if nft["address"] == "0x7afeda4c714e1c0a2a1248332c100924506ac8e6"
            else "AVATAR"
        )
        nft_resource_data.append((f"{label}//{nft['id']}", best_field, resource_rates))

    print("\n\nHIGHEST YIELDING FIELD:\n")
    print("    #   URL" + (" " * 79) + "\tResource Field")
    print("    -   ---" + (" " * 79) + "\t--------------")

    # After sorting, we renumber the results.
    for i, (opensea_url, field) in enumerate(sorted(nft_results, key=lambda x: int(x[1].split('-')[0])), 1):
        print(f"    {i} \t{opensea_url} \t{field}")

    # First column is special - calculate based on header, data rows, and "TOTAL"
    first_col_width = max(
        len("# COLLECTION//NFT# @ FIELD#"),
        len("TOTAL"),
        max(
            len(f"{i:02}    {label} @ {field_id:02}")
            for i, (label, field_id, _) in enumerate(nft_resource_data, 1)
        ),
    )

    col_widths = {
        resource: max(
            7, max(len(str(data[2].get(resource, ""))) for data in nft_resource_data)
        )
        for resource in resources
    }

    # Print the summary table
    print("\n\nRESOURCE EARNING SUMMARY:\n")
    separator_line = (
        "|"
        + "-"
        * (first_col_width + 3 + sum(col_widths.values()) + len(resources) * 3 - 1)
        + "|"
    )
    print(separator_line)
    header = (
        "| "
        + "# COLLECTION//NFT# @ FIELD#".ljust(first_col_width)
        + " | "
        + " | ".join(resource.ljust(col_widths[resource]) for resource in resources)
        + " |"
    )
    print(header)
    print(separator_line)
    total_resources = {resource: 0 for resource in resources}
    max_nft_id_length = max(len(str(data[1])) for data in nft_resource_data)
    for i, (label, field_id, rates) in enumerate(nft_resource_data, 1):
        row_label = f"{i:02}    {label:<{max_nft_id_length + 9}} @ {field_id:02}"
        row_data = [row_label.ljust(first_col_width)]
        for resource in resources:
            earn_rate = rates.get(resource, "")
            formatted_rate = f"{earn_rate:.3f}" if earn_rate else ""
            row_data.append(formatted_rate.ljust(col_widths[resource]))
            if earn_rate:
                total_resources[resource] += earn_rate
        print("| " + " | ".join(row_data) + " |")

    print(separator_line)
    total_row = ["TOTAL".ljust(first_col_width)]
    for resource in resources:
        earn_rate = total_resources.get(resource, 0)
        formatted_rate = f"{earn_rate:.3f}" if earn_rate else ""
        total_row.append(formatted_rate.ljust(col_widths[resource]))
    print("| " + " | ".join(total_row) + " |")
    print(separator_line)
    print("\n\n")
