# DCSC Asset Registry

Tool used to store information regarding assets produced within the DCSC in
order to increase asset reusability.

## Deployment

Application can be deployed for both production and development.

### Development Deployment using Vagrant

**Requirements:**

- [Vagrant](https://www.vagrantup.com)

Run `vagrant up` in the root folder to start Vagrant.

Run `vagrant ssh` to go inside the Vagrant machine.

To start the server, `cd /vagrant` and then `npm start`. The server will automatically connect to the database within Vagrant.

To access the web application, navigate to `localhost:3000` in your browser.
The database is also accessible on `localhost:27017` if you wish to access it
in Robomongo.

### Preview Deployment using Docker Compose

**Requirements:**

- [Docker](https://www.docker.com)
- Docker-Compose `1.6+`

To deploy run `docker-compose up` in the root folder.

Afterwards you an access the application on `localhost:80`.
The database is not accessible from outside the docker network.

### Production Deployment using Terraform

Coming soon
