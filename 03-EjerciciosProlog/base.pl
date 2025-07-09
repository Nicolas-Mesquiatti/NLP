asesino(butch).
casados(mia, marsellus).
casados(marsellus, mia).
muerto(zed).
buen_bailarin(vincent).
masaje_pies(vincent, mia).
sabrosa(pizza).
nutritiva(ensalada).
mata_todos(marsellus, X):- masaje_pies(X,mia).
ama(mia,X):- buen_bailarin(X).
come(jules,X):- nutritiva(X); sabrosa(X).

