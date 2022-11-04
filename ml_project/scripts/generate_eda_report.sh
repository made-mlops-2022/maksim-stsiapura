#!/bin/bash

PATH_TO_DATA="data/heart_cleveland_upload.csv"

papermill notebooks/heart-disease-dataset-cleveland-eda.ipynb \
          notebooks/heart-disease-dataset-cleveland-eda-executed.ipynb \
          -p path_to_data ${PATH_TO_DATA}

jupyter nbconvert --to html notebooks/heart-disease-dataset-cleveland-eda-executed.ipynb \
                  --output eda_report.html

rm notebooks/heart-disease-dataset-cleveland-eda-executed.ipynb
cp notebooks/eda_report.html reports/eda_report.html
rm notebooks/eda_report.html
