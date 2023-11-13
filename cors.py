from flask import Flask, make_response

def cors_preflight_response():

    response = make_response()

    # we can put the actual domain name next time
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    
    return response