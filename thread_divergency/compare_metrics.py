# compare metrics.txt and metrics_opt.txt
import re, pprint


def read_metrics(filename):
	
	metrics = {}
	with open(filename,'r') as f:
		lines = f.readlines()
		for line in lines:
			line = line.strip()
			
			if line[0]=='1':
				
				line = re.split('\s\s+',line)
				#print line
				metrics[line[1]] = {"name": line[2], "value": line[3:]}
				
	return metrics

metrics = read_metrics('metrics.txt')
metrics_opt = read_metrics('metrics_opt.txt')

#pprint.pprint( metrics)
# load metrics description

mdict = {}
with open('query_metrics.txt','r') as f:
	lines = f.readlines()
	for i in xrange(3,len(lines)):
		line = lines[i].strip()
		if len(line):
			line = line.split(':')
			mdict[line[0].strip()] = line[1].strip()	
			
# compare metrics and metrics_opt

for key in sorted(metrics.keys()):
	if metrics[key]["value"][-1]!=metrics_opt[key]["value"][-1]:
		print "---------------"
		print key+" ( "+metrics[key]["name"] + "):  "+ mdict[key]
		print "\t No optimize: "+str(metrics[key]["value"])
		print "\t with optimi: "+str(metrics_opt[key]["value"])




