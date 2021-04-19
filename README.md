## Getting Started
### Running the Application


First of all create virtual environment and activate it as follows:
```
$ mkdir environments
$ cd environments
$ virtualenv -p python3 intagleo
$ source intagleo/bin/activate
```

Install the requirements
```
Navigate back to the project directory and run the following command
$ pip install -r requirements.txt
```

Db Configure
```
Create mysql database with any name and configure it according to .env.dist file then
run following command in project dir.
$ python manage.py migrate
```

Start the Django app
```
$ python manage.py runserver
```

Screens

![student](https://user-images.githubusercontent.com/40248466/107156169-93c76680-699e-11eb-8642-70dc54bbf790.png)

![add](https://user-images.githubusercontent.com/40248466/107156224-ec96ff00-699e-11eb-810a-f73b62caf451.png)

![courses](https://user-images.githubusercontent.com/40248466/107156202-d426e480-699e-11eb-86f4-f84a52bb2bc7.png)

![calculate](https://user-images.githubusercontent.com/40248466/107156189-b9547000-699e-11eb-8d66-4bb397953349.png)
