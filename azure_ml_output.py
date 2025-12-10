import json
import sys
import requests

if len(sys.argv) != 5:
    print("Usage: python model_output.py ORIGIN DEST DEPARTURE ARRIVAL")
    sys.exit(1)

origin = sys.argv[1]
dest = sys.argv[2]
dep = int(sys.argv[3])
arr = int(sys.argv[4])

# Example static values for date/distance while testing:
year, month, day, day_of_week, distance = 2025, 12, 15, 3, 1000

payload = {
    "input_data": {
        "columns": [
            "YEAR", "MONTH", "DAY", "DAY_OF_WEEK",
            "ORIGIN_AIRPORT", "DESTINATION_AIRPORT",
            "SCHEDULED_DEPARTURE", "DISTANCE", "SCHEDULED_ARRIVAL"
        ],
        "index": [0],
        "data": [[year, month, day, day_of_week,
                  origin, dest, dep, distance, arr]]
    }
}

url = "YOUR AZURE ENDPOINT"
api_key = "YOUR API KEY"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

response = requests.post(url, headers=headers, json=payload)

data = response.json()
prediction = data[0]

sched_arr_hrs = int(arr // 100)
sched_arr_mins = int(arr % 100)

pred_code = int(round(prediction))
hh = pred_code // 100
mm = pred_code % 100

hh += mm // 60
mm = mm % 60

pred_arr = hh * 60 + mm
sched_arr = sched_arr_hrs * 60 + sched_arr_mins
delay = sched_arr - pred_arr

print(f"Raw Prediction: {prediction}")
print(f"Predicted Arrival time: {hh:02d}:{mm:02d}")

if delay > 0: 
    print(f"Delay: Early by {delay} minutes")
else:
    delay = abs(delay)
    print(f"Delay: {delay} minutes delayed")