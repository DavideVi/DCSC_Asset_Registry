# DCSC Asset Registry

Tool used to store information regarding assets produced within the DCSC in
order to increase asset reusability.

## Deployment

Application can be deployed for both production and development.

### Development Deployment using Vagrant

**Requirements:**

- Vagrant

Simply run `vagrant up` inside the root folder.

To start the server go to `/vagrant` and type: `npm start`. The server will
automatically connect to the database within Vagrant.

To access the web application, navigate to `localhost:3000` in your browser.
The database is also accessible on `localhost:27017` if you wish to access it
in Robomongo.

### Preview Deployment using Docker Compose

**Requirements:**

- Docker
- Docker-Compose `1.6+`

To deploy run `docker-compose up` in the root folder.

Afterwards you an access the application on `localhost:80`.
The database is not accessible from outside the docker network.

### Production Deployment using Terraform

Coming soon
