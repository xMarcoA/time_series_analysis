Food delivery company (time_series_analysis)
This program can predict the need for each meal in each center. Based on this information, the company can plan the raw material inventory accordingly.
2 different models are trained and compared with each other.
- ARIMA(Autoregressive-Integrated-Moving-Average Model)
- XGBoost

data_sql:
   - read in kaggle data
   - uploaded to local SQL server 

notebooks:
	- explore.ipynb:				 analyse the given data
	- forecasting_models.ipynb:	 creating and improve the models

figs: 
	- all created graphs to understand the data 

data source: 
  	- kaggle 

screenshots:

sql query:
![Bildschirmfoto 2021-05-06 um 15 54 01](https://user-images.githubusercontent.com/76050281/117311016-1e2b4380-ae84-11eb-8465-36af03c61ede.png)


pred. fig:
![Bildschirmfoto 2021-05-06 um 15 54 58](https://user-images.githubusercontent.com/76050281/117311412-74988200-ae84-11eb-9205-97ec8feaa723.png)

![Bildschirmfoto 2021-05-06 um 15 54 40](https://user-images.githubusercontent.com/76050281/117311079-2c795f80-ae84-11eb-8223-ee8a199b2955.png)


some analysis graphs:
![Bildschirmfoto 2021-05-06 um 15 55 32](https://user-images.githubusercontent.com/76050281/117311252-5468c300-ae84-11eb-983e-559097dfee60.png)

![Bildschirmfoto 2021-05-06 um 15 55 56](https://user-images.githubusercontent.com/76050281/117311278-5a5ea400-ae84-11eb-92cc-23e5c8c6ab95.png)

![Bildschirmfoto 2021-05-06 um 15 55 44](https://user-images.githubusercontent.com/76050281/117311328-63e80c00-ae84-11eb-8580-aabd1cdf90f8.png)

![Bildschirmfoto 2021-05-06 um 15 56 13](https://user-images.githubusercontent.com/76050281/117311441-7a8e6300-ae84-11eb-9180-e0950e8e3555.png)



