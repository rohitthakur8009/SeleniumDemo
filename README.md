This is a demo of Selenium and Python based UI TEsting framework.

The demo is conducted on "https://parabank.parasoft.com/parabank/index.htm" which is a dummy website for Automation testing.

Reporting tool used is allure.

To run locally clone the repo,

Run:

`docker build . -t rohitthakur8009/selenium-demo`

to build the image

Run:

`docker-compose up`

to run the tests and bring up the reporting server

Example:

<img width="1431" alt="image" src="https://user-images.githubusercontent.com/12047776/167125525-0b09515b-8f00-4065-b19b-671b201f16f1.png">


<img width="1188" alt="image" src="https://user-images.githubusercontent.com/12047776/167125624-4d8b858c-b722-4e57-9018-6d5d42f85751.png">


The reports will be accessible on http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html?redirect=false#

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/12047776/167125798-d247104d-dd7a-4e4e-b782-05e477787eff.png">



