# Restaurant API

FastAPI restaurant order management application containerized with Docker and deployed via GitHub Actions CI/CD to AWS EC2.

## Project Structure

```
restaurant-api/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── app.py
├── templates/
│   └── index.html
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── orders.json
└── README.md
```

## Setup

1. Push this repository to GitHub.
2. Add the following secrets in your GitHub repository settings:
   - `EC2_HOST`: Public IP or DNS of your EC2 instance.
   - `EC2_USERNAME`: SSH username (e.g., `ubuntu`).
   - `EC2_SSH_KEY`: Private SSH key for authenticating into EC2.
3. Ensure Docker and Docker Compose are installed on your EC2 instance.
4. Push to `main` to trigger the deployment workflow.

## Manual Run

```bash
sudo docker-compose up --build -d
```

Then visit `http://<ec2-public-ip>/`.
# Automated Deployment Active!
