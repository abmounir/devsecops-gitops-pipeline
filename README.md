## DevSecOps pipeline for a simple FastAPI application 

### Description
This repo contains a simple FastAPI application that is used to demonstrate a DevSecOps pipeline. The pipeline is built using GitHub Actions and Azure Devops, and uses the following tools:

- [SonarCloud](https://sonarcloud.io/) for static code analysis and code coverage
- [Trivy](https://trivy.dev/) for container image scanning 
- [OWASP ZAP](https://www.zaproxy.org/) for dynamic application security testing (DAST)
- [Checkov](https://www.checkov.io/) for infrastructure as code (IaC) scanning
- [ArgoCD](https://argoproj.github.io/argo-cd/) for GitOps deployment of the application
- [Kubernetes](https://kubernetes.io/) for container orchestration
- [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) for managed Kubernetes clusters
- [ArgoRollouts](https://argoproj.github.io/argo-rollouts/) for progressive delivery of the application (canary deployments)
  
