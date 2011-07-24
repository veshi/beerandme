from django.shortcuts import render_to_response

def new_result(request):
    if request.method == 'POST':
        pass
    else:
        pass
    return render_to_response("new_result.html", {})

def home(request):
   return render_to_response('home.html', {})
