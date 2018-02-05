# Currency Predictor

Currency Predictor is a Django web application that shows the history of prices for different cryptocurrencies and also predicts their prices in the near future.

## Getting Started

The instructions below will get you a copy of the project up and running on your local machine for development and testing purposes. To get started, clone the repository on a folder that you want.

### Prerequisites

The major things that you will need to run this application are Python3 and pip3

```
 $ sudo apt-get install python3
 $ sudo apt-get install python3-pip
```

### Installing

After you get the python3 and the pip3 installed and working, you will need to install the requirements to run your project.

For that purpose, go to the root directory of the repository and run the following command:

```
 $ pip3 install -r requirements.txt
```

Note: You might want to use a virtual environment for installing the python packages required for the project

```
 $ sudo pip3 install virtualenv
 $ virtualenv currencypredictor
 $ source path/to/env/bin/activate
```


## Running the tests

After you get the prerequisite packages installed in your virtualenv, you need to copy the contents of the .env.example file to a new .env file and make the changes accordingly.
For development mode, make DEBUG=True

Then, run your django application from the root directory through the following command:

```
 $ ./manage.py runserver
```
This will start a development server of Django in the localhost at port 8000. So, access your application at 127.0.0.1:8000


## Built With

* [Django](https://docs.djangoproject.com/en/2.0/) - The web framework used

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Ashish Jaiswal** - *Initial work* - [asheeshcric](https://github.com/asheeshcric)

## Acknowledgments

* The whole Python Team (Insight Workshop)