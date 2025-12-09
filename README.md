# Démo Django 6.0 Template Partials

Ce projet est une démonstration minimaliste de la nouvelle fonctionnalité **Template Partials** introduite dans Django 6.0.

## Le concept clé

L'objectif est de montrer comment définir, réutiliser et charger dynamiquement des fragments de HTML **sans jamais créer de fichiers templates séparés**.

Tout se passe dans un seul fichier : `blog/templates/blog/index.html`.

### Fonctionnalités démontrées

1.  **Définition Inline** : Un fragment (une "carte" d'article) est défini directement dans `index.html` avec le tag `{% partialdef card %}`.
2.  **Réutilisation** : Ce même fragment est utilisé pour afficher la liste complète des articles via `{% partial card %}`.
3.  **Rendu Partiel (HTMX)** : Une vue spécifique rend **uniquement** ce fragment à la demande via l'URL, grâce à la syntaxe `index.html#card`.
4.  **Inclusion Inter-Template** : Le partial défini dans `index.html` est réutilisé dans un *autre* fichier template (`home.html`) via `{% include "blog/index.html#card" %}`.

## Comparaison des approches

La démo illustre deux façons de consommer le même contenu :

### 1. Le Lien Classique (`target="_blank"`)
- L'utilisateur clique sur le lien.
- Le navigateur ouvre un nouvel onglet.
- Le serveur rend **uniquement le fragment HTML** de la carte (pas de `<html>`, `<head>`, ou `<body>` complets) car la vue cible `index.html#card`.
- Résultat : Vous voyez le code HTML brut ou rendu minimaliste du partial dans une page blanche.

### 2. L'approche HTMX
- L'utilisateur clique sur le bouton "Charger".
- **HTMX** intercepte le clic et envoie une requête AJAX en arrière-plan.
- Le serveur renvoie **exactement le même fragment HTML** que pour le lien classique.
- **HTMX** prend ce fragment et l'insère directement dans la `<div id="preview-area">` de la page actuelle.
- Résultat : L'interface se met à jour instantanément sans rechargement de page.

C'est la force de Django 6 : **une seule définition de template** sert aux deux cas d'usage.

## Structure

-   **`blog/templates/blog/index.html`** : Contient à la fois la structure de la page ET la définition du partial.
-   **`blog/templates/blog/home.html`** : Démonstration de l'inclusion d'un partial défini dans un autre fichier.
-   **`blog/views.py`** :
    -   `index` : Rend la page complète.
    -   `home` : Rend la page d'accueil qui inclut le partial de `index.html`.
    -   `single_post_partial` : Rend uniquement le partial `#card` pour les requêtes HTMX.
-   **HTMX** : Utilisé pour charger le partial dynamiquement dans une zone d'aperçu sans recharger la page.
-   **Simple.css** : Pour le style, sans écrire de CSS personnalisé.

## Comment tester

1.  Installez les dépendances (Django 6.0+).
2.  Lancez le serveur : `python manage.py runserver`.
3.  Créez quelques articles via l'admin (`/admin`).
4.  Sur la page d'accueil, cliquez sur "Charger (HTMX)" pour voir le serveur extraire et renvoyer juste le fragment HTML de l'article.
