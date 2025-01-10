from django.shortcuts import render
from django.http import JsonResponse

def mental_health_test(request):
    if request.method == 'POST':
        q1 = int(request.POST.get('q1', 0))
        q2 = int(request.POST.get('q2', 0))
        q3 = int(request.POST.get('q3', 0))
        
        total_score = q1 + q2 + q3
        
        if total_score >= 10:
            recommendation = "Disarankan untuk berkonsultasi dengan profesional kesehatan mental."
        else:
            recommendation = "Saat ini, Anda tidak memerlukan konsultasi, tetapi tetap jaga kesehatan mental Anda."
        
        return JsonResponse({
            "status": "success",
            "message": recommendation
        })
    
    return render(request, 'tes/tes.html')
