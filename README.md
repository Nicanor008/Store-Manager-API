[![Build Status](https://travis-ci.com/Nicanor008/Store-Manager-API.svg?branch=develop)](https://travis-ci.com/Nicanor008/Store-Manager-API)
[![Coverage Status](https://coveralls.io/repos/github/Nicanor008/Store-Manager-API/badge.svg?branch=develop)](https://coveralls.io/github/Nicanor008/Store-Manager-API?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/37d0c21d3071cbd5f2e3/maintainability)](https://codeclimate.com/github/Nicanor008/Store-Manager-API/maintainability)

# Store-Manager-API

Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store. This API is used to access the endpoints of the products and sales.

### What you can Achieve
1. Admin can add a product
2. Admin/store attendant can get all products
3. Admin/store attendant can get a specific product
4. Store attendant can add a sale order
5. Admin can get all sale order records

### API Endpoints
| API Endpoint | Functionality |
| -----------  | ------------- |
| POST /api/v1/auth/register |  Register a new user |
| POST /api/v1/auth/login |  Logins in a user and generates a token |
| GET /api/v1/products |  Fetch all products |
| POST /api/v1/products |  Create a single product into products list |
| GET /api/v1/products/<productsId> |  Fetch a single product into products list |
| GET /api/v1/sales |  Fetch all sale records |
| POST /api/v1/sales |  Create sale records into sales list |
| GET /api/v1/sales/<salesId> |  Fetch a sale record into sale list |


### How to run tests
This project has been implemented using unit tests. This is how you can test the endpoints:
* `git clone https://github.com/Nicanor008/Store-Manager-API.git`
* `cd Store-Manager-API`
* Activate the virtual environment `virtualenv venv'
* Install all dependencies required `pip install -r requirements.txt`
* Now run the unittests `nosetests` or `nosetests app/tests/v1`
* Test API endpoints in postman
