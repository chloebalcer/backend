from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
import subprocess

@csrf_exempt
def execute_code(request):
    if request.method =='POST':
        print(str(request.body))
        command = request.body.decode("utf-8")
        process = subprocess.Popen(["python", "-c", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = ""
        stderr = ""
        try:
            stdout= process.communicate()[0]
            stderr= process.communicate()[1]
        except :
            pass
        response = "{}{}".format(stdout, stderr)
        print("Response", response)
        return JsonResponse({'data': response})
        #return HttpResponse(response, content_type="text/plain")
