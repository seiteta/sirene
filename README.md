Première analyse de la [base Sirene des entreprises](https://www.data.gouv.fr/fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/) publiée en Open Data sur data.gouv.fr.

## Quickstart

Pour générer, le fichier [prenom.csv](https://github.com/seiteta/sirene/blob/master/prenoms.csv):

1. Transformer l'encodage du fichier csv d'origine avec la commande bash suivante `iconv -f ISO-8859-15 -t utf-8 sirc-17804_9075_14209_201612_L_M_20170104_171522721.csv > sirc-utf8.csv`
2. Lancer le script [name_counter.py](https://github.com/seiteta/sirene/blob/master/name_counter.py)

## Stats

* La base "stock" compte 10 538 425 lignes.
* 3 999 651 de ces lignes contiennent un prénom.
* Il y a 141 950 prénoms différents mais 102 781 prénoms ne sont portés qu'une seule fois.
