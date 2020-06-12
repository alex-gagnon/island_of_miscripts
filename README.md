# Island of Miscripts

Welcome to the Island of Miscripts

## What is this repository for?

Random bits of scripts and code so I'm not reinventing the wheel over and over.


## PyIsland

Home of the miscreant python scripts.

### Setup without Docker

Run `pip install -e .\pyisland\` to get setup.

#### Create a virtual environment
Run `pip install virtualenv` to install the virtualenv package
Run `virtualenv .\pyisland\.venv` to create a virtualenv location
Run `.\pyisland\Scripts\activate` to start up the virtualenv
* Note - to deactivate the virtualenv, input `deactivate`

#### Install packages within the virtualenv
Run `pip install -r .\pyisland\requirements.txt` to install packages.

#### Testing

Run `pytest .\pyisland\` to run tests.

### Setup with Docker

Run `docker build -t <image-name> .\pyisland\`

Run `docker run -it --rm <container-name> <image-name>`

### Classic Problems

Classic problems that are often seen such as Hanoi Tower, Calculating Pi, etc.

### Python Classes

These are classes that provided good examples of OOP usage and that I often
use for reference. They can also be used by the Classic Problems.

## Contributing

* Place code in appropriate folder with some documentation
* When possible, have tests
