
API and Selenium Tests for the DCSC Asset Registry
==================================================

**Pre-requisites:**
- Python 2.7.*
- Install Selenium `pip install selenium`
- Download and install PhantomJS (http://phantomjs.org/download.html)
- Add PhantomJS to your $PATH
- Install NoseTests `pip install nose`

**Usage:**
Set up environment variables
- `export AR_ENDPOINT="http://your_endpoint_here"`

Run all the tests
- `cd tests`
- `nosetests`
