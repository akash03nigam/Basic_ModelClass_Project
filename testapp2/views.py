from django.shortcuts import render
import datetime
# Create your views here.
def view(request):
    d= datetime.datetime.now()
    h= int(d.strftime('%H'))
    X= "Hello Lovelies"
    if h<12:
        msg= X+' Good Morning'
    elif h<16:
        msg= X+' Good Afternoon'
    elif h<20:
        msg= X+' Good Evening'
    else:
        msg= X+' Good Night'

    return render(request, 'code_app/results.html',{'Msg':msg,'date': d } )            
