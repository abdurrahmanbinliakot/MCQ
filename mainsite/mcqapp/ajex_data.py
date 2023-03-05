from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from .models import MCQ

@require_POST
def print_card(request):
    question_id = request.POST['question_id']
    question = get_object_or_404(MCQ, pk=question_id)
    rendered_template = render_to_string('card.html', {'question': question})
    return JsonResponse({'template': rendered_template})
