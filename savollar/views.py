from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Test_session, Natija, Savol

# Create your views here.
def kod(request):
    if request.method == 'POST':
        code = request.POST.get('code')

        if Test_session.objects.filter(code=code).exists():
            session = Test_session.objects.get(code=code)
            request.session['test_session_id'] = session.id
            return redirect('start-view')
        else:
            messages.error(request, 'Kod xato yoki mavjud emas!')
        
    return render(request, 'kod.html')


def verify_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        
        if Test_session.objects.filter(code=code).exists():
            session = Test_session.objects.get(code=code)
            request.session['test_session_id'] = session.id
            return redirect('start-view')
        else:
            messages.error(request, 'Kod xato yoki mavjud emas!')
            return redirect('kod-view')
    
    return redirect('kod-view')


def start1(request):
    test_session_id = request.session.get('test_session_id')
    
    if not test_session_id:
        return redirect('kod-view')
    
    try:
        session = Test_session.objects.get(id=test_session_id)
        context = {
            'session': session,
            'kurs': session.kurs.name if session.kurs else 'Noma\'lum',
            'guruh': session.guruh.name if session.guruh else 'Noma\'lum',
        }
        return render(request, 'start.html', context)
    except Test_session.DoesNotExist:
        return redirect('kod-view')




def start(request):

    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        test_session_id = request.session.get('test_session_id')

        session = Test_session.objects.get(id=test_session_id)

        new_natija_obj = Natija.objects.create(
            first_name=first_name,
            last_name=last_name,
            test_session=session
        )

        request.session['natija_id'] = new_natija_obj.id

        savollar = Savol.objects.filter(kurs=session.kurs)

        context = {
            'savollar': savollar,
            'natija_id': new_natija_obj.id
        }

        return render(request, 'savollar.html', context)

    return redirect('start-view')


def natija(request, natija_id):
    try:
        natija_obj = Natija.objects.get(id=natija_id)
    except Natija.DoesNotExist:
        return redirect('kod-view')
    
    # Get user answers from POST request
    test_session = natija_obj.test_session
    savollar = Savol.objects.filter(kurs=test_session.kurs)
    
    correct_count = 0
    incorrect_count = 0
    total_questions = savollar.count()
    
    # Calculate correct and incorrect answers
    for savol in savollar:
        user_answer = request.POST.get(f'answer_{savol.id}')
        if user_answer:
            if user_answer == savol.javob:
                correct_count += 1
            else:
                incorrect_count += 1
    
    # Calculate percentage
    percentage = int((correct_count / total_questions * 100)) if total_questions > 0 else 0
    
    context = {
        'natija': natija_obj,
        'correct_answers': correct_count,
        'incorrect_answers': incorrect_count,
        'total_questions': total_questions,
        'percentage': percentage,
    }
    
    return render(request, 'natija.html', context)
