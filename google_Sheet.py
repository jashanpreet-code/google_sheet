import requests
import datetime as dt
import os


date = dt.datetime.now()
today_time = (date.strftime("%I:%M:%S"))
today_date = (date.strftime("%d/%m/%Y"))

APPLICATION_ID = "318bbd0d"
APPLICATION_KEY  = "e3ec6be2fd95142f36e37c32f4149cc4"
WEIGHT = 70
HEIGHT = 170
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEET_ENDPOINT = os.environ["https://api.sheety.co/ce4db1c3caf3cc0bcec569c5e7e939c7/myWorkouts/workouts"]
# POST_ENDPOINT =    "https://api.sheety.co/ce4db1c3caf3cc0bcec569c5e7e939c7/myWorkouts/workouts"
# PUT_ENDPOINT = "https://api.sheety.co/ce4db1c3caf3cc0bcec569c5e7e939c7/myWorkouts/workouts"
# DELETE_ENDPOINT = "https://api.sheety.co/ce4db1c3caf3cc0bcec569c5e7e939c7/myWorkouts/workouts"


headers = {
    'x-app-id': APPLICATION_ID,
    'x-app-key': APPLICATION_KEY
  }

inter = input("Tell me which exercise you did: ")

params = {
    "query": inter,
    "gender" : "male",
    "weight_kg" : WEIGHT,
    "height_cm" : HEIGHT,
    "age" : 25    
}

re = requests.post(END_POINT, json=params, headers=headers)
print(re.status_code)
result = re.json()


# calori = (re.json()['exercises'][0]['nf_calories'])
# exercise = (re.json()['exercises'][0]['user_input'])
# time_duration = (re.json()['exercises'][0]['duration_min'])

for exercise in result["exercises"]:
    paramst = {
        "workout": {
            "Date": today_date,
            "Time": today_time,
            "Exercise": exercise["user_input"].title(),
            "Duration": exercise["duration_min"],
            "Calories": exercise["nf_calories"],
        }
}

head = {
    "Authorization": "Basic bnVsbDpudWxs",
}

#https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/edit?usp=sharing
# print(paramst["workout"])


gett = requests.post(
                     SHEET_ENDPOINT, 
                     json=paramst,
                     auth=(
                         os.environ["jashanpreet"],
                         os.environ["jashan@780"],
                     )
                     )
print(gett.status_code)
print(gett.text)


# gett = requests.get(RETRIVE_ENDPOINT)
# print(gett.status_code)

# sheet_inputs = requests.put(PUT_ENDPOINT, json=paramst, headers=head)
# print(sheet_inputs.status_code)

# sheety_headers = requests.get(RETRIVE_ENDPOINT)
# print(sheety_headers.text)
