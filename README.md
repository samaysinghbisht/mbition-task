<h2>Steps to deploy and test the application: </h2>

1. Clone the repository
2. Have AWS CLI configured
3. Eksctl should be installed 
4. Create EKS Cluster by running the command: "eksctl create cluster --name mbition-cluster --region eu-central-1 --nodegroup-name linux-nodes --node-type t2.micro --nodes 2"
5. Delete the EKS cluster by running the command: "eksctl delete cluster --region=eu-central-1 --name=mbition-cluster"

<h3>Run the app locally:</h3>

There are three ways to run the application locally:
- Run using Python, for that use the command: "flask run --host=0.0.0.0 --port=(port-number)"
- Run using docker:
    - Build the image: "docker build -t mBition .
    - Run the image in a container with port mapping: "docker run -p (host-port):5000 mBition-app" 
    - Access the application on localhost:(host-port)
- Run using kubernetes:
    - Use the manifest in k8s folder.
    - Run below commands:
        - kubectl apply -f k8s/namespace.yaml
        - kubectl apply -f k8s/deployment.yaml
        - kubectl apply -f k8s/service.yaml
    - Port forward the service to a host port(let's say 4000): 
        - kubectl port-forward svc/mBition-service -n mBition 4000:80
    - Access the application on locahost:4000

<h3>Running Unit Tests</h3>

To run the Unit Tests locally, please execute this command in the root directory:
- pip install -r requirements.txt
- python -m unittest discover -s tests

<h3> Deploy to EKS</h3>
Once the cluster is deployed, push the changes to github repo, the pipeline will run automatically.

In Addition, please create below 4 repository variables:
- DOCKER_USER
- DOCKER_PASSWORD
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

Let the pipeline do it's thing.