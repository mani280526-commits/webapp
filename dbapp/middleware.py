from django.core.exceptions import ValidationError
from django.shortcuts import redirect
class CustomMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
       #validate
       if request.method=='POST' and 'insert' in request.path_info:
           if int(request.POST['esal'])<0:
               #raise ValidationError('Negative salary is not allowed')
               return redirect('selecturl')
       resp = self.get_response(request)
       #validate
       print('After comning from view response')
       return resp  
