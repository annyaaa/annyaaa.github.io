def petitsGens(gens:list[tuple[str,int]])->tuple[int,list[str]]:
	mini=gens[0][1]
	petit=[]
	for pers in gens:
		if pers[1]<mini:
			mini=pers[1]
			petit=[pers[0]
		elif pers[1]=mini
			petit=petit + [pers[0]]
		return (mini,petit)
