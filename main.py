#requisites
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import sys

[features, labels] = load_digits(return_X_y = True)

#variables
speeding = 0.35
speed_vio = 0
speed_AutoFail = 0
mileage= 0.35
braking = 0.35
corners = 0.35
clutch = 0.35

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

def check_distance(mileage, driver_score):
  if miles_travelled >= 100:
    driver_score -= 0.05
  else:
    driver_score += 0.05

def check_acceleration(acceleration, driver_score):
  if acceleration >= 100:
    driver_score -= 0.05
  else:
    driver_score += 0.05

def check_braking(braking, driver_score):
  if braking >= 1:
    driver_score -= 0.05
  else:
    driver_score += 0.05


#test data
featureS1, featureS2, labelS1, labelS2 = train_test_split(features,labels,train_size = 0.8,test_size=0.2_


## > tested data: giveScore



print('Driver S')
#accuracy rating
print('The driver accuracy is: ')



#push
#PUSH forwards text to "push.php" file to push to HastingsDirect Database
def push():
  if __name__ =="__main__":
    if len(sys.argv) != 2:
      print("Usage: python main.py<push.php>")
      sys.exit(1)