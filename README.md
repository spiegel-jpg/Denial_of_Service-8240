# Denial_of_Service-8240
http://www.almhuette-raith.at is the source for apache access log files, which required a fair amount of preprocessing.
Due to the open nature of the log file on the webserver, all the entries pertaining to the access of the log file itself
have been removed.
Our dataset is available at https://data.world/noideabro/frc-attack for educational use only.

Description of each file in the repo is as follows - 

1. CSCI8240RP.ipynb - contains code to create quantiles, add noise and denoise using discrete wavelet transform.
2. LSTM.py - an example implementation of LSTM neural network.
3. apache_log_to_csv_converter.php - convert apahce log to csv file.
4. parse.py - analysizng the data for each year, month and day.
5. parseD.py - get directories from data.


This work is related to a research project being conducted at The University of Georgia.
