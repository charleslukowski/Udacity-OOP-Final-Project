def poker(hands):
	"""Return the best hand: poker([hand,...]) => hand"""
	return max(hands, key=hand_rank) #???

def hand_rank(hand):
	"""	"""
	return None

def test():
	"""Test case for functions in poker program"""

	#Define 3 hands
	sf = "6C 7C 8C 9C TC".split()
	fk = "9D 9H 9S 9C 7D".split()
	fh = "TD TC TH 7C 7D".split()

	#asset, assume is true, but if not will print an error message
	assert poker([sf, fk, fh]) == sf

	# Add 2 new assert statements here. The first 
    # should check that when fk plays fh, fk 
    # is the winner. The second should confirm that
    # fh playing against fh returns fh.
    assert poker([fh, fk]) == fk
    assert poker([fh, fh]) == fh
	

	return "tests pass"

	
print test()