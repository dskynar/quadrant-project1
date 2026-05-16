# AWS EC2 Post-Deployment Setup Guide

This guide details the steps to configure an Ubuntu 24.04 LTS EC2 instance with Docker, a localized Python virtual environment, and the necessary network configurations to host a Qdrant vector database accessible from your local development machine.

---

## Part 1: Establish Remote Connection
Access your running EC2 instance via SSH using your generated private key:

```bash
ssh -i ~/.ssh/my-ec2-key.pem ubuntu@YOUR_EC2_PUBLIC_IP

```

---

## Part 2: Container Engine Installation

Install the Docker runtime engine directly from the official Ubuntu repositories and configure non-root user permissions.

```bash
# 1. Synchronize package indexes and apply available patches
sudo apt update && sudo apt upgrade -y

# 2. Install the core Docker engine and composition system tools
sudo apt install docker.io docker-compose -y

# 3. Initialize and enable the background daemon process
sudo systemctl enable --now docker

# 4. Grant execution permissions to the default system user
sudo usermod -aG docker $USER

```

> ⚠️ **CRITICAL CONFIGURATION:** You must terminate your current SSH session and reconnect for the group membership updates to apply to your shell terminal environment:
> ```bash
> exit
> ssh -i ~/.ssh/my-ec2-key.pem ubuntu@YOUR_EC2_PUBLIC_IP
> 
> ```
> 
> 

---

## Part 3: Python Environment Mirroring

Isolate dependencies by creating a dedicated python virtual environment matching your local laptop execution space.

```bash
# 1. Provision system package manager tools and environment abstraction modules
sudo apt install python3-pip python3-venv -y

# 2. Initialize project workspace and drop into directory
mkdir ~/quadrant-project1 && cd ~/quadrant-project1

# 3. Spin up an isolated virtual environment shell matching local parameters
python3 -m venv quadrant-project1

# 4. Source the binary engine execution path
source quadrant-project1/bin/activate

```

---

## Part 4: Qdrant Database Deployment

Pull down and run the Qdrant database engine container. This command includes a detached engine flag to keep the process running safely in the background layer.

```bash
# 1. Map out local persistent disk volume paths on the filesystem
mkdir qdrant_storage

# 2. Initialize detached container execution with targeted network ports
docker run -d --name qdrant \
    -p 6333:6333 -p 6334:6334 \
    -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
    qdrant/qdrant

```

---

## Part 5: Infrastructure as Code (Network Firewalls)

Update your local tracking architecture files to securely open your ingress rules to the application port.

Add this configuration directly inside your **local laptop's** `main.tf` file inside the `aws_security_group` resource block:

```hcl
  # Network Ingress Ruleset: Qdrant Engine REST Routing API
  ingress {
    description = "Allow inbound Qdrant API operations from local laptop"
    from_port   = 6333
    to_port     = 6333
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # For maximum security, restrict to your exact local source IP: ["YOUR_LAPTOP_IP/32"]
  }

```

Apply your infrastructure updates programmatically from your local workspace:

```bash
terraform plan
terraform apply

```

---

## Part 6: Connectivity & Verification Testing

Verify structural integration by querying the cluster runtime state from a terminal session on your **local machine**:

```bash
curl http://YOUR_EC2_PUBLIC_IP:6333/info

```

```

```
