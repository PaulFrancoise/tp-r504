#!/bin/bash

# Lancer le conteneur avec les paramètres spécifiés
docker run -d \
  --name tp4-app \
  --network net-tp4 \
  -p 5000:5000 \
  im-tp4

