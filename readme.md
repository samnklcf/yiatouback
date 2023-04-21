Création de compte :
Pour créer un nouveau compte, vous devez envoyer une requête POST à l'endpoint /creation-2f416677-858f-796a-a221-690e5e4ae75a2f416677-858f-796a-a221-690e5e4ae75a. Dans le corps de la requête, vous devez inclure les champs suivants :

username (obligatoire) : le nom d'utilisateur
email (obligatoire) : l'adresse e-mail
password (obligatoire) : le mot de passe
Exemple de code en utilisant Fetch pour créer un compte :

javascript
Copy code
const createUser = async (username, email, password) => {
const response = await fetch('/let response = await fetch("https://alissadata.pythonanywhere.com/api/token", {
method: "POST",
body: data,
});

let dataUser = await response.json();

    if (response.ok) {
      Cookies.set(
        "2f416677-858f-796a-a221-690e5e4ae75a-token",
        JSON.stringify(dataUser),
        { expires: 7, path: "/" }
      );

}

La réponse renverra un objet JSON avec un jeton d'accès (access) qui sera utilisé pour les requêtes ultérieures. C'est ce token qu'on récupère avec "Cookies.set". Mais le développeur front end peut aussi utiliser le localstorage pour enregistrer ce token.

Authentification :
Pour se connecter à un compte existant, vous devez envoyer une requête POST à l'endpoint /token-auth/. Dans le corps de la requête, vous devez inclure les champs suivants :

username (obligatoire) : le nom d'utilisateur
password (obligatoire) : le mot de passe
Exemple de code en utilisant Fetch pour se connecter à un compte :

javascript
Copy code
const authenticateUser = async (username, password) => {
const response = await fetch('/token-auth/', {
method: 'POST',
headers: {
'Content-Type': 'application/json'
},
body: JSON.stringify({
username: username,
password: password
})
});
const data = await response.json();
return data;
}
La réponse renverra un objet JSON avec un jeton d'accès (access) qui sera utilisé pour les requêtes ultérieures.
