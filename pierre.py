pierre = {'ltp':[14,15,16],'uml':[14,12,15], 'sda':[12,15,15], 'base':[2,8,14], 'reseau':[14,14,15]}
resultat = pierre['ltp'][0] +pierre['ltp'][1]+pierre['ltp'][2]+pierre['sda'][0] +pierre['sda'][1]+pierre['sda'][2]+pierre['base'][0] +pierre['base'][1]+pierre['base'][2]+pierre['reseau'][0] +pierre['reseau'][1]+pierre['reseau'][2]+pierre['uml'][0] +pierre['uml'][1]+pierre['uml'][2]
moyenne = resultat/15
print(moyenne)

#E0
listeliste = [1,2,3,4,5,6,7,8,9,10]
liste.append(11)
liste.extend([22,23])
print(liste)
L2 = []
L1 = []
L2.append(liste.pop(0))
L1.append(liste.pop(0))
L2.append(liste.pop(0))
L1.append(liste.pop(0))
L2.append(liste.pop(0))
L1.append(liste.pop(0))
L2.append(liste.pop(0))
L1.append(liste.pop(0))
L2.append(liste.pop(0))
L1.append(liste.pop(0))
L2.append(liste.pop(0))
L1.append(liste.pop(0))
L2.append(liste.pop(0))
print(L1)
print(L2)
liste = [1,2,3,4,5,6,7,8,9,10]
liste.pop(3)

#E1
d = {'nom':'Dupuis','prenom':'Jacque','age':30}
d['prenom'] = 'Jacques'
print(d)
print(d.keys())
print(d.values())
print(d.items())
phrase = d['prenom']+" "+d['nom']+" "+" a "+str(d['age'])
print(phrase)
