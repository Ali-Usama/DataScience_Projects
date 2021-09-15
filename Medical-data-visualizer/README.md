# Medical Data Visualizer

## Introduction

In this project, we have visualized and made calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations.

## Data description

The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

File name: medical_examination.csv

| Feature | Variable Type | Variable      | Value Type |
|:-------:|:------------:|:-------------:|:----------:|
| Age | Objective Feature | age | int (days) |
| Height | Objective Feature | height | int (cm) |
| Weight | Objective Feature | weight | float (kg) |
| Gender | Objective Feature | gender | categorical code |
| Systolic blood pressure | Examination Feature | ap_hi | int |
| Diastolic blood pressure | Examination Feature | ap_lo | int |
| Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |
| Glucose | Examination Feature | gluc | 1: normal, 2: above normal, 3: well above normal |
| Smoking | Subjective Feature | smoke | binary |
| Alcohol intake | Subjective Feature | alco | binary |
| Physical activity | Subjective Feature | active | binary |
| Presence or absence of cardiovascular disease | Target Variable | cardio | binary |

## Tasks Performed

In this project, we have created a chart similar to `examples/Figure_1.png`, where we showed the counts of good and bad outcomes for the `cholesterol`, `gluc`, `alco`, `active`, and `smoke` variables for patients with cardio=1 and cardio=0 in different panels.

Used the data to complete the following tasks in `medical_data_visualizer.py`:
* Added an `overweight` column to the data. To determine if a person is overweight, first calculated their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Used the value 0 for NOT overweight and the value 1 for overweight.
* Normalized the data by making 0 always good and 1 always bad. If the value of `cholesterol` or `gluc` was 1, made the value 0. If the value was more than 1, made the value 1.
* Converted the data into long format and created a chart that shows the value counts of the categorical features using seaborn's `catplot()`. The dataset should be split by 'Cardio' so there is one chart for each `cardio` value. The chart should look like `examples/Figure_1.png`.
* Cleaned the data. Filtered out the following patient segments that represent incorrect data:
  - diastolic pressure is higher than systolic (Keep the correct data with `(df['ap_lo'] <= df['ap_hi'])`)
  - height is less than the 2.5th percentile (Keep the correct data with `(df['height'] >= df['height'].quantile(0.025))`)
  - height is more than the 97.5th percentile
  - weight is less than the 2.5th percentile
  - weight is more than the 97.5th percentile
* Created a correlation matrix using the dataset. Plotted the correlation matrix using seaborn's `heatmap()`. Masked the upper triangle. The chart looks like `examples/Figure_2.png`.


Unit tests are written for you under `test_module.py`.

### Development

For development, you can use `main.py` to test your functions. Click the "run" button and `main.py` will run.


