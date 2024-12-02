# Ali's API challenge
An exercise proposed by Ali to get to know each other

## Instructions

**Projet Backend dev**

Dans le cadre du développement de la plateforme mobile et Web sur la thématique recrutement, nous comptons exposer une API de type REST basée sur le framework Django/Python.

Les livrables du projet sont la réalisation d'une application Django/Python qui comprend :

- un ou plusieurs modèles liés à des tables dans une bases de données PostgreSQL
- un ou plusieurs Endpoints API dédiés au candidat afin de renseigner et consulter ses informations personnelles,
- un ou plusieurs Endpoints API dédiés au recruteur afin de consulter les informations des candidats,
- une interface OpenAPI de type swagger servant de documentation pour les developpeurs Frontend.

**Exigences**

- Utilisation de Visual Studio Code (VSCode) (sauf Simon).
- Conception du module avec des diagrammes UML sur DrawIO
- Suivi de la réalisation, du début jusqu'à la fin, sur un repo Github public.

## Models chosen

- For users: CustomUser (general), Candidate, Recruiter
- For job offers: JobOffer
![Classes diagram](docs/images/classes_diag.png)

## API endpoints
![Endpoints](docs/images/endpoints.png)
