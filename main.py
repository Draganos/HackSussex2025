#prerequisites
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
import requests
import json
import sys
import numpy as np
import pandas as pd

#ImportFromPHP
# Person ID selector
person_id = input("Enter Person ID: ")

# Hosted PHP URL (replace with your actual InfinityFree URL)
php_url = "http://hacksussex.infinityfreeapp.com/pull.php"  # CHANGE THIS

# Send request to InfinityFree PHP server
try:
  response = requests.post(php_url, data={"PersonID": person_id})
  response.raise_for_status()  # Raises an error if response is not 200 OK
except requests.RequestException as e:
  print(f"Error: Could not connect to the server. Details: {e}")
  sys.exit(1)

# Get the output from PHP
php_output = result.stdout.strip()

# Check if the output is valid JSON
try:
  data = json.loads(php_output)
  if "error" in data:
    print("No data found for this ID.")
    sys.exit(1)
  else:
    speed_vio = int(data.get("SpeedVio", 0))
    SpeedAutoFail = int(data.get("SpeedAutoFail", 0))
    miles_travelled = int(data.get("Mileage", 0))
    high_acceleration = int(data.get("HighAccelerations", 0))
    high_deceleration = int(data.get("HighDecelerations", 0))

    print("\n--- Driver Information ---")
    print(f"Person ID: {person_id}")
    print(f"Speed Violations: {speed_vio}")
    print(f"Speed AutoFail: {SpeedAutoFail")
    print(f"Miles Travelled: {miles_travelled}")
    print(f"High Accelerations: {high_acceleration}")
    print(f"High Decelerations: {high_deceleration}")

except json.JSONDecodeError:
  print("Error: Invalid data received from PHP.")
  sys.exit(1)

#variables - default scores
speeding = 0.35
distance = 0.35

driver_score = 0
driver_accuracy = 0

#Person ID selector
person_id = input('Enter Person ID: ')
print("Viewing person " + person_id + "'s ID")

#train


def check_speeding(speeding, speed_vio):
  while speed_AutoFail != 1:
    if speed_vio >= 1:
      speeding = speeding + 0.1
    if speed_vio >= 2:
      speeding = speeding + 0.125
    if speed_vio >= 2.5:
      speeding = speeding + 0.15
      if speed_vio >= 5:
        speeding = 0.9
  else:
    if speed_AutoFail == 1:
      speeding = 0.99

  return speeding


def check_distance(distance, miles_travelled):
  if miles_travelled >= 1000:
    distance -= 0.05
  else:
    distance += 0.3
  if miles_travelled >= 10000:
    distance -= 0.25
  return distance


def check_acceleration(high_acceleration, high_deceleration, miles_travelled):
  acceleration = high_acceleration + high_deceleration
  acceleration = (acceleration / miles_travelled) * 100
  if acceleration >= 2.5:
    acceleration = 0.7
  else:
    acceleration = 0.3


#test data
np.random.seed(42)
n_samples = 1000
speed_vio = np.random.randint(0, 12, size=n_samples)  #range 0-12
miles_travelled = np.random.randint(500, 2000, size=n_samples)  #500 to 2000
high_acceleration = np.random.randint(
    0, 21, size=n_samples)  # high acceleration events
high_deceleration = np.random.randint(
    0, 21, size=n_samples)  # high deceleration events

# if you want code with a little more correlation
# high_acceleration = np.random.randint(0, 21, size = n_samples)
# high_deceleration = high_acceleration - np.random.randint(0, 4, size = n_samples)
# if high_deceleration < 0 then high_deceleration = 0

data = pd.DataFrame({
    'SpeedViolations': speed_vio,
    'MilesTravelled': miles_travelled,
    'HighAccelerations': high_acceleration,
    'HighDecelerations': high_deceleration,
})

target_scores = (
    (speed_vio * -5) +  # More violations therefore lower score
    (miles_travelled / 100) +  # more experience therefore higher score
    (high_acceleration * -3) +  # risky behavior lowers score
    (high_deceleration * -3)).astype(int)

target_scores = np.clip(target_scores, 1, 999)

X_train, X_test, y_train, y_test = train_test_split(data,
                                                    target_scores,
                                                    test_size=0.2,
                                                    random_state=42)
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

## > tested data: giveScore

inputdata = pd.DataFrame_({
    'SpeedViolations': [speed_vio],
    'MilesTravelled': [miles_travelled],
    'HighAccelerations': [high_acceleration],
    'HighDecelerations': [high_deceleration]
})

#accuracy rating

driver_score = model.predict(inputdata)[0]
print(f"Predicted Driver Score: {round(driver_score, 2)}")
y_pred = model.predict(X_test)
accuracy = r2_score(y_test, y_pred)
print(f"Model Accuracy (R² Score): {round(accuracy, 4)}")

#push
#PUSH forwards text to "push.php" file to push to HastingsDirect Database
#def push():
#  if __name__ == "__main__":
#    if len(sys.argv) != 2:
#      print("Usage: python main.py<push.php>")
#      sys.exit(1)


def push_to_db(person_id, driver_score):
  php_push_url = "http://hacksussex.infinityfreeapp.com/push.php"
  data = {"PersonID": person_id, "DriverScore": driver_score}
  try:
    response = requests.post(php_push_url, data=data)
    response.raise_for_status()
    print("Data successfully pushed to database.")
  except requests.RequestException as e:
    print(f"Error pushing data: {e}")


push_to_db(person_id, round(driver_score, 2))

with open("result.txt", "w") as file:
  file.write(driver_score, "is the score logged. ")


# https://docs.google.com/presentation/d/1XXUxz-BJFOBBgI6trFrMrnTjChBzhoASJ9XoN5gzUPg/edit?usp=sharing
