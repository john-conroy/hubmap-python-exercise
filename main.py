#!/usr/bin/env python3
from client import ApiClient

# Example uuids for HuBMAP entities.
donor = '7b12f4f595083d2cba794e78e5c929f1'
sample = '062bd84696d51e02f670f064879b562d'
dataset = '0d1f7b2917325a7778ffecacb7ddba6f'

# Implement function here
def get_descendants_uuids_by_type():
    return

if __name__ == "__main__":
    # use the client to fetch json for a given entity
    client = ApiClient()
    # print the output from get_descendants_uuids_by_type
    print(get_descendants_uuids_by_type())
