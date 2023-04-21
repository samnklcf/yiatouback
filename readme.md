Création de compte :
Pour créer un nouveau compte, vous devez envoyer une requête POST à l'endpoint /creation-2f416677-858f-796a-a221-690e5e4ae75a2f416677-858f-796a-a221-690e5e4ae75a. Dans le corps de la requête, vous devez inclure les champs suivants :

username (obligatoire) : le nom d'utilisateur
email (obligatoire) : l'adresse e-mail
password (obligatoire) : le mot de passe
Exemple de code en utilisant Fetch pour créer un compte :

        function Login() {
        // Initialisation des états d'erreur et de chargement de la page
        const [erreur, SetErreur] = useState(false);
        const [top, SetTop] = useState(false);

        // Création de deux références pour stocker les valeurs des champs de connexion
        const username = useRef();
        const password = useRef();

        // Fonction pour gérer la soumission du formulaire de connexion
        const handleForm = async (e) => {
            e.preventDefault(); // Empêche le comportement par défaut de l'événement de soumission

            // Création d'un objet FormData pour stocker les données du formulaire
            const data = new FormData();
            data.append("username", username.current.value); // Ajout de la valeur du champ d'identifiant
            data.append("password", password.current.value); // Ajout de la valeur du champ de mot de passe
            
            SetTop(true); // Affichage du spinner de chargement

            // Envoi de la requête de connexion au serveur avec les données du formulaire
            let response = await fetch("https://yiatoutest.pythonanywhere.com/api/token", {
            method: "POST",
            body: data,
            });

            // Récupération des données de réponse du serveur
            let dataUser = await response.json();

            if (response.ok) { // Si la réponse est valide (status 2xx)
            // Enregistrement du token d'authentification dans un cookie
            Cookies.set(
                "2f416677-858f-796a-a221-690e5e4ae75a-token",
                JSON.stringify(dataUser),
                { expires: 7, path: "/" }
            );
            
            // Rechargement de la page
            window.location.reload();
            } else { // Si la réponse est invalide (status 404 ou 500)
            SetErreur(true); // Affichage de l'erreur
            SetTop(false); // Masquage du spinner de chargement
            }
        };
        }


La réponse renverra un objet JSON avec un jeton d'accès (access) qui sera utilisé pour les requêtes ultérieures. C'est ce token qu'on récupère avec "Cookies.set". Mais le développeur front end peut aussi utiliser le localstorage pour enregistrer ce token.

Authentification :
Pour se connecter à un compte existant, vous devez envoyer une requête POST à l'endpoint /token-auth/. Dans le corps de la requête, vous devez inclure les champs suivants :

username (obligatoire) : le nom d'utilisateur
password (obligatoire) : le mot de passe
Exemple de code en utilisant Fetch pour se connecter à un compte :

    const handleForm = async (e) => { // déclare une fonction asynchrone qui sera exécutée lors de la soumission du formulaire

            e.preventDefault(); // empêche la soumission du formulaire de se produire par défaut

            const data = new FormData(); // crée un nouvel objet FormData qui stockera les données du formulaire
            data.append("username", username.current.value); // ajoute la valeur du champ "username" du formulaire à l'objet FormData
            data.append("email", email.current.value); // ajoute la valeur du champ "email" du formulaire à l'objet FormData
            data.append("password", password.current.value); // ajoute la valeur du champ "password" du formulaire à l'objet FormData

            SetTop(true); // met à jour l'état de la variable "Top" à true

            let response = await fetch( // envoie une requête POST à l'endpoint de création de compte utilisateur de l'API
            "https://yiatoutest.pythonanywhere.com/creation-2f416677-858f-796a-a221-690e5e4ae75a2f416677-858f-796a-a221-690e5e4ae75a",
            {
                method: "POST",
                body: data,
            }
            );
            let dataUser = await response.json(); // récupère les données de réponse sous forme d'objet JSON

            if (response.ok) { // si la réponse est valide (statut 200-299)
            Cookies.set( // stocke le jeton d'accès dans un cookie nommé "2f416677-858f-796a-a221-690e5e4ae75a-token"
                "2f416677-858f-796a-a221-690e5e4ae75a-token",
                JSON.stringify(dataUser),
                { expires: 7, path: "/" }
            );

            Cookies.set( // stocke le nom d'utilisateur dans un cookie nommé "2f416677-858f-796a-a221-690e5e4ae75a-Cooktoken"
                "2f416677-858f-796a-a221-690e5e4ae75a-Cooktoken",
                JSON.stringify({ nom: username.current.value }),
                { expires: 7, path: "/" }
            );

            window.location.reload(); // recharge la page après avoir stocké les cookies
            } else { // si la réponse n'est pas valide
            SetErreur(dataUser); // met à jour l'état de la variable "Erreur" avec les données de réponse de l'API
            SetTop(false); // met à jour l'état de la variable "Top" à false
            }
        };
La réponse renverra un objet JSON avec un jeton d'accès (access) qui sera utilisé pour les requêtes ultérieures.
