from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')
def cgpa(request):
    chephy=request.GET["BS3271"]
    che=request.GET["CY3251"]
    py=request.GET["GE3151"]
    pylab=request.GET["GE3171"]
    eng=request.GET["HS3151"]
    mat=request.GET["MA3151"]
    phy=request.GET["PH3151"]
    if chephy=='A+':
        chephy1=9
    elif chephy=='O':
        chephy1=10
    elif chephy=='A':
        chephy1=8
    elif chephy=='B+':
        chephy1=7
    elif chephy=='B':
        chephy1=6
    elif chephy=='c':
        chephy1=5
    else:
        chephy1=0
    chephy1*=4
    if che=='A+':
        che1=9
    elif che=='O':
        che1=10
    elif che=='A':
        che1=8
    elif che=='B+':
        che1=7
    elif che=='B':
        che1=6
    elif che=='c':
        che1=5
    else:
        che1=0
    che1*=3
    if py=='A+':
        py1=9
    elif py=='O':
        py1=10
    elif py=='A':
        py1=8
    elif py=='B+':
        py1=7
    elif py=='B':
        py1=6
    elif py=='c':
        py1=5
    else:
        py1=0
    py1*=4
    if pylab=='A+':
        pylab1=9
    elif pylab=='O':
        pylab1=10
    elif pylab=='A':
        pylab1=8
    elif pylab=='B+':
        pylab1=7
    elif pylab=='B':
        pylab1=6
    elif pylab=='c':
        pylab1=5
    else:
        pylab1=0
    pylab1*=3
    if eng=='A+':
        eng1=9
    elif eng=='O':
        eng1=10
    elif eng=='A':
        eng1=8
    elif eng=='B+':
        eng1=7
    elif eng=='B':
        eng1=6
    elif eng=='c':
        eng1=5
    else:
        eng1=0
    eng1*=4
    if mat=='A+':
        mat1=9
    elif mat=='O':
        mat1=10
    elif mat=='A':
        mat1=8
    elif mat=='B+':
        mat1=7
    elif mat=='B':
        mat1=6
    elif mat=='c':
        mat1=5
    else:
        mat1=0
    mat1*=4
    if phy=='A+':
        phy1=9
    elif phy=='O':
        phy1=10
    elif phy=='A':
        phy1=8
    elif phy=='B+':
        phy1=7
    elif phy=='B':
        phy1=6
    elif phy=='c':
        phy1=5
    else:
        phy1=0
    phy1*=3

    cgpa= (py1+che1+chephy1+pylab1+eng1+mat1+phy1)/25
    return render(request,"https://reshiweb.github.io/reshiweb/Django/Scripts/Django_Project/templates/CGPA.html",{'CGPA':cgpa})
