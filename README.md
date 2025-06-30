**Question 1 : Quelles sont les types de couches pouvant composer un
Perceptron multicouches ?**
Il y a l'input, la/les couche.s cachée.s, l'output

**Question 2 : Définissez et différenciez les notions d’Epochs, d’Iterations et de Batch
size.**
Epochs : Représente un passage complet de l'algorithme d'entrainement sur tous les échantillons du dataset d'entrainement. Une epochs contient plusieurs itérations (sauf si Batch Size = taille du dataset).

Iterations : indique le nombre de fois que les paramètres d’un algorithme sont modifiés, une itération implique le 
traitement d’un batch. Le nombre d'itération est égal au nombre d'échantillon dans le dataset / le batch size
Une epoch est un ensemble d'itérations. Une itération traite un batch.

Batch : Lot d'échantillon compris dans chaque epochs, cela permet de ne pas charger toutes les données d'un coup pour eviter un problème de mémoire. Il y a 3 types de batch : Batch gradient descent où le batch est égal au dataset complet. Le Stochastic Gradient Descent où chaque batch contient qu'un seul échantillon. Enfin le Mini-Batch Gradient Descent où le batch est supérieur à 1 et inférieur à la totalité du dataset (généralement 11)


**Question 3 : Qu’est ce que l’hyper-paramètre learning rate ? Quelles sont les conséquences d’un learning rate trop bas ou trop élevé ?**

Learning rate ou taux d'apprentissage est le pourcentage de modification des paramètres de l'algorithme à chaque fin d'itération dans le but de minimiser la fonction de perte. Il a un impacte direct sur la vitesse de convergence et sur les performances finales du modèle. S'il est trop élevé, le processus d'optimisation risque de dépasser la valeur de perte minimale (n'obtiendra pas de résultat stable et optimale), tandis qu'avec un learning rate trop faible, il atteindra un résultat stable et optimale mais avec trop d'itération, il peut ne jamais atteindre la bonne valeur dans un temps acceptable ou encore converger vers un minimum local et non global. Ou encore être juste bloqué dans une zone plane de la fonction de perte 
Pour faire simple, c'est la valeur que l'on utilise pour obtenir un nouveau résultat à chaque itération dans le but de se rapprocher de la valeur à prédire. 


**Question 4 : Définissez la Batch normalization et argumentez son utilisation.**

La Batch normalization est le fait de normaliser les entrées du modèle de deep learning, pas uniquement les premières entrées mais celle de chaque couche pour faciliter l'apprentissage du modèle, cela se nomme ainsi parce que la normalisation se produit sur les batch et pas sur l'ensemble des échantillons. Son utilisation a plusieurs bénéfiques comme la stabilisation du réseau de neurones. La variance étant égale à 1, on évite le décalage de covariance et l'on peut déclarer que le réseau de neurones est stabilisé permettant d'utiliser un learning rate plus élevé et d'accélerer l'entrainement du modèle (l'explosion/la disparition du gradient pendant la backpropagation est évité).
Cela agit également comme un regularizer, les données ayant une même échelle de valeur, elles sont vues comme ayant un lien entre elles


**Question 5 : Qu'est-ce que l'algorithme d'optimisation d'Adam ?**

L'algorithme d'optimisation d'Adam est conçu pour mettre à jour efficacement les poids du réseau pendant le processus de formation en adaptant le taux d'apprentissage pour chaque paramètre individuellement

**Question 8 : Qu'est-ce que l'Early Stopping ?**

Consiste à interrompre l'entraînement d'un modèle d'apprentissage lorsque la perte d'un ensemble de données de validation commence à augmenter et que les performances de généralisation se dégradent

**Question 2.2 et 2.3 : Donnez le principe de fonctionnement d’une couche convolutive. Qu’est ce qu’un filtre de convolution ?
Comment un filtre de convolution est-il appliqué à une image en entrée ? Qu’est ce qui en résulte ? En quoi est-il utile pour la détection
d'objets ?**

Une couche convolutive analyse l'image par zone de pixel (approche locale) et permet de repérer les caractéristiques d'un label sur des zones d'image et garder ces informations en mémoire. Cela permet plus de précision dans la détection et moins d'erreur dans l'apprentissage. Le filtre de convolution est l'outil que la couche utilise pour analyser l'image. Le filtre de convolution est donc appliquer localement par un kernel (3x3, 5x5, etc) en utilisant un stride (généralement 1) et une fonction d'activation (soit défini pour un rôle précis, soit qui évolue avec le temps)

**Question 2.4 : Quelle est la fonction d’activation utilisée par un CNN ? Pourquoi est-elle la plus adaptée pour ce type de réseaux de neurones ?**

Il y a plusieurs fonction d'activation pour un CNN (Relu, Softmax, sigmoïd) mais la plus courante est la relu qui filtre les valeurs négatifs et laisse passer uniquement les valeurs positives. La simplicité de ce modèle évite l'overfitting et le ralentissement du modèle à cause des gradient trop petit qui, une fois multiplié, deviendrait encore plus petit 

**Question 2.5 : Qu’est ce qui arrive à la Feature Map lorsque celle-ci est donnée en paramètre à la fonction d’activation d’un CNN?**

Les features map produites après une couche convolutives se voient appliquées la fonction d'activation relu, qui filtre du coup les valeurs négatives pour ne garder que les valeurs positives, cela permet l'introduction de la non-linéarité dans le modèle, en ayant un gradient constant de 1 cela facilite l'apprentissage du modèle et en mettant toutes les valeurs négatives à 0, cela conduit à des activations creuses qui permettent de rendre le réseau plus efficace

**Question 2.6 et 2.7 : Donnez le principe de fonctionnement d’une couche de Pooling. Il existe différentes opérations de Pooling, citez en au moins deux. Quels sont les avantages de l’utilisation d’une couche de Pooling ?**

La couche de Pooling sert à compresser la valeur d'entrée pour garder que l'information importante, comme la couche de convolution elle fonctionne avec un kernel et en fonction du type de pooling, compresse pour garder une seule information. Le maxpooling garde la plus grande valeur, l'average pooling garde la moyenne des valeurs. Les avantages d'une couche de pooling est une réduction de la charge de calcul en réduissant la dimensionnalité fournissant une forme abstraite de la représentation

**Question 2.8 : La dernière couche d’un CNN est une couche entièrement connectée. Expliquez son fonctionnement. Qu’est ce que reçoit la couche entièrement connectée ?**

Chaque neurones de la couche de sortie reçoit toutes les sorties de la couche précédentes. Ils prennent la somme pondérée des neuronnes de la couche précédentes, chaque neurones applique un biais puis une fonction d'activation 

**Question 2.9 : Détaillez les raisons pour lesquelles un réseau de neurones convolutif est préféré à un réseau de neurones dense pour une tâche de classification d'images.**

Un réseau de neurones convolutif est plus rapide et précis pour la classification d'image, n'ayant pas besoin d'analyser toute l'image en même temps pour classifier l'image mais le faisant kernel par kernel, l'apprentissage du modèle est plus efficace et rapide
