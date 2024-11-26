import os
import multiprocessing as mp

def main():
	to_convert = []
	for d, _, fs in os.walk("."):
		for f in fs:
			if f.endswith(".raw"):
				to_convert.append(os.path.join(os.path.abspath(d), f))

	#Bryce - Modify This!!! You need your own copy of the exe and working mono (if on Mac) or .NET frmework
	base_command = "mono /Users/mitchjo/Library/Python/3.11/lib/python/site-packages/pcpfm/ThermoRawFileParser.exe -o . -f 2 -i "

	workers = mp.Pool(mp.cpu_count()-1)
	workers.map(os.system, [base_command + tc for tc in to_convert])

if __name__ == '__main__':
	mp.freeze_support()
	main()
