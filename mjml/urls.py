from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from mjml.utils import get_context_for_template, transpile_mjml_to_html


def template_preview(request, template_name):
    success = transpile_mjml_to_html(template_name)
    if not success:
        return HttpResponse(f'Error transpiling MJML: {template_name}')
    context = get_context_for_template(template_name)
    return render(request, f'email/{template_name}.html', context)


urlpatterns = [
    path('<str:template_name>', template_preview, name='template_preview')
]
