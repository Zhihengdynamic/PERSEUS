###############
#### CODES ####
###############

ekgCodes = ["EKG Not Interpretable", "EKG Interpretable", "EKG Disconnect",'Annotation Error','My new button']
ppgCodes = ["PPG Not Interpretable", "PPG Interpretable", "PPG Disconnect",'Annotation Error','My new button']
qosCodes = ["QoS Incorrect", "QoS Correct",'Annotation Error']

# Color options for annotations.
ekgColorSelector = ['red', 'green', 'teal', 'black','orange']
ppgColorSelector = ['red', 'green', 'teal', 'black','orange']
qosColorSelector = ['#FF00FF', 'blue', 'gray','orange']

####################
#### APPEARANCE ####
####################

ppgYRange = [0,5000]
ekgYRange = [-1.5,1.5]
spo2YRange = [50,120]
hrYRange = [0,250]
YRange3 = [0,250]
YRange4 = [0,250]
YRange5 = [0,250]


# Width and height options for viewers.
viewerWidth = 1500
ekgViewerHeight = 250
ppgViewerHeight = 250
spo2ViewerHeight = 150
hrViewerHeight = 150
nibpViewerHeight = 150
defaultViewerHeights = 250

# Line color and qos color options.
ekgLineColor = 'black'
ppgLineColor = 'black'
qosMarkerColor = 'red'

##############
#### MISC ####
##############

# Starting page before file gets initialized.
initializePage = -1

# Initial amount of data to display (in seconds).
windowInSecs = 60

timeAroundAlarm = 300

# Frequency of PPG signal. Helps determine number of datapoints to grab per window.
ppgFrequency = 125

## Slider attributes for adjusting the amount of data (in seconds) displayed in the window. ##

# Smallest window size possible (in seconds).
timeSliderStart = 15

# Largest window size possible (in seconds).
timeSliderEnd = 120

timeSliderInitialValue = windowInSecs
timeSliderStep = 15
