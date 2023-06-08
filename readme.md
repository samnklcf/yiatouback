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

    