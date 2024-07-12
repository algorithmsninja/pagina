from django.http import HttpResponse

def pagina(request):
    
    pagina = '<h1> pagina 1 </h1>'
    
    response = HttpResponse(pagina)
    
    return response
    
    
