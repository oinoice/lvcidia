#!/usr/bin/env python3
import json
import subprocess
import os
import time

# Get the environment variable LVCIDIA_TOKEN or default to YOUR_TOKEN_HERE
token = os.environ.get("LVCIDIA_TOKEN", "YOUR_TOKEN_HERE")


BASE_URL = "https://backend.prd.lvcidia.web3.uken.com"
HEADERS = [
    "-H",
    "Host: backend.prd.lvcidia.web3.uken.com",
    "-H",
    "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "-H",
    "Accept: application/json",
    "-H",
    "Accept-Language: en-US,en;q=0.5",
    "-H",
    "Accept-Encoding: gzip, deflate, br",
    "-H",
    "Referer: https://staking.lvcidia.xyz/",
    "-H",
    "Content-Type: application/json",
    "-H",
    f"Authorization: Bearer {token}",  # Use the f-string to insert the token value
    "-H",
    "Origin: https://staking.lvcidia.xyz",
    "-H",
    "Connection: keep-alive",
    "-H",
    "Sec-Fetch-Dest: empty",
    "-H",
    "Sec-Fetch-Mode: cors",
    "-H",
    "Sec-Fetch-Site: cross-site",
    "-H",
    "TE: trailers",
]

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

resource_weights = {8: 5, 5: 4, 3: 3, 4: 3, 1: 2, 2: 2, 9: 2, 6: 1, 7: 1}

value_hierarchy = [8, 5, 3, 4, 1, 2, 9, 6, 7]


def send_request(endpoint):
    """
    Sends a HTTP request to an endpoint and returns the response as a JSON
    object, or None if the request fails.

    :param endpoint: The `endpoint` parameter is a string that represents the specific API endpoint or
    URL path that you want to send a request to. It is typically appended to the base URL to form the
    complete URL for the request
    :return: The function `send_request` returns either a JSON object if the request is successful, or
    `None` if the request fails.
    """
    command = ["curl"] + HEADERS + [BASE_URL + endpoint]
    result = subprocess.run(command, capture_output=True, text=True)

    time.sleep(0.1)  # Sleep for 100ms

    if result.returncode == 0:
        return json.loads(result.stdout)
    else:
        print(f"Request failed with status code: {result.returncode}")
        return None


def get_value(nft, resource_field):
    """
    Calculates the value of a given resource field in an NFT based on the
    resources it emits.

    :param nft: The `nft` parameter is a dictionary that represents a non-fungible token (NFT). It
    contains information about the NFT, including its resources
    :param resource_field: The `resource_field` parameter is a dictionary that contains information
    about a specific resource field. It has the following structure:
    :return: the total value calculated based on the resources emitted by the resource field.
    """
    value = 0
    for resource in nft["resources"]:
        if resource_field["resources"][str(resource["id"])]["emittedByResourceField"]:
            value += resource_weights.get(resource["id"], 1)
    return value


def best_resource_field_for_nft(nft, resource_fields):
    """
    Finds the resource field with the highest value for a given NFT.

    :param nft: The `nft` parameter represents the non-fungible token (NFT) for which we want to find
    the best resource field
    :param resource_fields: A dictionary where the keys are the field names and the values are the
    corresponding resource fields
    :return: the best resource field for the given NFT.
    """
    best_value = -1
    best_resource_field = None

    for i, resource_field in resource_fields.items():
        current_value = get_value(nft, resource_field)
        if current_value > best_value:
            best_value = current_value
            best_resource_field = i

    return best_resource_field


def get_nfts():
    """
    Retrieves the staking progress and earn rate for NFTs.
    :return: the response from the API endpoint "/api/tokens/staking-progress/earn-rate".
    """
    endpoint = "/api/tokens/staking-progress/earn-rate"
    response = send_request(endpoint)
    if type(response) is str:
        print(f"Unexpected response type for NFTs: {response}")
        return None
    return response


def get_resource_fields():
    """
    Retrieves resource fields data from multiple endpoints and
    returns a dictionary containing the data.
    :return: a dictionary called `resource_fields`.
    """
    resource_fields = {}

    for resource_number in range(1, 15):
        endpoint = f"/api/stats/resource-fields/{resource_number}"
        json_data = send_request(endpoint)
        if json_data:
            resource_fields[resource_number] = json_data
    return resource_fields


def assign_nft_to_best_resource_field():
    """
    Retrieves NFTs, retrieves resource fields, determines the best resource field for each NFT, and prints the NFT's OpenSea URL and its
    corresponding best resource field.
    :return: The function does not explicitly return anything. However, it prints the information about
    the NFTs and their assigned resource fields.
    """
    nfts = get_nfts()

    if not nfts:
        print("Failed to retrieve NFTs.")
        return

    resource_fields = get_resource_fields()

    # Creating a list of tuples with relevant info for each NFT
    nft_info_list = []
    for nft in nfts:
        best_resource = best_resource_field_for_nft(nft, resource_fields)
        opensea_url = f"https://opensea.io/assets/ethereum/{nft['address']}/{nft['id']}"
        resource_label = resource_field_labels.get(best_resource, "Unknown")
        nft_info_list.append((opensea_url, best_resource, resource_label))

    # Sorting the list by resource field id
    sorted_nft_info_list = sorted(nft_info_list, key=lambda x: x[1])

    print("\n    #    NFT" + (" " * 78) + "\tResource Field")
    print("    -    ---" + (" " * 78) + "\t--------------")
    for i, info in enumerate(sorted_nft_info_list):
        print(f"    {i} \t{info[0]} \t{info[1]}-{info[2]}")
    print("\n")


if __name__ == "__main__":
    assign_nft_to_best_resource_field()
