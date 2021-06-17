pierre = {'ltp':[14,15,16],'uml':[14,12,15], 'sda':[12,15,15], 'base':[2,8,14], 'reseau':[14,14,15]}
resultat = pierre['ltp'][0] +pierre['ltp'][1]+pierre['ltp'][2]+pierre['sda'][0] +pierre['sda'][1]+pierre['sda'][2]+pierre['base'][0] +pierre['base'][1]+pierre['base'][2]+pierre['reseau'][0] +pierre['reseau'][1]+pierre['reseau'][2]+pierre['uml'][0] +pierre['uml'][1]+pierre['uml'][2]
moyenne = resultat/15
print(moyenne)
