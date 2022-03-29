# Azure-Functions-New

This is my First Azure Project.
The Process flow is as
  a) User invokes a Rest Endpoint for Azure Function with data for ML
  b) The Azure Function Invokes a ML Webservice with Data
  c) Store the response and responds back with the data
  d) Status updates are made to a MySql Database


Request URL, not able to post in the Webpage:

https://rohanvittest.azurewebsites.net/api/SampleFunction?code=HM5CDuXolCGER00dUIeFR/aaWY3HjFjJttimGjUvV6jrealKzJLFMA==&name=Rohan&data={
  "Inputs": {
    "WebServiceInput0": [
      {
        "ID": 1,
        "LIMIT_BAL": 20000,
        "SEX": 2,
        "EDUCATION": 2,
        "MARRIAGE": 1,
        "AGE": 24,
        "PAY_0": 2,
        "PAY_2": 2,
        "PAY_3": -1,
        "PAY_4": -1,
        "PAY_5": -2,
        "PAY_6": -2,
        "BILL_AMT1": 3913,
        "BILL_AMT2": 3102,
        "BILL_AMT3": 689,
        "BILL_AMT4": 0,
        "BILL_AMT5": 0,
        "BILL_AMT6": 0,
        "PAY_AMT1": 0,
        "PAY_AMT2": 689,
        "PAY_AMT3": 0,
        "PAY_AMT4": 0,
        "PAY_AMT5": 0,
        "PAY_AMT6": 0,
        "default payment next month": 1
      }
    ]
  },
  "GlobalParameters": {}
}
