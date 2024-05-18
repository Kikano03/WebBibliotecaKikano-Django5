from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Página en desarrollo</h1>
        <h2><strong>GRUPO #9:</strong></h2>
        <ul>
            <li><strong>Integrantes:</strong></li>
            <li><strong>CHÁVEZ MACÍAS LOYNI NICOLE</strong></li>
            <li><strong>PIN CEDEÑO JESÚS SIMÓN</strong></li>
            <li><strong>GUTIERREZ RIVAS CRISTHIAN EDUARDO</strong></li>
        </ul>
    """)
