Strava Integration

## What:

This repo is used for pulling my Strava activities and playing around with the data, by activity type.

- In 'get_tokens.py', go to the Strava URL, enter client_id, authorize when prompted, and copy the 'code' in the URL to the space provided further down in the script.
    - Once run, a file 'tokens/strava_tokens.json' will get updated with your refresh token that can be used later
- 'pull_activities.ipynb' is a notebook to play around with the data
    - Eventually I will create classes & functions that will update a set of metrics & charts that I can use to analyze my training data for the last X days/weeks/months


## Why:

I enjoy looking at historical training data by activity (run/bike), and analyzing my pace/speed, cadence, heart rate, etc. As I ramp up for a particular race, I want to confirm my volume ramps up appropriately for the outcome I expect. Most of the features I want to analyze my data with are only available in the paid subscription to Strava. The API allows me to draw similar conclusions, without the need to pay the premium.


## Credit:

The code used to pull my activities using the Strava API is roughly the same as what was done here: https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86

I changed a few of the token initialization to suit my needs. I've also added my own analysis.

