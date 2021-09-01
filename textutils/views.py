# manually created
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def analyze(request):
    original_text = request.POST.get('text', 'default')

    remove_punc = request.POST.get('remove_punc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    new_line_remover = request.POST.get('new_line_remover', 'off')
    extra_space_remover = request.POST.get('extra_space_remover', 'off')

    params = {'required_feature1': None, 'required_feature2': None, 'required_feature3': None,
              'required_feature4': None}

    if remove_punc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in original_text:
            if char not in punctuations:
                analyzed += char
        params['required_feature1'] = 'remove punctuations'
        original_text = analyzed

    if uppercase == "on":
        analyzed = ""
        for char in original_text:
            analyzed += char.upper()
        params['required_feature2'] = 'UPPERCASE'
        original_text = analyzed

    if new_line_remover == "on":
        analyzed = ""
        for char in original_text:
            if char != "\n" and char != "\r":
                analyzed += char
            else:
                analyzed += " "
        params['required_feature3'] = 'new line remover'
        original_text = analyzed

    if extra_space_remover == "on":
        analyzed = ""
        for index, char in enumerate(original_text):
            if not (original_text[index] == " " and original_text[index + 1] == " "):
                analyzed += char
        params['required_feature4'] = 'extra_space_remover'
        original_text = analyzed

    if remove_punc == "off" and uppercase == "off" and new_line_remover == "off" and extra_space_remover == "off":
        return HttpResponse("No Analyser is selected")

    params['analyzed_text'] = original_text

    return render(request, 'analyze.html', params)
