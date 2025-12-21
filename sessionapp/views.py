from django.shortcuts import render

# Create your views here.
def sessionexample(request):
    request.session.modified = True
    if request.method == 'GET':
        return render(request,'sessionapp/session.html')
    if request.method =='POST':
        data = request.POST['t1']
        if 'prev_data' in request.session:
            request.session['prev_data'].append(data)

        else:
            request.session['prev_data'] =[data]
        output = '-'.join(request.session['prev_data'])    
        return render(request,'sessionapp/session.html',{'data':output})
    