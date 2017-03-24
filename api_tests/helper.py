import requests, os, json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def out_header(scenario):
    print bcolors.HEADER + "\n== " + scenario + " ==" + bcolors.ENDC

def make_request(endpoint, payload_file):
    print bcolors.OKBLUE + "\n[INFO]\t New request to " + endpoint + bcolors.ENDC

    # Loading payload
    payload = {}
    print bcolors.OKBLUE + "[DATA]\t Loading payload '" + payload_file + "'" + bcolors.ENDC
    try:
        with open('./payloads/' + payload_file) as data_file:
            payload = json.load(data_file)
    except Exception:
        print bcolors.FAIL + bcolors.BOLD + "[ERR ]\t Error loading payload '" + payload_file + "'" + bcolors.ENDC
        return None

    # Making request
    # print bcolors.OKBLUE + "[URL ]\t" + endpoint + bcolors.ENDC
    try:
        response = requests.post(endpoint, data=payload)

        if response.status_code == 500:
            print bcolors.FAIL + bcolors.BOLD + "[FAIL]\t Error 500" + bcolors.ENDC
            print "====="
            print response.text
            print "====="
            return None

        return response

    except Exception:
        print bcolors.FAIL + bcolors.BOLD + "[ERR ]\t Error making request" + bcolors.ENDC
        return None

def get_key(response, path):
    # TODO: Process path
    try:
        return response.json()["path"]
    except ValueError: # JSONDecodeError
        print bcolors.FAIL + bcolors.BOLD + "[ERR ]\t Error decoding JSON" + bcolors.ENDC
        print "====="
        print response.text
        print "====="
        return None
    except KeyError:
        return None

def assert_eq(actual, expected, message):
    if expected == actual:
        print bcolors.OKGREEN + "[OK  ]\t " + str(message) + bcolors.ENDC
    else:
        print bcolors.FAIL + "[FAIL]\t " + str(message) + "\n[FAIL]\t  \-> Expected: '" + str(expected) + "'; Actual: '" + str(actual) + "'" + bcolors.ENDC

def assert_neq(actual, expected, message):
    if expected != actual:
        print bcolors.OKGREEN + "[OK  ]\t " + str(message) + bcolors.ENDC
    else:
        print bcolors.FAIL + "[FAIL]\t " + str(message) + "\n[FAIL]\t  \-> Expected: NOT '" + str(expected) + "'; Actual: '" + str(actual) + "'" + bcolors.ENDC
