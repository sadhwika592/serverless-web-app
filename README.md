# 🚀 Serverless Web Application with CI/CD Pipeline

This project demonstrates how to build a serverless web application using AWS Lambda, API Gateway, and DynamoDB with a fully automated CI/CD pipeline using AWS CodePipeline and CodeBuild.

---

## 🛠 Technologies

- **Language**: Python 3.9
- **AWS Services**: Lambda, API Gateway, DynamoDB, S3, CodePipeline, CodeBuild, IAM, CloudFormation
- **Tools**: Git, Docker (optional), SAM CLI, CloudWatch

---

## 📦 Features

- Submit data to API endpoint → Lambda → DynamoDB
- Monitor activity via CloudWatch
- CI/CD Pipeline for deployment via CodePipeline

---

## ⚙️ Deployment (SAM CLI)

```bash
sam build
sam deploy --guided
