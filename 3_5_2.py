def horizontal_wall():
	print '+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+'

def hollow_strip():
	print '|', (7 * ' '), '|', (7 * ' '), '|', (7 * ' '), '|', (7 * ' '), '|'

def deploy_4x4_grid():
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

deploy_4x4_grid()
