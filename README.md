# Django-Restaurant-rest-api

Cette application est une API de gestion de restaurant construite avec Django, Django REST Framework et Djoser. Elle permet de gérer les catégories de menu, les articles de menu, les paniers, les commandes et les éléments de commande.

## Prérequis

- Python 3.12
- Django 5.1 ou supérieur
- Django REST Framework
- Djoser

## Installation

1. Clonez le dépôt :
   
   - git clone https://github.com/gnoubis/Django-Restaurant-rest-api.git
   - cd Django-Restaurant-rest-api

3. Créez et activez un environnement virtuel :
   - pip install pipenv
   - pipenv shell

4. Installez les dépendances :
 - pipenv install

5. Appliquez les migrations
   
   - python manage.py migrate
6. Créez un superutilisateur pour accéder à l'admin :
   - python manage.py createsuperuser
7. Démarrez le serveur de développement :
   - python manage.py runserver

## Modèles

## Category
- slug: Slug de la catégorie
- title: Titre de la catégorie

## MenuItem
- title: Titre de l'article de menu
- price: Prix de l'article de menu
- featured: Indique si l'article est en vedette
- category: Catégorie à laquelle appartient l'article de menu
  
## Cart
- user: Utilisateur auquel appartient le panier
- menuitem: Article de menu dans le panier
- quantity: Quantité de l'article de menu
- unit_price: Prix unitaire de l'article de menu
- price: Prix total pour la quantité de l'article de menu

## Order
- user: Utilisateur ayant passé la commande
- delivery_crew: Équipe de livraison assignée à la commande
- status: Statut de la commande (livrée ou non)
- total: Montant total de la commande
- date: Date de la commande

## OrderItem
- order: Commande à laquelle appartient l'article
- menuitem: Article de menu commandé
- quantity: Quantité de l'article de menu
- unit_price: Prix unitaire de l'article de menu
- price: Prix total pour la quantité de l'article de menu

## API Endpoints
## Catégories
- GET /categories: Liste des catégories
- POST /categories: Créer une nouvelle catégorie
- GET /categories/{id}: Détails d'une catégorie
- PUT /categories/{id}: Mettre à jour une catégorie
- DELETE /categories/{id}: Supprimer une catégorie

  ## Articles de Menu
- GET /menu-items: Liste des articles de menu
- POST /menu-items: Créer un nouvel article de menu
- GET /menu-items/{id}: Détails d'un article de menu
- PUT /menu-items/{id}: Mettre à jour un article de menu
- DELETE /menu-items/{id}: Supprimer un article de menu

## Paniers
- GET /cart/menu-items: Liste des articles dans le panier
- POST /cart/menu-items: Ajouter un article au panier
- DELETE /cart/menu-items/delete: Supprimer tous les articles du panier
  
## Commandes
- GET /orders: Liste des commandes
- POST /orders: Créer une nouvelle commande
- GET /orders/{id}: Détails d'une commande
- PUT /orders/{id}: Mettre à jour une commande
- DELETE /orders/{id}: Supprimer une commande

## Éléments de Commande
- GET /order-items: Liste des éléments de commande
- POST /order-items: Ajouter un élément de commande
- GET /order-items/{id}: Détails d'un élément de commande
- PUT /order-items/{id}: Mettre à jour un élément de commande
- DELETE /order-items/{id}: Supprimer un élément de commande

## Contribuer
Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.



