#!/usr/bin/env bash
set -euo pipefail

# Usage: PROJECT=your-gcp-project-id ./deploy.sh
PROJECT=${PROJECT:-}
if [ -z "${PROJECT}" ]; then
  echo "Please set PROJECT environment variable to your GCP project id. Example: PROJECT=my-project ./deploy.sh"
  exit 1
fi

IMAGE=gcr.io/${PROJECT}/star-wars-api
SERVICE=star-wars-api
REGION=${REGION:-us-central1}

echo "Building image ${IMAGE}..."
gcloud builds submit --tag ${IMAGE}

echo "Deploying to Cloud Run (${REGION})..."
gcloud run deploy ${SERVICE} \
  --image ${IMAGE} \
  --platform managed \
  --region ${REGION} \
  --allow-unauthenticated

echo "Deployment complete."
