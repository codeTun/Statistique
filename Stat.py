import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Paramètres de la distribution exponentielle
scale = 1000  # Échelle, en heures

# Générer un ensemble de données de durées de vie à partir d'une distribution exponentielle
durees_vie = np.random.exponential(scale=scale, size=1000)

# Calculer la moyenne, la médiane et le mode des durées de vie
moyenne = np.mean(durees_vie)
mediane = np.median(durees_vie)
mode = stats.mode(durees_vie)

# Calculer l'écart type et la variance des durées de vie
ecart_type = np.std(durees_vie)
variance = np.var(durees_vie)

# Créer un histogramme des durées de vie
plt.hist(durees_vie, bins=50)
plt.xlabel('Durée de vie (heures)')
plt.ylabel('Fréquence')
plt.title('Histogramme des durées de vie')
plt.show()

# Afficher les résultats de l'analyse descriptive
print("Moyenne : ", moyenne)
print("Médiane : ", mediane)
print("Mode : ", mode.mode[0])
print("Écart type : ", ecart_type)
print("Variance : ", variance)