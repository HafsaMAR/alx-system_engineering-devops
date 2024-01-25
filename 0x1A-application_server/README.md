# 0x1A-application_server

## AirBnB Clone Deployment

This repository contains the necessary code and configurations to deploy the AirBnB Clone project. The deployment involves setting up the development and production environments, configuring Nginx, and serving the different components of the application.

### Server Information

| Name           | Username | IP              | State   |
|----------------|----------|-----------------|---------|
| 251432-web-01  | ubuntu   | 18.207.207.202  | running |
| 251432-web-02  | ubuntu   | 18.207.112.121  | running |
| 251432-lb-01   | ubuntu   | 18.234.129.6    | running |

### Task 0: Set up development with Python

In this task, we will set up the development environment and configure the Flask application to serve its content from the route /airbnb-onepage/ on port 5000.

Requirements:
- Ensure that task #3 of your SSH project is completed for web-01.
- Install the net-tools package on your server: `sudo apt install -y net-tools`
- Git clone your AirBnB_clone_v2 repository on your web-01 server.
- Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
- The Flask application object must be named `app`.

### Task 1: Serve a page with Nginx

Building on the previous task, we will now configure Nginx to serve the page from the route /airbnb-onepage/.

Requirements:
- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the process listening on port 5000.
- Nginx config file: 2-app_server-nginx_config

### Task 2: Add a route with query parameters

In this task, we will expand the web application by adding another service for Gunicorn to handle. Nginx will be configured to proxy requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001.

Requirements:
- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to the process listening on port 5001.
- Nginx config file: 3-app_server-nginx_config

### Task 3: Set up API server

In this task, we will serve the AirBnB clone v3 - RESTful API on web-01.

Requirements:
- Git clone your AirBnB_clone_v3 repository.
- Setup Nginx so that the route /api/ points to a Gunicorn instance listening on port 5002.
- Nginx must serve this page both locally and on its public IP on port 80.
- Gunicorn should be bound to api/v1/app.py.

### Task 4: Serve AirBnB clone v4

In this final task, we will serve the AirBnB clone v4 - Web dynamic on web-01.

Requirements:
- Git clone your AirBnB_clone_v4 repository.
- Gunicorn should serve content from web_dynamic/2-hbnb.py on port 5003.
- Setup Nginx so that the route / points to your Gunicorn instance.
- Setup Nginx to serve the static assets found in web_dynamic/static/.
- Nginx must serve this page both locally and on its public IP and port 5003.
- Update the IP in web_dynamic/static/scripts/2-hbnb.js to the correct IP.

### Conclusion

By following the instructions in this README file, you will be able to deploy the AirBnB Clone project successfully. Make sure to review the provided Nginx configuration files and update any necessary IP addresses or routes.