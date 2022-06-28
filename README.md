# Flask REST API demo app

This is an app for demo purposes of creating Docker image and Kubernetes deployment. This readme will describe deployment on minikube, while deployment on any Cloud provider can differ.

### Requirements
- VirtualBox
- minikube (with virtualbox driver)
- IDE of choice (eg. VS Code)
- kubectl
- Postman or similar API tool

---
## Minikube setup

Start minikube

```bash
minikube start --driver=virtualbox --no-vtx-check
```

## Building Docker image

Docker image is describe inside Dockerfile. It's alpine version of python base image, on top of witch we need to install flask and add app file (`app.py`)

To start building custom image use:

```bash
docker build -t moreskovic/flask-demo-api:alpha .
```

**Note**: to be able to execute the next step image must be *tagged* using syntax ***dockerHubUser/imageName:version*** (You need DockerHub account; it's free)

For pushing image to DockerHub run next command: 

```bash
docker push moreskovic/flask-demo-api:alpha
```
## Deployment on minikube

Firstly we create deployment (with 3 pods):
```bash
kubectl apply -f deploy.yaml
```
Next step is to create NodePort service which will expose app to minikube on set port (30007):
```bash
kubectl apply -f nodeport.yaml
```
For getting IP:PORT for connection execute below command:
```bash
echo $(minikube ip):$(kubectl get service flask-np -o jsonpath='{.spec.ports[0].nodePort}')
```

## How to use app

App can be used trough regular web browser or API tool like Postman. Refering to address and port given by previos command response should be: 

```text
This is a test message!
```

By default this is HTTP GET request on root (/) url. Also on root url available is POST method which will simply copy input to output. POST method should be tested using Postman, and body containing text in JSON format as *raw* style.

```json
{
    "Message": "Post Example"
}
```

Example:

![alt](https://user-images.githubusercontent.com/102029624/176196983-47e178f3-4389-45c0-9991-ec65c71404df.png)


### Contributors
- Matija Oreskovic

(c) AG04 Innovative Solutions d.o.o. (2022)