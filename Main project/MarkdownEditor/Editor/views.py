from django.shortcuts import render
from markdown import markdown
from django.http import HttpResponse
import html2text



def convert_html_to_markdown(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'convert_to_markdown':
            html_content = request.POST.get('html_content')
            h = html2text.HTML2Text()
            h.ignore_images = True
            h.ignore_links = True
            converted_content = h.handle(html_content)
            return render(request, 'index.html', {'converted_html_content': converted_content})
        elif action == 'delete_html':
            return render(request, 'index.html', {'converted_html_content': ''})
        
    return render(request, 'index.html')

def convert_markdown_to_html(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'convert_to_html':
            markdown_text = request.POST.get('markdown_text')
            converted_content = markdown(markdown_text)  # Corrected line
            return render(request, 'index.html', {'converted_markdown_content': converted_content})
        elif action == 'delete_markdown':
            return render(request, 'index.html', {'converted_markdown_content': ''})
       
    return render(request, 'index.html')

    

