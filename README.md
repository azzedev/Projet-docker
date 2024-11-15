README - TP DOCKER EPSI TOULOUSE

Introduction :

L'objectif de ce TP est de déployer une application web complète en utilisant docker et docker
compose. Vous allez avoir à votre disposition une application avec un frontend et un backend. Il
vous faudra créer les Dockerfiles, définir le comportement de la stack grâce à docker compose en
ajoutant les services manquants.


Structure du Projet :

dossier de bases :
    -un dossier backend avec une api flask
    -un dossier frontend avec react
modifications apporté :
    -modification de config.py pour ajouter mysql
    -ajout d'un dockerfile dans backend et frontend
    -déplacement du .env dans backend vers la racines pour avoir des variables d'environnement globale
    -création dun docker-compose a la racine du projet.


Partie Backend :
    -Config.py :
        DevelopmentConfig : pour une base de données MySQL lors du développement.

    -Dockefile :
        flask db upgrade pour exécuter les migrations au démarages

Partie Frontend :
    -DockerFile

Racine du projet :

    Docker-compose :
        -services utilisé :
            -Backend. => Dockerfile
            -Frontend. => Dockerfile
            -MySQL. => services 
            -phpMyAdmin. => services
            -Traefik. => services

Pour éviter une redondance je vais expliquer le fonctionnement d'un dockerfile (pour l'exemple celui du backend)

On utilise FROM pour utiliser l'image officiel de notre techno ici : python:3.9.20-bullseye

On crée ensuite un Workdir qu'on a appellé App pour une certaine lisibilité dans notre conteneur

On copie l'ensemble de notre requirement.txt dans app pour le récupéré dans notre conteneur

On fait l'installation de l'ensemble des dépendences nécéssaire au projet

On copie ensuide l'ensemble de tout les fichiers crée dans notre App (COPY . /app)

On expose ensuite le port requis pour faire fonctionner l'app (ici on expose 5000 The default port for the Flask application is 5000) source => https://flask.palletsprojects.com/en/stable/server/

Enfin on exécute chaqune des commandes nécéssaire en sachant que j'ai aouté une commande permettant de faire les migrations directment au lancement de compose up (CMD ["sh", "-c", "flask db upgrade && flask run --host=0.0.0.0 --port=5000"])

Pour ce qui est du fichier docker-compose on utilise les dockerfile déja présent dans frontend et backend pour les 2 services et ensuite on a crée 3 services :

    -mysql :
        -Service pour la base de données,
        (meme principe pour l'image mais on a ajouter les variables d'environnement et un **volume permettant de persister les données si le conteneurs est supprimé**)
        on a aussi mis en places des healthcheck pour vérifier que le services fonctionnes.
        Pour le network je l'ai laissé par défaut en bridge (si je ne précise pas le webnet c'est bridge par défaut)

    -phpmyadmin :
        -Interface pour administrer la base de données :

    -traefik :
        -Reverse proxy (J'ai reussis a crée une url personnalisé pour api et localhost de base mais je n'y arrive 
        pas pour phpmyadmin et le dashboard ce sera un axe d'améliorations pour le projet)


Guide d'utilisation pour lancer le projet a l'aide de docker :

cd dans le projet a la racine 

docker-compose build =>
docker-compose up =>
docker ps (pour vérifié l'état des services)

Une fois que tout les services sont healthy voici les urls pour accéder aux différents services :
    -Frontend : http://localhost
    -Backend : http://localhost/apizzed
    -phpMyAdmin : http://localhost:8081 (ici le nom d'utilisateur et le mot de passe sont dans le .env)
    -Traefik Dashboard : http://localhost:8080

(j'avais eu une erreur lorsque j'ai changé des variables d'environnement car le script initial ne se lancer pas !!
penser a supprimer les volumes si l'on veut changer les variables d'environnement car car MySQL détecte que la base de données est déjà initialisée)




