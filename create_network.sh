#!/bin/bash

# Créer un réseau Docker de type bridge avec le nom "net-tp4"
docker network create --driver bridge net-tp4

# Vérifier si le réseau a été créé
docker network ls | grep net-tp4

# Afficher un message si le réseau est bien créé
if docker network ls | grep -q net-tp4; then
  echo "Le réseau 'net-tp4' a été créé avec succès."
else
  echo "Le réseau 'net-tp4' n'a pas pu être créé."
fi
