def horizontal_wall():
	print '+ ', (4 * '- '), '+ ', (4 * '- '), '+'

def hollow_strip():
	print '|', (9 * ' '), '|', (9 * ' '), '|'

def deploy_2x2_grid():
	horizontal_wall()
	hollow_strip()
	hollow_strip()
	hollow_strip()
	hollow_strip()
	horizontal_wall()
	hollow_strip()
	hollow_strip()
	hollow_strip()
	hollow_strip()
	horizontal_wall()

deploy_2x2_grid()
