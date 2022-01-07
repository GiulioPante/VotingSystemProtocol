# @GAME THEORY 2021/22 Giulio Pante
# Priority assignment program
import votelib.evaluate
import votelib.evaluate.approval
import votelib.evaluate.sequential
import votelib.evaluate.condorcet
import votelib.evaluate.proportional
import votelib.evaluate.auxiliary
import votelib.evaluate.core
import votelib.convert
import votelib.component.rankscore
import votelib.component.quota
import os
import random
import matplotlib.pyplot as plt
# clear terminal
os.system('cls||clear')

def stampa(dictionary):
	# stampa dizionario
	for el in dictionary.items():
		print(el[0],":",el[1])
	print()

def BordaCount(voti):
	eRank = votelib.component.rankscore.Borda(base=0)
	eConvert = votelib.convert.RankedToPositionalVotes(eRank, unranked_scoring='zero')
	eEvaluate = votelib.evaluate.core.Plurality()
	winnerBorda=eEvaluate.evaluate(eConvert.convert(voti))[0]
	# ci sono più candidati?
	unTier = votelib.evaluate.core.Tie()
	winnerBorda = min(unTier.break_by_list(winnerBorda,[]))
	if winnerBorda=='A':
		WINNERSBORDA[0]+=1
	elif winnerBorda=='B':
		WINNERSBORDA[1]+=1
	elif winnerBorda=='C':
		WINNERSBORDA[2]+=1
	elif winnerBorda=='D':
		WINNERSBORDA[3]+=1
	elif winnerBorda=='E':
		WINNERSBORDA[4]+=1
	elif winnerBorda=='F':
		WINNERSBORDA[5]+=1
	elif winnerBorda=='G':
		WINNERSBORDA[6]+=1
	elif winnerBorda=='H':
		WINNERSBORDA[7]+=1
		print(voti)

def Plurality(voti):
	eRank = votelib.component.rankscore.FixedTop(1)
	# questo econvert va sia con borda rank sia con fixed top a seconda di cosa voglio e alla fine plurality
	eConvert = votelib.convert.RankedToPositionalVotes(eRank, unranked_scoring='zero')
	eEvaluate = votelib.evaluate.core.Plurality()
	winnerPlurality = eEvaluate.evaluate(eConvert.convert(voti))[0]
	# ci sono più candidati?
	unTier = votelib.evaluate.core.Tie()
	winnerPlurality = min(unTier.break_by_list(winnerPlurality,[]))
	if winnerPlurality=='A':
		WINNERSPLURALITY[0]+=1
	elif winnerPlurality=='B':
		WINNERSPLURALITY[1]+=1
	elif winnerPlurality=='C':
		WINNERSPLURALITY[2]+=1
	elif winnerPlurality=='D':
		WINNERSPLURALITY[3]+=1
	elif winnerPlurality=='E':
		WINNERSPLURALITY[4]+=1
	elif winnerPlurality=='F':
		WINNERSPLURALITY[5]+=1
	elif winnerPlurality=='G':
		WINNERSPLURALITY[6]+=1
	elif winnerPlurality=='H':
		WINNERSPLURALITY[7]+=1

def CondorcetWinner(voti):
	eConvert = votelib.convert.RankedToCondorcetVotes(unranked_at_bottom=True)
	eEvaluate = votelib.evaluate.condorcet.CondorcetWinner()
	if eEvaluate.evaluate(eConvert.convert(voti))!=[]:
		condorcetWinner = eEvaluate.evaluate(eConvert.convert(voti))[0]
	elif eEvaluate.evaluate(eConvert.convert(voti))==[]:
		condorcetWinner = 'NO CONDORCET'

	if condorcetWinner=='A':
		WINNERSCONDORCET[0]+=1
	elif condorcetWinner=='B':
		WINNERSCONDORCET[1]+=1
	elif condorcetWinner=='C':
		WINNERSCONDORCET[2]+=1
	elif condorcetWinner=='D':
		WINNERSCONDORCET[3]+=1
	elif condorcetWinner=='E':
		WINNERSCONDORCET[4]+=1
	elif condorcetWinner=='F':
		WINNERSCONDORCET[5]+=1
	elif condorcetWinner=='G':
		WINNERSCONDORCET[6]+=1
	elif condorcetWinner=='H':
		WINNERSCONDORCET[7]+=1

def TopApproval(voti):
	# top 2-3-4 approval
	for top_approval in range(2,5):
		seq=[1 for i in range(top_approval)]
		eRank = votelib.component.rankscore.SequenceBased(seq)
		eConvert = votelib.convert.RankedToPositionalVotes(eRank, unranked_scoring='zero')
		eEvaluate = votelib.evaluate.core.Plurality()
		topwinner=eEvaluate.evaluate(eConvert.convert(voti))[0]
		# ci sono più candidati?
		unTier = votelib.evaluate.core.Tie()
		topwinner = min(unTier.break_by_list(topwinner,[]))
		if topwinner=='A':
			WINNERSAPPROVAL[top_approval-2][0]+=1
		elif topwinner=='B':
			WINNERSAPPROVAL[top_approval-2][1]+=1
		elif topwinner=='C':
			WINNERSAPPROVAL[top_approval-2][2]+=1
		elif topwinner=='D':
			WINNERSAPPROVAL[top_approval-2][3]+=1
		elif topwinner=='E':
			WINNERSAPPROVAL[top_approval-2][4]+=1
		elif topwinner=='F':
			WINNERSAPPROVAL[top_approval-2][5]+=1
		elif topwinner=='G':
			WINNERSAPPROVAL[top_approval-2][6]+=1
		elif topwinner=='H':
			WINNERSAPPROVAL[top_approval-2][7]+=1

def TwoPhaseRunoff(voti):
	top_approval=1
	seq=[1 for i in range(top_approval)]
	eRank = votelib.component.rankscore.SequenceBased(seq)
	eConvert = votelib.convert.RankedToPositionalVotes(eRank, unranked_scoring='zero')
	eEvaluate = votelib.evaluate.auxiliary.InputOrderSelector()
	candidati=eEvaluate.evaluate(eConvert.convert(voti),n_seats=2)
	dropvoti={}
	for k,v in voti.items():
		keys = list(k)
		keys2=keys.copy() # se rimuovo elementi dalla lista che sto scorrendo fa cose strane ahah
		for element in keys2:
			if (element != candidati[0]) and (element != candidati[1]):
				keys.remove(element)
		keys=tuple(keys)
		if keys not in dropvoti:
			dropvoti[keys]=v
		else:
			dropvoti[keys]+=v
	top_approval=1
	seq=[1 for i in range(top_approval)]
	eRank = votelib.component.rankscore.SequenceBased(seq)
	eConvert = votelib.convert.RankedToPositionalVotes(eRank, unranked_scoring='zero')
	eEvaluate = votelib.evaluate.auxiliary.InputOrderSelector()
	twophaserunoffwinner = eEvaluate.evaluate(eConvert.convert(dropvoti),n_seats=1)[0]
	if twophaserunoffwinner=='A':
		WINNERSTWOPHASE[0]+=1
	elif twophaserunoffwinner=='B':
		WINNERSTWOPHASE[1]+=1
	elif twophaserunoffwinner=='C':
		WINNERSTWOPHASE[2]+=1
	elif twophaserunoffwinner=='D':
		WINNERSTWOPHASE[3]+=1
	elif twophaserunoffwinner=='E':
		WINNERSTWOPHASE[4]+=1
	elif twophaserunoffwinner=='F':
		WINNERSTWOPHASE[5]+=1
	elif twophaserunoffwinner=='G':
		WINNERSTWOPHASE[6]+=1
	elif twophaserunoffwinner=='H':
		WINNERSTWOPHASE[7]+=1

def BordaWithDropout(voti):
	# scelgo a caso un device da eliminare
	dropout = random.choice(orderedDevices)
	dropvoti={}
	for k,v in voti.items():
		if dropout in k:
			# se c'è l'elemento da eliminare lo elimino
			keys=list(k)
			keys.remove(dropout)
			keys=tuple(keys)
		# bisogna vedere se c'è già la lista in dropvoti
		# e in caso affermativo aggiungo i voti della lista
		# nuova a quella esistente
		if keys not in dropvoti:
			dropvoti[keys]=v
		else:
			dropvoti[keys]+=v
	eRank = votelib.component.rankscore.Borda(base=0)
	eConvert = votelib.convert.RankedToPositionalVotes(eRank, unranked_scoring='zero')
	eEvaluate = votelib.evaluate.core.Plurality()
	winnerBordaDropout = eEvaluate.evaluate(eConvert.convert(dropvoti))[0]
	# ci sono più candidati?
	unTier = votelib.evaluate.core.Tie()
	winnerBordaDropout = min(unTier.break_by_list(winnerBordaDropout,[]))
	if winnerBordaDropout=='A':
		WINNERSRANDOMBORDA[0]+=1
	elif winnerBordaDropout=='B':
		WINNERSRANDOMBORDA[1]+=1
	elif winnerBordaDropout=='C':
		WINNERSRANDOMBORDA[2]+=1
	elif winnerBordaDropout=='D':
		WINNERSRANDOMBORDA[3]+=1
	elif winnerBordaDropout=='E':
		WINNERSRANDOMBORDA[4]+=1
	elif winnerBordaDropout=='F':
		WINNERSRANDOMBORDA[5]+=1
	elif winnerBordaDropout=='G':
		WINNERSRANDOMBORDA[6]+=1
	elif winnerBordaDropout=='H':
		WINNERSRANDOMBORDA[7]+=1
		# print("dropped",dropout)
		# stampa(voti)
		# stampa(dropvoti)

def barPlot(lista,nome,esperimento):
	"""
	Parametri:
	lista: la lista delle frequenze di vittoria per ogni nodo

	Output:
	Barplot che conta il numero di vittorie per ogni nodo
	"""
	fig, ax = plt.subplots(figsize=(6,4))
	plt.bar([100,90,80,70,60,50,40,30], lista, width=10, edgecolor="dimgrey", color=["indianred", "lightsalmon"])

	tit = "Victory frequency for "+nome+"\n"+str(esperimento)+" visible devices"
	plt.title(tit)
	plt.ylabel("N. of victories")
	plt.xlabel("BitRate")
	plt.grid(axis="y")
	# plt.show()
	nomefile="Plots/"+nome+"/"+nome+" "+str(esperimento)+".png"
	# print(nomefile)
	plt.savefig(nomefile)



# LISTA DI DEVICE ORDINATI IN BASE AL BITRATE
orderedDevices = ['A','B','C','D','E','F','G','H']
dictVoti={}
for o in orderedDevices:
	dictVoti[tuple(o)]=0
initialDevices = [(100,'A'),(90,'B'),(80,'C'),(70,'D'),(60,'E'),(50,'F'),(40,'G'),(30,'H')]
n=len(initialDevices) # number of devices
# inizializzo un dizionario che conterrà le liste di visibilità di ogni nodo
visibilityDict = {}



exp = []
for i in range(0,n):
	for j in range(0,n):
		if(j<i+1):
			exp.append(range(j,i+1))

for esperimento in exp:
	WINNERSPLURALITY = [0 for i in range(0,n)]
	WINNERSBORDA = [0 for i in range(0,n)]
	WINNERSCONDORCET = [0 for i in range(0,n)]
	WINNERSRUNOFF = [0 for i in range(0,n)]
	W2APPROVAL = [0 for i in range(0,n)]
	W3APPROVAL = [0 for i in range(0,n)]
	W4APPROVAL = [0 for i in range(0,n)]
	WINNERSAPPROVAL = [W2APPROVAL,W3APPROVAL,W4APPROVAL]
	WINNERSTWOPHASE = [0 for i in range(0,n)]
	WINNERSRANDOMBORDA = [0 for i in range(0,n)]
	for giro in range(0,10000):
		# random.seed(12)
		scelte=[i for i in esperimento]
		for d in initialDevices:
			# inizializzo le liste di visibilità (ogni nodo all'inizio vede se stesso)
			visibilityDict[d]=[d]
			devices = initialDevices.copy()
			# rimuovo dalla lista dei device quello già inserito (per ogni nodo diverso) 
			devices.remove(d)
			# qui usa la funzione choice per selezionare un elemento random in devices in modo da avere elementi diversi (senza reinserimento!!!)
			# https://datagy.io/python-random-element-from-list/
			# uso un k diverso per ogni giro del for esterno
			
			# a_caso serve per avere liste di visibilità lunghe diverse
			# sceglie un numero compreso tra 0 e n (->numero di devices)
			a_caso=random.choice(scelte)
			# elementi è un campionamento senza reinserimento di "a_caso" devices
			elementi = random.sample(devices, k=a_caso)
			for el in elementi:
				visibilityDict[d].append(el)

		# ordino gli elemnti della lista di visibilità in base al payload
		for l in visibilityDict.values():
			l.sort(reverse=True)
		# print("SORTED DICT: ")
		# stampa(visibilityDict)

		# ora devo stampare le liste in ordine e bene
		liste=[]
		for i in visibilityDict.values():
			listanodi=[]
			appoggio=orderedDevices.copy()
			for payl,node in i:
				# inserisco il nodo nella lista
				listanodi.append(node)
				# rimuovo il nodo dal vettore di appoggio
				# che è una copia della lista dei vettori ordinati
				appoggio.remove(node)

			if len(listanodi)!=8:
				for a in appoggio:
					#completo la lista con i nodi che non ci sono, ordinati
					listanodi.append(a) #RIMETTERE QUESTO PER AVERE LISTE COMPLETE!
			# inserisco la lista nella lista di liste
			liste.append(listanodi)

		# metto in un array le liste con le varie occorrenze
		poss=[]
		occ=[]
		for lista in liste:
			if lista not in poss:
				poss.append(lista)
				occorrenze=liste.count(lista)
				occ.append(occorrenze)

		# metto il tutto in un dizionario per usare votelib
		voti={}
		for i in range(len(poss)):
			voti[tuple(poss[i])] = occ[i]
		# print("Liste ordinate:")
		# stampa(voti)

	########################################

		Plurality(voti)
		BordaCount(voti)
		CondorcetWinner(voti)
		TopApproval(voti)
		TwoPhaseRunoff(voti)
		BordaWithDropout(voti)

	print()
	print("ESPERIMENTO:",esperimento,'\n')
	# print("PLURALITY")
	# print(WINNERSPLURALITY)
	barPlot(WINNERSPLURALITY,'Plurality',esperimento)

	# print("\nBORDA COUNT")
	# print(WINNERSBORDA)
	barPlot(WINNERSBORDA,'Borda Count',esperimento)

	# print("\nCONDORCET WINNER")
	# print(WINNERSCONDORCET)
	barPlot(WINNERSCONDORCET,'Condorcet Winner',esperimento)
	# print("\nRUNOFF (PROBLEMA***)")
	# print(WINNERSRUNOFF)
	# print("\nAPPROVAL")
	# print("TOP-2",WINNERSAPPROVAL[0])
	barPlot(WINNERSAPPROVAL[0],'2-Approval',esperimento)
	# print("TOP-3",WINNERSAPPROVAL[1])
	barPlot(WINNERSAPPROVAL[1],'3-Approval',esperimento)
	# print("TOP-4",WINNERSAPPROVAL[2])
	barPlot(WINNERSAPPROVAL[2],'4-Approval',esperimento)

	# print("\nTWO PHASE RUNOFF")
	# print(WINNERSTWOPHASE)
	barPlot(WINNERSTWOPHASE,'Two Phase Runoff',esperimento)

	# print("\nBORDA COUNT WITH CASUAL SINGLE DROPOUT")
	# print(WINNERSRANDOMBORDA)
	barPlot(WINNERSRANDOMBORDA,'Borda with Random Dropout',esperimento)

	filename = "Plots/"+str(esperimento)+".txt"
	f=open(filename,'w')
	f.write("Plurality\n")
	f.write(str(WINNERSPLURALITY))
	f.write("\n")
	f.write("Borda Count\n")
	f.write(str(WINNERSBORDA))
	f.write("\n")
	f.write("Condorcet Winner\n")
	f.write(str(WINNERSCONDORCET))
	f.write("\n")
	f.write("2-Approval\n")
	f.write(str(WINNERSAPPROVAL[0]))
	f.write("\n")
	f.write("3-Approval\n")
	f.write(str(WINNERSAPPROVAL[1]))
	f.write("\n")
	f.write("4-Approval\n")
	f.write(str(WINNERSAPPROVAL[2]))
	f.write("\n")
	f.write("Two Phase Runoff\n")
	f.write(str(WINNERSTWOPHASE))
	f.write("\n")
	f.write("Borda with Single Random Dropout\n")
	f.write(str(WINNERSRANDOMBORDA))