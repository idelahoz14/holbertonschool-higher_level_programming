#!/bin/bash
# Takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl "$1" -sH "X-HolbertonSchool-User-Id: 98"
