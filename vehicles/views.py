from django.shortcuts import render_to_response, get_object_or_404
from django.http import JsonResponse
from models import Vehicle, VSNPattern 
import log
import fnmatch

# Index page
def index(req):
   return render_to_response('index.html')


# Function to lookup matching records using the input Vehicle Serial Number
# and return json response of matched vehicles
def lookupVsn(req):
    if req.method == 'POST':
       input_vsn = req.POST['vsn'].upper()
       
    matching_patterns = []
    for pattern in set(p.pattern for p in VSNPattern.objects.all()):
      if fnmatch.fnmatch(input_vsn, pattern):
	 matching_patterns.append(pattern)
        
    ### Remove any patterns from the initial lookup, that dont match exact characters in the input string 
    final_patterns = list(matching_patterns)
    for pattern in matching_patterns:
	for i in range(0, len(pattern)):
	    if pattern[i] != '*' and pattern[i] != input_vsn[i]:
	       final_patterns.remove(pattern)
	       break
      
    #### For more than one matching patterns, select the one with fewer wildcards
    #### Construct the response by looking up vehicle records from the django database
    response = dict()
    if final_patterns == []:
	response["empty"] = True
    else:
	response["empty"] = False
        if len(final_patterns) > 1:
       	    patternDict = dict([p, p.count('*')] for p in final_patterns)
	    result = min(patternDict, key=patternDict.get)
        else: 
            result = final_patterns[0]
        response["vehicles"] = list()
    	for vsnpattern in VSNPattern.objects.filter(pattern = result):
		matched_vehicle = vsnpattern.vehicle
		response["vehicles"].append({"vehicle": str(matched_vehicle)})   
    return JsonResponse(response, safe=False)
	
        
